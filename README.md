# 🎬 CineStats — Film Data Analytics Hub

A real-time movie data dashboard built with **Streamlit**, **Plotly**, and the **TMDb API**.  
Created by **WANG XINRU** for **Arts and Big Data** | Sungkyunkwan University | 2026 Spring

---

## 📌 Project Overview

**CineStats** is an interactive film data analytics web app that explores movie information through real-time data and visual charts.

The app collects movie data from **The Movie Database (TMDb)** and presents it in a clear dashboard format. Users can explore popular movies, top-rated films, genre patterns, release year trends, director performance, and individual movie search results.

This project connects film culture with data visualization. Instead of showing movie information only as a list, CineStats helps users understand patterns in ratings, popularity, genres, and directors through interactive charts and filters.

---

## 📊 Features

- **Analytics Dashboard** — Genre distribution, rating trends, release year analysis, and rating vs popularity visualization
- **Director Analysis** — Top directors by average rating, movie count, and revenue vs rating comparison
- **Popular Movies** — Browse currently popular films and filter by genre or minimum rating
- **Top Rated Movies** — View all-time best-rated films with posters, genres, votes, and summaries
- **Movie Search** — Search any movie by title and view rating, genre, poster, votes, and overview
- **CSV Export** — Download movie and director data for further analysis

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| **Streamlit** | Web app framework |
| **Plotly** | Interactive charts and data visualization |
| **Pandas** | Data processing and table management |
| **TMDb API** | Real-time movie data source |
| **Google Colab** | Development and testing environment |
| **Python** | Main programming language |

---

## 📊 Data Source

The movie data used in this project comes from **The Movie Database (TMDb) API**.

The app retrieves information such as movie titles, release years, ratings, vote counts, popularity scores, genres, posters, overviews, director information, and revenue data.

---

## 🚀 How to Run

Install the required libraries and run the Streamlit app:

```bash
pip install streamlit pandas plotly requests
streamlit run app.py
```

Then open the local URL shown in the terminal to view the app.

---

## 📦 Requirements

Create a `requirements.txt` file with the following libraries:

```txt
streamlit
pandas
plotly
requests
```

---

## 📸 Screenshot

<img width="1466" height="567" alt="截屏2026-05-06 下午12 56 25" src="https://github.com/user-attachments/assets/cfed9b55-1802-46fa-82a6-4653ecfd51da" />

---


## 🎯 Project Purpose

This project was created for the **Arts and Big Data** course.

The main purpose of CineStats is to show how data can be used to understand film and media culture. By combining real-time movie data with interactive visualizations, the app allows users to explore relationships between popularity, ratings, genres, release years, and director performance.

Through this project, I wanted to demonstrate that data analysis is not only useful in business or science, but can also be applied to creative fields such as film. CineStats presents film data in a more accessible and visual way, making it easier for users to discover patterns behind movies and audience preferences.

---

## 🙋‍♀️ Author

**WANG XINRU**

Created as a Streamlit web app project for **Arts and Big Data **.

**CineStats — Film Data Analytics Hub**  
A project that connects film, data, and visual storytelling.

---

## 🙏 Acknowledgement

This project uses movie data provided by TMDb API.  
This project is created for the Arts and Big Data final project.
