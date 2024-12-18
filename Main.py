import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def load_books_dataset(file_path):
    # Load dataset into a pandas dataframe
    books = pd.read_csv(file_path)
    
    # Drop rows where crucial fields (e.g., title, categories, description) are missing
    books = books.dropna(subset=['title', 'categories', 'description'])
    
    # Fill missing authors or subtitles with empty strings
    books['authors'] = books['authors'].fillna('')
    books['subtitle'] = books['subtitle'].fillna('')

    # Reset the index after cleaning
    books = books.reset_index(drop=True)
    
    return books

def get_recommendations(user_preference, books):
    # Combining 'description' and 'categories' for vectorization
    books['combined_features'] = books['description'] + ' ' + books['categories']
    
    # Vectorize the combined features and calculate cosine similarity
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(books['combined_features'].fillna(''))
    cosine_sim = cosine_similarity(count_matrix)

    # Check if sizes match
    assert len(cosine_sim) == len(books), "Mismatch between similarity matrix and book data"

    recommendations = []
    for idx, row in books.iterrows():
        if user_preference.lower() in row['categories'].lower():
            similar_books = list(enumerate(cosine_sim[idx]))
            similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)
            
            # Collecting top 2 similar books
            for book in similar_books[1:3]:  # Skip the first book (itself)
                book_index = book[0]
                if book_index < len(books):
                    recommended_book = books.iloc[book_index]['title']
                    if recommended_book not in recommendations:
                        recommendations.append(recommended_book)
                else:
                    print(f"Index {book_index} out of bounds for books with size {len(books)}")
    return recommendations[0:5]




# Load the CSV dataset
st.title('Online Book Recommendations')

# File path to the dataset
file_path = 'Books.csv'
books = load_books_dataset(file_path)

# Sidebar for user input
st.sidebar.header("User Preferences")

# Input field for genre preference
genre_input = st.sidebar.text_input('Enter your preferred genre (e.g., Fiction, Fantasy)')

# Button to trigger recommendation
if st.sidebar.button('Get Recommendations'):
    if genre_input:
        # Fetch recommendations based on the loaded dataset
        recommendations = get_recommendations(genre_input, books)
        if recommendations:
            st.subheader(f"Books recommended for '{genre_input}' genre:")
            for rec in recommendations:
                st.write(f"- {rec}")
        else:
            st.write(f"No recommendations found for '{genre_input}' genre.")
    else:
        st.write("Please enter a genre to get recommendations.")
