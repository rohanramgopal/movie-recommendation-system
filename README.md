# 🎬 CineMatch  
### Netflix-Inspired Movie Recommendation System  

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Recommender-green)
![UI](https://img.shields.io/badge/UI-Netflix%20Inspired-black)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🎥 Preview  

![Cinema Experience](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)

---

## 📌 Overview  

CineMatch is a **Netflix-inspired movie recommendation system** built using **Python, Streamlit, and Machine Learning**.

It allows users to:

- 🔐 Sign in through a styled login page  
- 👤 Choose a viewer profile  
- 🎯 Get personalized movie recommendations  
- 🔥 Explore trending/popular movies  
- ⭐ Add watched movies and ratings  
- 🧠 Improve recommendations using watch history  

---

## ✨ Features  

- 🔐 Login page UI  
- 👤 Profile selection (like Netflix)  
- 🎯 Personalized recommendations  
- 🔥 Popular movie discovery  
- 🎭 Mood-based filtering  
- 🎬 Genre filtering  
- ➕ Add watched movies + ratings  
- ⚡ Real-time recommendation updates  
- 🎨 Netflix-style UI  

---

## 🧠 How It Works  

1. Load MovieLens dataset  
2. Create **user-movie matrix**  
3. Apply **collaborative filtering**  
4. Generate recommendations based on:
   - user history  
   - similar movies  
5. Apply filters (mood + genre)  
6. Display results in UI  

---

## 🛠 Tech Stack  

- **Python**  
- **Pandas / NumPy**  
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

---
## ⚙️ Installation
- git clone git@github.com:rohanramgopal/movie-recommendation-system.git
- cd movie-recommendation-system
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

---

▶️ Run the App
streamlit run app.py

---

## 🚀 Future Enhancements
- 🎬 Movie posters (TMDb API)
- 🔍 Search functionality
- 🧠 Hybrid recommendation system
- ☁️ Cloud deployment
- 👥 Real authentication system
- 🎞 Netflix-style card UI
- 💡 Why This Project Stands Out

This is not just a recommender system — it is a product-style project combining:

machine learning
UI/UX design
real-time interaction
user-driven personalization

---

## 👨‍💻 Author

**Rohan Ramgopal
