import streamlit as st
import pandas as pd
from recommender import (
    load_data,
    create_user_movie_matrix,
    get_user_watched_movies,
    recommend_movies_item_based,
    get_popular_movies
)

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.58), rgba(0,0,0,0.72)),
        url("https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=1800&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: white;
}

html, body, .stApp, [data-testid="stAppViewContainer"] {
    margin: 0 !important;
    padding: 0 !important;
}

[data-testid="stAppViewContainer"] > .main {
    padding-top: 0 !important;
}

.block-container {
    padding-top: 0rem !important;
    padding-bottom: 1rem !important;
    margin-top: 0 !important;
    max-width: 1280px;
}

header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0rem !important;
}

div[data-testid="stToolbar"] {
    top: 0.15rem;
    right: 0.5rem;
}

section[data-testid="stSidebar"] {
    background: rgba(10,10,10,0.98) !important;
    border-right: 1px solid rgba(255,255,255,0.06);
}

[data-testid="collapsedControl"] {
    color: white !important;
}

.logo {
    font-size: 2.2rem;
    font-weight: 900;
    color: #E50914;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.login-wrap,
.profile-wrap {
    min-height: auto;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding-top: 0 !important;
    margin-top: 0 !important;
}

.login-panel,
.profile-panel {
    width: 100%;
    max-width: 1100px;
    background: rgba(0,0,0,0.62);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 26px;
    padding: 12px 30px 28px 30px;
    margin-top: 0 !important;
    box-shadow: 0 18px 50px rgba(0,0,0,0.45);
    backdrop-filter: blur(6px);
}

.login-box {
    max-width: 420px;
    margin: 10px auto 0 auto;
    background: rgba(20,20,20,0.86);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 26px;
}

.login-title,
.profile-title {
    font-size: 2.5rem;
    font-weight: 800;
    color: white;
    margin-bottom: 6px;
}

.login-subtitle,
.profile-subtitle {
    color: #d1d5db;
    margin-bottom: 18px;
    font-size: 0.98rem;
}

.hero {
    background: linear-gradient(135deg, rgba(229,9,20,0.92), rgba(20,20,20,0.94));
    border-radius: 24px;
    padding: 26px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.35);
    margin-top: 0.2rem;
    margin-bottom: 18px;
}

.hero h1 {
    font-size: 2.6rem;
    font-weight: 900;
    margin: 0 0 8px 0;
    color: white;
}

.hero p {
    margin: 0;
    color: #f3f4f6;
    font-size: 1rem;
}

.glass-card {
    background: rgba(18,18,18,0.86);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.25);
}

.metric-card {
    background: linear-gradient(135deg, rgba(25,25,25,0.95), rgba(10,10,10,0.98));
    border: 1px solid rgba(229,9,20,0.22);
    border-radius: 20px;
    padding: 20px;
    text-align: center;
}

.metric-card h3 {
    margin: 0;
    color: #d1d5db;
    font-size: 1rem;
    font-weight: 600;
}

.metric-card h2 {
    margin: 10px 0 0 0;
    color: white;
    font-size: 2rem;
    font-weight: 900;
}

.profile-card {
    background: rgba(24,24,24,0.92);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 18px 14px;
    text-align: center;
}

.profile-avatar {
    width: 105px;
    height: 105px;
    margin: 0 auto 12px auto;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #E50914, #7f1d1d);
    color: white;
    font-size: 40px;
    font-weight: 800;
}

.profile-name {
    color: white;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 6px;
}

.profile-meta {
    color: #cbd5e1;
    font-size: 0.9rem;
    margin-bottom: 12px;
}

.section-title {
    color: white;
    font-size: 1.25rem;
    font-weight: 800;
    margin-bottom: 10px;
}

.small-note {
    color: #d1d5db;
    font-size: 0.95rem;
    margin-bottom: 10px;
}

.badge {
    display: inline-block;
    background: rgba(229,9,20,0.14);
    border: 1px solid rgba(229,9,20,0.35);
    color: white;
    padding: 8px 14px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.92rem;
    margin-bottom: 12px;
}

.poster-strip {
    display: flex;
    gap: 14px;
    overflow-x: auto;
    padding-bottom: 8px;
}

.poster-box {
    min-width: 190px;
    background: rgba(30,30,30,0.95);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 12px;
    text-align: center;
}

.poster-box img {
    width: 100%;
    height: 230px;
    border-radius: 12px;
    object-fit: cover;
    margin-bottom: 10px;
}

