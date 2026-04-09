# 🎬 CineMatch
### Netflix-Inspired Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Recommender-green)
![UI](https://img.shields.io/badge/UI-Netflix%20Inspired-black)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📌 Overview

CineMatch is a Netflix-inspired movie recommendation system built with **Python**, **Streamlit**, and **Machine Learning**.

It allows users to:

- sign in through a styled login page
- choose a viewer profile
- explore popular movies
- get personalized recommendations
- add watched movies with ratings
- improve recommendations using their updated watch history

The project combines a cinematic interface with a collaborative filtering recommendation engine to create an engaging movie discovery experience.

---

## ✨ Features

- 🔐 Login page UI
- 👤 Profile selection page
- 🎯 Personalized movie recommendations
- 🔥 Popular movie discovery
- 🎭 Mood-based movie filtering
- 🎬 Genre-based filtering
- ➕ Add watched movies and ratings
- 🧠 Recommendations influenced by watch history
- 🎨 Netflix-style red and black UI

---

## 🎥 Preview

### 🔐 Login Experience
![Login Demo](https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif)

### 👤 Profile Selection
![Profile Demo](https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif)

### 🎯 Recommendations
![Recommendation Demo](https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif)

### 🍿 Movie Browsing
![Movie Browsing Demo](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)

### 🎬 Cinematic Experience
![Cinema Demo](https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif)

---

## 🧠 How It Works

1. The system loads the MovieLens dataset.
2. It creates a **user-movie rating matrix**.
3. It uses **collaborative filtering** to find similar movie patterns.
4. Users can add watched movies and ratings.
5. The recommendation engine updates suggestions using this watch history.
6. Mood and genre filters refine the final recommendations.

---

## 🛠 Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **MovieLens Dataset**

---

## 📂 Project Structure

```bash
movie-recommendation-system/
│
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
    ├── movies.csv
    └── ratings.csv
