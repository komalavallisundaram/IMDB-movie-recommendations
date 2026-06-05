import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def main():
    
    try:
        df = pd.read_csv("imdb_movies_2024.csv")
        print("✅ Loaded imdb_movies_2024.csv successfully")
    except FileNotFoundError:
        raise FileNotFoundError("❌ imdb_movies_2024.csv not found. Run scraper.py first.")

    
    df["Storyline"] = df["Storyline"].fillna("").astype(str)
    df = df[df["Storyline"].str.strip() != ""]

    if df.empty:
        raise ValueError("❌ No valid storylines found in imdb_movies_2024.csv. Please check your scraped data.")

    vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words="english")
    X = vectorizer.fit_transform(df["Storyline"])
    print("✅ TF-IDF vectorization complete")
    print("Vocabulary size:", len(vectorizer.vocabulary_))
    print("TF-IDF matrix shape:", X.shape)  # rows = movies, cols = features

if __name__ == "__main__":
    main()
