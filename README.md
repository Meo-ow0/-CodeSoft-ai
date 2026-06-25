# Rule-Based Chatbot

I made this ruled based chatbot application built for my internship project. This project demonstrates foundational natural language processing (NLP) concepts using JavaScript and simple pattern matching.

##  The Concept
This chatbot is designed to provide a warm, approachable experience. It uses a custom-defined rule engine to process user inputs and return appropriate responses. The aesthetic is inspired by a calm "coffee shop" vibe to ensure a professional and welcoming user interface.

##  Features
- **Rule-Based Logic:** Uses pattern matching to identify user intent.
- **Responsive UI:** A clean, CSS-styled chat interface.
- **Coffee Palette:** Warm beige, tan, and espresso tones for a modern look.
- **Lightweight:** Built with simple HTML, CSS, and vanilla JavaScript.

## Tech Stack
- **Frontend:** HTML5, CSS3
- **Scripting:** Vanilla JavaScript
- **Editor:** Visual Studio Code

## How to Run
1. Ensure you have **Visual Studio Code** installed.
2. Install the **Live Server** extension from the VS Code marketplace.
3. Open your project folder in VS Code.
4. Right-click `index.html` and select **"Open with Live Server"**.
5. The application will open in your default browser.


AI-Powered Movie Recommendation System
A content-based recommendation engine that suggests movies based on genre, keywords, and metadata analysis. Developed as part of an AI/ML internship project.

The Logic
This system uses TF-IDF (Term Frequency-Inverse Document Frequency) to vectorize movie metadata and Cosine Similarity to calculate the mathematical proximity between titles. By converting text-based features into high-dimensional vectors, the system can determine how "close" two movies are in terms of their content.

Key Features
Content-Based Filtering: Recommends items based on user preferences and movie features.
Typo-Tolerance: Integrated difflib to match user input even with minor spelling errors.
Efficient Lookup: Uses Pandas Series mapping for 
O
(
1
)
 search performance.
Scalable: Built on a modular pipeline allowing for dataset swaps.
Tech Stack
Language: Python
Libraries: - pandas, numpy: Data manipulation
scikit-learn: Vectorization and similarity scoring
difflib: String matching
Environment: Jupyter Notebooks (VS Code)
How it Works
Data Preprocessing: Missing values are handled and features are combined into a single "content" string.
Vectorization: TfidfVectorizer converts text into numerical vectors.
Similarity Mapping: cosine_similarity generates a matrix comparing every movie against every other movie.
Recommendation: The function retrieves the top 
N
 indices based on similarity scores.
Usage
To run the recommendation engine:

Load your dataset (movies.csv) in the notebook.
Initialize the TfidfVectorizer to generate the similarity matrix.
Call the get_recommendations('Movie Title') function to output the top matches.
Developed as part of an Internship Project.
##  How it Works
The bot matches user input against a set of predefined keywords. If a match is found, it returns a specific response; otherwise, it returns a friendly default message to maintain conversation flow.

---
*Developed as part of an Internship Project.*
