import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, csv_file="imdb_movies_2024.csv"):
        try:
            self.df = pd.read_csv(csv_file)
            print(f"✅ Loaded {csv_file} successfully")
        except FileNotFoundError:
            raise FileNotFoundError(f"❌ {csv_file} not found. Run scraper.py first.")

        self.df["Storyline"] = self.df["Storyline"].fillna("").astype(str)
        self.df = self.df[self.df["Storyline"].str.strip() != ""]

        if self.df.empty:
            raise ValueError("❌ No valid storylines found in dataset. Please check your CSV.")

        self.vectorizer = TfidfVectorizer(stop_words="english", token_pattern=r"(?u)\b\w+\b")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["Storyline"])
        print("✅ TF-IDF matrix built successfully")
        print("Vocabulary size:", len(self.vectorizer.vocabulary_))
        print("TF-IDF matrix shape:", self.tfidf_matrix.shape)

    def recommend(self, input_storyline, top_n=5):
        input_vec = self.vectorizer.transform([input_storyline])
        similarity_scores = cosine_similarity(input_vec, self.tfidf_matrix).flatten()
        top_indices = similarity_scores.argsort()[-top_n:][::-1]
        recommendations = self.df.iloc[top_indices][["Movie Name", "Storyline"]]
        return recommendations

if __name__ == "__main__":
    recommender = MovieRecommender("imdb_movies_2024.csv")
    test_story = "A young wizard begins his journey at a magical school."
    print("🔮 Recommendations for your storyline:")
    print(recommender.recommend(test_story))
