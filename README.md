# Online Book Recommendation System

## Overview
The Online Book Recommendation System is a simple web application that suggests books based on user preferences like genres or categories. Built with Python and Streamlit, it uses cosine similarity on text features to provide personalized recommendations.

---

## Features
- **Interactive User Interface**: Built using Streamlit, the app is user-friendly and easy to navigate.
- **Genre-Based Recommendations**: Users can input their preferred genre (e.g., "Fiction" or "Fantasy") to get book suggestions.
- **Flexible Dataset Handling**: Supports book datasets in CSV format, which can be customized as needed.
- **Cosine Similarity Matching**: Combines book descriptions and categories to calculate similarity for accurate recommendations.

---

## Prerequisites
- Python 3.8+
- Required Python libraries:
  - pandas
  - scikit-learn
  - streamlit

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/book-recommendation-system.git
   cd book-recommendation-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your dataset:
   - Ensure you have a CSV file (e.g., `Books.csv`) with the following columns:
     - `title` (Book title)
     - `categories` (Genre or category)
     - `description` (Brief description of the book)
     - `authors` (Author names, optional)
     - `subtitle` (Subtitle, optional)

   Place this file in the root directory or modify the `file_path` in the script to the correct location.

---

## Usage
1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Interact with the application:
   - Enter your preferred genre in the sidebar.
   - Click the **Get Recommendations** button to view book suggestions.

---

## File Structure
- `app.py`: Main application script.
- `requirements.txt`: Python dependencies for the project.
- `Books.csv`: Sample dataset (to be provided by the user).

---

## Sample Dataset Structure
Ensure your dataset follows this structure:

| title              | categories        | description                                      | authors       | subtitle              |
|--------------------|-------------------|------------------------------------------------|---------------|-----------------------|
| Book Title 1       | Fiction           | A thrilling tale of adventure and mystery.     | Author Name   | An Exciting Journey   |
| Book Title 2       | Fantasy, Adventure| An epic saga set in a magical world.           | Author Name 2 | The Magical Realm     |

---

## How It Works
1. **Data Preprocessing**:
   - Missing values in critical fields (e.g., `title`, `categories`, `description`) are dropped.
   - Non-essential fields like `authors` and `subtitle` are filled with empty strings if missing.

2. **Feature Engineering**:
   - Combines `description` and `categories` into a single feature for text vectorization.

3. **Vectorization & Similarity Calculation**:
   - Uses **CountVectorizer** to convert text into feature vectors.
   - Computes cosine similarity between books to find similar ones.

4. **Recommendations**:
   - Identifies books similar to those matching the user’s genre preference.
   - Displays the top 5 recommended books.

---

## Future Enhancements
- Integrate **TF-IDF Vectorization** for improved text representation.
- Add filters for multiple preferences (e.g., author, publication year).
- Enhance the dataset to include ratings and reviews for better recommendations.
- Deploy the application using cloud services like AWS or Heroku.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---

## Contributions
Contributions are welcome! If you'd like to improve this project, feel free to submit a pull request or open an issue on GitHub.