.poster-box p {
    color: white;
    font-size: 0.92rem;
    font-weight: 600;
    margin: 0;
}

div[data-testid="stDataFrame"] {
    background: rgba(255,255,255,0.03);
    border-radius: 14px;
    padding: 6px;
    border: 1px solid rgba(255,255,255,0.06);
}

div[data-baseweb="select"] > div,
div[data-baseweb="base-input"] > div,
div[data-baseweb="input"] > div {
    background: rgba(40,40,40,0.95) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

div[data-baseweb="select"] *,
div[data-baseweb="base-input"] *,
div[data-baseweb="input"] * {
    color: white !important;
}

.stTextInput label,
.stSelectbox label,
.stMultiSelect label,
.stSlider label,
.stRadio label,
.stNumberInput label {
    color: white !important;
    font-weight: 600 !important;
}

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 12px;
    padding: 0.82rem 1rem;
    font-weight: 800;
    font-size: 1rem;
    color: white;
    background: #E50914;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #b20710;
    transform: translateY(-1px);
    color: white;
}

.stAlert {
    border-radius: 14px;
}

hr {
    border-color: rgba(255,255,255,0.08);
}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def cached_load():
    return load_data()


def get_mood_genres(mood):
    mapping = {
        "Anything": [],
        "Action Night": ["Action", "Adventure", "Thriller", "Sci-Fi"],
        "Feel Good": ["Comedy", "Animation", "Children"],
        "Mind-Bending": ["Sci-Fi", "Mystery", "Thriller", "IMAX"],
        "Romantic": ["Romance", "Drama", "Comedy"],
        "Dark & Intense": ["Crime", "Thriller", "War", "Mystery", "Horror"],
        "Family Time": ["Animation", "Children", "Adventure", "Fantasy", "Comedy"]
    }
    return mapping.get(mood, [])


def combine_filters(df, manual_genres, mood):
    filtered = df.copy()
    mood_genres = get_mood_genres(mood)

    if mood_genres and "genres" in filtered.columns:
        mood_pattern = "|".join(mood_genres)
        filtered = filtered[
            filtered["genres"].fillna("").str.contains(mood_pattern, case=False, na=False)
        ]

    if manual_genres and "Any" not in manual_genres and "genres" in filtered.columns:
        manual_pattern = "|".join(manual_genres)
        filtered = filtered[
            filtered["genres"].fillna("").str.contains(manual_pattern, case=False, na=False)
        ]

    return filtered


def get_augmented_ratings(base_ratings):
    if "custom_ratings" not in st.session_state:
        st.session_state.custom_ratings = pd.DataFrame(columns=["userId", "movieId", "rating", "timestamp"])
    if st.session_state.custom_ratings.empty:
        return base_ratings.copy()
    return pd.concat([base_ratings, st.session_state.custom_ratings], ignore_index=True)


def add_custom_rating(user_id, movie_id, rating_value):
    new_row = pd.DataFrame([{
        "userId": user_id,
        "movieId": movie_id,
        "rating": rating_value,
        "timestamp": 999999999
    }])

    existing = st.session_state.custom_ratings
    if not existing.empty:
        existing = existing[~((existing["userId"] == user_id) & (existing["movieId"] == movie_id))]
    st.session_state.custom_ratings = pd.concat([existing, new_row], ignore_index=True)


movies, ratings = cached_load()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "entered_app" not in st.session_state:
    st.session_state.entered_app = False
if "selected_user" not in st.session_state:
    st.session_state.selected_user = None
if "custom_ratings" not in st.session_state:
    st.session_state.custom_ratings = pd.DataFrame(columns=["userId", "movieId", "rating", "timestamp"])

fixed_profiles = [
    {"label": "Person 1", "userId": 1, "emoji": "🎬"},
    {"label": "Person 2", "userId": 2, "emoji": "🍿"},
    {"label": "Person 3", "userId": 3, "emoji": "⭐"},
]

