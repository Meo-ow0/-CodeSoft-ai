# AI-Powered Movie Recommendation System

A content-based recommendation engine that suggests movies based on genre, keywords, and metadata analysis. Developed as part of an AI/ML internship project.

##  The Logic
This system uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to vectorize movie metadata and **Cosine Similarity** to calculate the mathematical proximity between titles. By converting text-based features into high-dimensional vectors, the system can determine how "close" two movies are in terms of their content.

##  Key Features
- **Content-Based Filtering:** Recommends items based on user preferences and movie features.
- **Typo-Tolerance:** Integrated `difflib` to match user input even with minor spelling errors.
- **Efficient Lookup:** Uses Pandas Series mapping for $O(1)$ search performance.
- **Scalable:** Built on a modular pipeline allowing for dataset swaps.

## Tech Stack
- **Language:** Python
- **Libraries:** - `pandas`, `numpy`: Data manipulation
    - `scikit-learn`: Vectorization and similarity scoring
    - `difflib`: String matching
- **Environment:** Jupyter Notebooks (VS Code)

## How it Works
1. **Data Preprocessing:** Missing values are handled and features are combined into a single "content" string.
2. **Vectorization:** `TfidfVectorizer` converts text into numerical vectors.
3. **Similarity Mapping:** `cosine_similarity` generates a matrix comparing every movie against every other movie.
4. **Recommendation:** The function retrieves the top $N$ indices based on similarity scores.

## Usage
To run the recommendation engine:
1. Load your dataset (`movies.csv`) in the notebook.
2. Initialize the `TfidfVectorizer` to generate the similarity matrix.
3. Call the `get_recommendations('Movie Title')` function to output the top matches.

---
*Developed as part of an Internship Project.*