# 🎬 CineStats — Film Data Analytics Hub

> A real-time interactive movie analytics dashboard powered by the TMDb API.  
> Built for Arts and Big Data (SOA2005-01) | Sungkyunkwan University | 2026 Spring

---

## 📌 Project Overview

CineStats is a web-based data dashboard that collects, analyzes, and visualizes real-time movie data from **The Movie Database (TMDb)**. Instead of static datasets, this app pulls live data every session — giving users up-to-date insights into film trends, director performance, and genre popularity.

The goal of this project is to explore how **big data and the arts intersect** — using real cinema data to uncover patterns in what makes a film successful, which directors consistently deliver quality, and how audience tastes have shifted over the decades.

---

## 🖥️ Live Demo

> Run the app locally using the instructions below.  
> Built and tested on Google Colab + Streamlit.

---

## ✨ Features

### 📊 Analytics Dashboard
- Genre distribution pie chart (Popular Movies)
- Top 10 highest rated movies bar chart
- Movies released per year — trend line chart
- Average rating by genre
- Rating vs Popularity scatter plot

### 🎬 Director Analysis ⭐ (Main Feature)
- Top 15 directors ranked by average rating
- Most prolific directors by number of films
- Revenue vs Rating scatter plot per director
- Director profile photo + best movie display
- Search any director by name
- Export director data as CSV

### 🔥 Popular Movies
- Filter by genre
- Filter by minimum rating
- Movie poster, overview, vote count display

### ⭐ Top Rated Movies
- Filter by release year
- Sorted by rating
- Full movie details with poster

### 🔍 Search
- Search any movie title in real time
- Pulls live results from TMDb API

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Plotly](https://plotly.com) | Interactive data visualizations |
| [TMDb API](https://www.themoviedb.org/documentation/api) | Real-time movie data source |
| [Pandas](https://pandas.pydata.org) | Data processing |
| [Google Colab](https://colab.research.google.com) | Development & deployment environment |

---

## 🚀 How to Run

### Option 1: Google Colab (Recommended)

**Step 1** — Install dependencies
```python
!pip install streamlit plotly requests -q
!wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 \
  -O /usr/local/bin/cloudflared
!chmod +x /usr/local/bin/cloudflared
```

**Step 2** — Write app.py
```python
%%writefile app.py
# paste the full app.py code here
```

**Step 3** — Launch the app
```python
import subprocess, time, re
subprocess.Popen(["streamlit", "run", "app.py",
    "--server.port", "8501",
    "--server.headless", "true",
    "--server.enableCORS", "false",
    "--server.enableXsrfProtection", "false"])
time.sleep(3)
proc = subprocess.Popen(
    ["cloudflared", "tunnel", "--url", "http://localhost:8501"],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
time.sleep(5)
for line in proc.stderr:
    if "trycloudflare.com" in line:
        url = re.search(r'https://[^\s]+trycloudflare\.com', line)
        if url:
            print(f"🎉 Your app: {url.group()}")
            break
```

### Option 2: Local Machine

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/cinestats.git
cd cinestats

# Install dependencies
pip install streamlit plotly requests pandas

# Run the app
streamlit run app.py
```

---

## 📁 Project Structure
cinestats/
│
├── app.py          # Main Streamlit application
└── README.md       # Project documentation
---

## 🗂️ Data Source

This project uses the **TMDb API (v3)** which provides:
- Movie metadata (title, genre, release date, overview)
- Ratings and vote counts from millions of users worldwide
- Cast and crew information including directors
- Box office revenue data
- Movie poster images

> Data is fetched live on each session — no static dataset needed.

---

## 📈 Key Insights This Dashboard Can Answer

- Which film genres are most popular right now?
- Which directors have the highest average ratings?
- Is there a correlation between a film's popularity and its rating?
- Which decades produced the most critically acclaimed films?
- How does box office revenue relate to critical reception?

---

## 🗓️ Development Timeline

| Week | Milestone |
|------|-----------|
| W09 | Built initial movie collection app |
| W10 | Switched to TMDb API, added director analysis |
| W11–W13 | Polished UI, added charts, uploaded to GitHub |
| W14 | Final refinements based on feedback |
| W15–W16 | Presentation & evaluation |

---

## 👤 Author

| | |
|--|--|
| **Name** | Your Name |
| **Student ID** | Your Student ID |
| **Course** | Arts and Big Data (SOA2005-01) |
| **Professor** | Prof. Jahwan Koo |
| **University** | Sungkyunkwan University |
| **Semester** | 2026 Spring |

---

## 📜 License

This project is for educational purposes only.  
Movie data provided by [TMDb](https://www.themoviedb.org).  
*This product uses the TMDb API but is not endorsed or certified by TMDb.*
