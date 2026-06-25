import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Simple Database
data = {
    'title': ['Matrix', 'Inception', 'Toy Story', 'Avengers'],
    'genres': ['Sci-Fi Action', 'Sci-Fi Action', 'Animation Kids', 'Action Sci-Fi']
}
df = pd.DataFrame(data)

# 2. Convert genres to a matrix
cv = CountVectorizer()
matrix = cv.fit_transform(df['genres'])

# 3. Calculate similarity
similarity = cosine_similarity(matrix)

# 4. Recommendation function
def get_recommendations(title):
    idx = df[df['title'] == title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    # Get top 2 matches (excluding itself)
    return [df['title'][i[0]] for i in scores[1:3]]

print(get_recommendations('Matrix'))