import streamlit as st
from recommend import MovieRecommender
@st.cache_resource
def load_recommender():
    return MovieRecommender("imdb_movies_2024.csv")

recommender = load_recommender()

st.title("🎬 IMDb Movie Recommender")
st.write("Enter a storyline and get the top 5 similar movies!")

user_input = st.text_area("Storyline:", "")

if st.button("Recommend"):
    if user_input.strip():
        results = recommender.recommend(user_input, top_n=5)
        st.subheader("🔮 Recommended Movies:")
        for _, row in results.iterrows():
            st.markdown(f"**{row['Movie Name']}**")
            st.write(row['Storyline'])
            st.write("---")
    else:
        st.warning("Please enter a storyline before clicking Recommend.")