if not st.session_state.logged_in:
    st.markdown('<div class="login-wrap"><div class="login-panel">', unsafe_allow_html=True)
    st.markdown('<div class="logo">CineMatch</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-title">Sign In</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">Enter your login details to continue</div>', unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    username = st.text_input("Username", placeholder="Enter username")
    password = st.text_input("Password", type="password", placeholder="Enter password")

    if st.button("Login"):
        if username.strip() and password.strip():
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Enter both username and password.")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
    st.stop()

if not st.session_state.entered_app:
    st.markdown('<div class="profile-wrap"><div class="profile-panel">', unsafe_allow_html=True)
    st.markdown('<div class="logo">CineMatch</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-title">Who’s watching?</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-subtitle">Choose a profile to continue</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    cols = [c1, c2, c3]

    for col, profile in zip(cols, fixed_profiles):
        with col:
            st.markdown(
                f"""
                <div class="profile-card">
                    <div class="profile-avatar">{profile['emoji']}</div>
                    <div class="profile-name">{profile['label']}</div>
                    <div class="profile-meta">Movie profile</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"Continue as {profile['label']}", key=f"profile_{profile['userId']}"):
                st.session_state.selected_user = profile["userId"]
                st.session_state.entered_app = True
                st.rerun()

    if st.button("Back to Login"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown('</div></div>', unsafe_allow_html=True)
    st.stop()

augmented_ratings = get_augmented_ratings(ratings)
user_movie_matrix = create_user_movie_matrix(augmented_ratings)

st.markdown("""
<div class="hero">
    <h1>🎬 CineMatch</h1>
    <p>Discover films, track watched titles, and get smarter recommendations from your own viewing history.</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("CineMatch")
page = st.sidebar.radio("Browse", ["Home", "Personalized Picks", "Popular Now", "Add Watched Movie"])

all_genres = set()
for g in movies["genres"].dropna():
    for part in g.split("|"):
        if part.strip():
            all_genres.add(part.strip())

genre_options = ["Any"] + sorted(all_genres)
selected_genres = st.sidebar.multiselect(
    "What type of movie do you want?",
    genre_options,
    default=["Any"]
)

mood = st.sidebar.selectbox(
    "Choose your mood",
    ["Anything", "Action Night", "Feel Good", "Mind-Bending", "Romantic", "Dark & Intense", "Family Time"]
)

num_recommendations = st.sidebar.slider("How many recommendations?", 5, 20, 10)

switch_profiles = {1: "Person 1", 2: "Person 2", 3: "Person 3"}
selected_user = st.sidebar.selectbox(
    "Switch profile",
    [1, 2, 3],
    format_func=lambda x: switch_profiles[x],
    index=[1, 2, 3].index(st.session_state.selected_user)
)

if selected_user != st.session_state.selected_user:
    st.session_state.selected_user = selected_user
    st.rerun()

if st.sidebar.button("Logout Profile"):
    st.session_state.entered_app = False
    st.session_state.selected_user = None
    st.rerun()

if st.sidebar.button("Sign Out"):
    st.session_state.logged_in = False
    st.session_state.entered_app = False
    st.session_state.selected_user = None
    st.rerun()

st.markdown(
    f'<div class="badge">Active viewer: {switch_profiles[st.session_state.selected_user]}</div>',
    unsafe_allow_html=True
)

total_movies = movies["movieId"].nunique()
total_users = ratings["userId"].nunique()
total_ratings = len(augmented_ratings)

m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(f'<div class="metric-card"><h3>Total Movies</h3><h2>{total_movies}</h2></div>', unsafe_allow_html=True)
with m2:
    st.markdown(f'<div class="metric-card"><h3>Total Users</h3><h2>{total_users}</h2></div>', unsafe_allow_html=True)
with m3:
    st.markdown(f'<div class="metric-card"><h3>Total Ratings</h3><h2>{total_ratings}</h2></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if page == "Home":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🍿 Featured Cinema Vibes</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="poster-strip">
        <div class="poster-box">
            <img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=600&q=80">
            <p>Epic Screenings</p>
        </div>
        <div class="poster-box">
            <img src="https://images.unsplash.com/photo-1542204165-65bf26472b9b?auto=format&fit=crop&w=600&q=80">
            <p>Blockbuster Energy</p>
        </div>
        <div class="poster-box">
            <img src="https://images.unsplash.com/photo-1518998053901-5348d3961a04?auto=format&fit=crop&w=600&q=80">
            <p>Cozy Movie Nights</p>
        </div>
        <div class="poster-box">
            <img src="https://images.unsplash.com/photo-1440404653325-ab127d49abc1?auto=format&fit=crop&w=600&q=80">
            <p>Dark Theatre Feels</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔥 Popular Right Now</div>', unsafe_allow_html=True)
    popular_movies = get_popular_movies(augmented_ratings, movies, top_n=50)
    popular_movies = popular_movies.merge(movies[["title", "genres"]], on="title", how="left")
    popular_movies = combine_filters(popular_movies, selected_genres, mood)

    if popular_movies.empty:
        st.info("No movies match the selected filters.")
    else:
        display_popular = popular_movies[["title", "genres", "avg_rating", "rating_count"]].head(10).copy()
        display_popular.columns = ["Title", "Genres", "Average Rating", "Number of Ratings"]
        st.dataframe(display_popular, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Personalized Picks":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">🎯 Personalized Picks for {switch_profiles[st.session_state.selected_user]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-note">Recommendations use the original dataset plus any watched movies you added for this viewer.</div>', unsafe_allow_html=True)

    if st.button("Recommend Movies For Me"):
        recommendations = recommend_movies_item_based(
            user_id=st.session_state.selected_user,
            user_movie_matrix=user_movie_matrix,
            movies_df=movies,
            ratings_df=augmented_ratings,
            top_n=100
        )

        recommendations = recommendations.merge(movies[["title", "genres"]], on="title", how="left")
        recommendations = combine_filters(recommendations, selected_genres, mood)
        recommendations = recommendations.head(num_recommendations)

        if recommendations.empty:
            st.warning("No recommendations matched your selected filters.")
        else:
            st.success("Your movie picks are ready.")
            display_recs = recommendations[["title", "genres", "score"]].copy()
            display_recs.columns = ["Title", "Genres", "Recommendation Score"]
            display_recs["Recommendation Score"] = display_recs["Recommendation Score"].round(2)
            st.dataframe(display_recs, use_container_width=True, hide_index=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📜 Watched Movies</div>', unsafe_allow_html=True)
    watched_movies = get_user_watched_movies(st.session_state.selected_user, augmented_ratings, movies)
    watched_movies = watched_movies.merge(movies[["title", "genres"]], on="title", how="left")
    watched_movies = combine_filters(watched_movies, selected_genres, mood)

    if watched_movies.empty:
        st.info("No watched movies found for the selected filters.")
    else:
        display_watched = watched_movies[["title", "genres", "rating"]].copy()
        display_watched.columns = ["Title", "Genres", "User Rating"]
        st.dataframe(display_watched, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Popular Now":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔥 Top Popular Movies</div>', unsafe_allow_html=True)

    if st.button("Show Popular Movies"):
        popular_movies = get_popular_movies(augmented_ratings, movies, top_n=100)
        popular_movies = popular_movies.merge(movies[["title", "genres"]], on="title", how="left")
        popular_movies = combine_filters(popular_movies, selected_genres, mood)
        popular_movies = popular_movies.head(num_recommendations)

        if popular_movies.empty:
            st.warning("No popular movies matched the selected filters.")
        else:
            st.success("Popular movies loaded.")
            display_popular = popular_movies[["title", "genres", "avg_rating", "rating_count"]].copy()
            display_popular.columns = ["Title", "Genres", "Average Rating", "Number of Ratings"]
            st.dataframe(display_popular, use_container_width=True, hide_index=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Add Watched Movie":
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">➕ Add Watched Movie for {switch_profiles[st.session_state.selected_user]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-note">Add a movie and rating. This will immediately influence recommendations for this profile during the current session.</div>', unsafe_allow_html=True)

    movie_titles = movies["title"].sort_values().tolist()
    chosen_title = st.selectbox("Select a movie", movie_titles)
    chosen_rating = st.slider("Your rating", 0.5, 5.0, 4.0, 0.5)

    if st.button("Add to Watch History"):
        chosen_movie_id = int(movies.loc[movies["title"] == chosen_title, "movieId"].iloc[0])
        add_custom_rating(st.session_state.selected_user, chosen_movie_id, chosen_rating)
        st.success(f'"{chosen_title}" added with rating {chosen_rating}.')

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Recently Added by You</div>', unsafe_allow_html=True)

    custom_df = st.session_state.custom_ratings
    custom_df = custom_df[custom_df["userId"] == st.session_state.selected_user]

    if custom_df.empty:
        st.info("No custom watched movies added yet.")
    else:
        custom_display = custom_df.merge(movies[["movieId", "title", "genres"]], on="movieId", how="left")
        custom_display = custom_display[["title", "genres", "rating"]].copy()
        custom_display.columns = ["Title", "Genres", "Your Rating"]
        st.dataframe(custom_display, use_container_width=True, hide_index=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("CineMatch • Netflix-inspired movie recommendation experience")
