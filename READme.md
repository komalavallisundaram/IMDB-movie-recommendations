# 🎬 IMDb Movie Recommendation System Using Storylines

##  Project Overview
This project builds a **movie recommendation system** using IMDb 2024 movie data.  
We scrape movie names and storylines with **Selenium**, clean the text, and then apply **TF‑IDF + Cosine Similarity** to recommend similar movies.  
Finally, a **Streamlit app** allows users to type a storyline and get the **top 5 recommended movies**.

## Skills Learned
- Web Scraping with **Selenium**
- **Python** programming
- **Pandas** for data handling
- **Streamlit** for interactive UI
- **NLP techniques** (TF‑IDF, Cosine Similarity)
- Data Cleaning & Preprocessing
- Exploratory Data Analysis
- Basic Visualization
- User Interface Development

##  Project Structure
├── scraper.py              # Scrapes IMDb 2024 movies (Name + Storyline) → CSV
├── movie.py                 # Cleans and vectorizes storylines using TF-IDF
├── recommend.py             # MovieRecommender class with cosine similarity
├── app.py                   # Streamlit app for interactive recommendations
├── imdb_movies_2024.csv     # Dataset (scraped IMDb movies)
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies

### File Details
- **scraper.py** → Extracts movie names & storylines from IMDb and saves them into a CSV file.  
- **movie.py** → Cleans text and builds the TF‑IDF matrix.  
- **recommend.py** → Contains the recommender class using cosine similarity.  
- **app.py** → Streamlit app for user interaction.  
- **imdb_movies_2024.csv** → Dataset of scraped movies.  
- **requirements.txt** → List of dependencies.

##  Workflow
1. Scrape IMDb 2024 movies (names + storylines) → CSV file  
2. Clean and preprocess the text  
3. Convert text into vectors using **TF‑IDF**  
4. Compute similarity scores with **Cosine Similarity**  
5. Recommend **top 5 movies** based on input storyline  
6. Display results in the **Streamlit app**

