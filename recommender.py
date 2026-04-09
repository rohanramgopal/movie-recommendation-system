import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    movies = pd.read_csv("data/movies.csv")
    ratings = pd.read_csv("data/ratings.csv")
    return movies, ratings


def create_user_movie_matrix(ratings_df):
    return ratings_df.pivot_table(
        index="userId",
        columns="movieId",
        values="rating"
    )


def get_user_watched_movies(user_id, ratings_df, movies_df):
    user_ratings = ratings_df[ratings_df["userId"] == user_id]
    watched = user_ratings.merge(movies_df, on="movieId")
    watched = watched.sort_values(by="rating", ascending=False)
    return watched[["movieId", "title", "rating"]]


def get_popular_movies(ratings_df, movies_df, top_n=10, min_ratings=20):
    movie_stats = ratings_df.groupby("movieId").agg(
        avg_rating=("rating", "mean"),
        rating_count=("rating", "count")
    ).reset_index()

    movie_stats = movie_stats[movie_stats["rating_count"] >= min_ratings]
    popular = movie_stats.merge(movies_df, on="movieId")
    popular = popular.sort_values(
        by=["avg_rating", "rating_count"],
        ascending=[False, False]
    )

    return popular[["movieId", "title", "avg_rating", "rating_count"]].head(top_n)


def recommend_movies_item_based(user_id, user_movie_matrix, movies_df, ratings_df, top_n=10):
    if user_id not in user_movie_matrix.index:
        return pd.DataFrame(columns=["movieId", "title", "score"])

    matrix_filled = user_movie_matrix.fillna(0)

    item_similarity = cosine_similarity(matrix_filled.T)
    item_similarity_df = pd.DataFrame(
        item_similarity,
        index=matrix_filled.columns,
        columns=matrix_filled.columns
    )

    user_ratings = user_movie_matrix.loc[user_id].dropna()

    if user_ratings.empty:
        return pd.DataFrame(columns=["movieId", "title", "score"])

    recommendation_scores = {}

    for movie_id, rating in user_ratings.items():
        similar_movies = item_similarity_df[movie_id]

        for sim_movie_id, similarity_score in similar_movies.items():
            if sim_movie_id not in user_ratings.index and sim_movie_id != movie_id:
                recommendation_scores[sim_movie_id] = (
                    recommendation_scores.get(sim_movie_id, 0) + similarity_score * rating
                )

    if not recommendation_scores:
        return pd.DataFrame(columns=["movieId", "title", "score"])

    recommendations = pd.DataFrame(
        recommendation_scores.items(),
        columns=["movieId", "score"]
    )

    recommendations = recommendations.merge(movies_df, on="movieId")
    recommendations = recommendations.sort_values(by="score", ascending=False)

    return recommendations[["movieId", "title", "score"]].head(top_n)
