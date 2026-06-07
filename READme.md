# IMDb Movie Recommendation System Using Storylines
## Project Overview
This project is about building a movie recommendation system using IMDb 2024 movie data.  
We scrape movie names and storylines from IMDb with Selenium, clean the text, and then use TF‑IDF + Cosine Similarity to recommend similar movies.  
Finally, we provide a Streamlit app where users can type a storyline and get the top 5 recommended movies.

## Skills Learned
- Selenium (web scraping)
- Python
- Pandas
- Streamlit
- NLP (TF‑IDF, Cosine Similarity)
- Data Cleaning
- Data Analysis
- Visualization
- User Interface Development

## Project Structure
 ├── scraper.py              # Scrapes IMDb 2024 movies (Name + Storyline) and saves to CSV
 ├── movie.py           # Cleans and vectorizes storylines using TF-IDF
 ├── recommend.py            # MovieRecommender class with cosine similarity
 ├── app.py                  # Streamlit app for interactive recommendations
 ├── imdb_movies_2024.csv    # Dataset (scraped IMDb movies)
 ├── README.md               # Project documentation
 └── requirements.txt        # Python dependencies


- **scraper.py** → extracts movie names and storylines from IMDb and saves them into a CSV file.  
- **movie.py** → cleans the text and builds the TF‑IDF matrix.  
- **recommend.py** → contains the recommender class that uses cosine similarity.  
- **app.py** → Streamlit app for user interaction.  
- **imdb_movies_2024.csv** → dataset of scraped movies.  
- **requirements.txt** → dependencies list.


# Workflow
1. Scrape IMDb 2024 movies (names + storylines) → CSV file
2. Clean and preprocess the text
3. Convert text into vectors using TF‑IDF
4. Compute similarity scores with Cosine Similarity
5. Recommend top 5 movies based on input storyline
6. Show results in Streamlit app

# Example Use Case
Input:
A young wizard begins his journey at a magical school where he makes friends and enemies, facing dark forces along the way.

Output: 
Top recommended movies with similar plots (names + storylines).



