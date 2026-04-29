# 🎬 CineStats — Film Data Analytics Hub

> A real-time movie data dashboard built with **Streamlit**, **Plotly**, and the **TMDb API**.  
> Created for **Arts and Big Data (SOA2005-01)** | Sungkyunkwan University | 2026 Spring

---

## 📌 Project Overview

**CineStats** is an interactive film data analytics web app that helps users explore movie trends through real-time data.

The app collects movie information from the **TMDb API** and presents it through charts, filters, director analysis, movie posters, and search tools.  
It is designed as a personal **film data hub**, combining movie culture with data visualization.

Instead of simply listing films, CineStats turns movie information into a visual dashboard where users can compare popularity, ratings, genres, release years, and director performance.

---

## 📊 Features

- **Analytics Dashboard** — Genre distribution, rating trends, release year analysis, and rating vs popularity visualization  
- **Director Analysis** — Top directors by average rating, movie count, and revenue comparison  
- **Popular Movies** — Browse currently popular films and filter by genre or minimum rating  
- **Top Rated Movies** — View all-time top-rated films with posters, genres, votes, and summaries  
- **Movie Search** — Search any movie by title and display detailed results  
- **CSV Export** — Download movie and director data for further analysis  

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| **Streamlit** | Web app framework |
| **Plotly** | Interactive charts and data visualization |
| **Pandas** | Data cleaning and table management |
| **TMDb API** | Real-time movie data source |
| **Google Colab** | Development and testing environment |
| **Python** | Main programming language |

---

## 🧩 Main Sections

### 📊 Analytics

The analytics page shows an overview of the movie dataset using key metrics and visual charts.

It includes:

- Number of popular movies
- Number of top-rated movies
- Number of genres
- Average rating of top-rated films
- Genre distribution pie chart
- Top 10 rated movie bar chart
- Movies by release year line chart
- Average rating by genre chart
- Rating vs popularity scatter plot

---

### 🎬 Director Analysis

The director analysis section focuses on directors from the top-rated movie dataset.

It includes:

- Number of directors analyzed
- Highest average rating
- Most prolific director
- Top directors by average rating
- Directors by number of movies
- Rating vs total revenue comparison
- Search function for director details
- CSV export for director data

---

### 🔥 Popular Movies

This section displays currently popular movies from TMDb.

Users can:

- Filter movies by genre
- Set a minimum rating
- View movie posters
- Read short overviews
- Check popularity scores and vote counts

---

### ⭐ Top Rated Movies

This section displays highly rated movies of all time.

Users can:

- Filter movies by release year
- View movie posters
- Check ratings and vote counts
- Read movie summaries

---

### 🔍 Movie Search

The search page allows users to search for any movie title.

For each result, the app displays:

- Movie title
- Release year
- Rating
- Genre
- Vote count
- Poster image
- Overview

---

## 📊 Data Source

The data used in this project comes from **The Movie Database (TMDb) API**.

The app retrieves:

- Movie titles
- Release years
- Ratings
- Vote counts
- Popularity scores
- Genres
- Posters
- Movie overviews
- Director information
- Revenue data

---

## 🚀 How to Run

### 1. Install required libraries

```bash
pip install streamlit pandas plotly requests
