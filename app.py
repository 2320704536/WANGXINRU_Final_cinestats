%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title="🎬 CineStats — Film Analytics", layout="wide")

API_KEY = "75b267957348ed042d5c3d6f2d66b0a3"
BASE_URL = "https://api.themoviedb.org/3"

st.markdown("""
<style>
    .block-container { padding-top: 2rem; }
    .stMetric { background-color: #1a1a2e; border-radius: 10px; padding: 10px; }
    .director-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        border-left: 4px solid #e94560;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎬 CineStats — Film Data Analytics Hub")
st.caption("Real-time movie data powered by TMDb API")
st.markdown("---")

# ── API Functions ─────────────────────────────────────────
@st.cache_data(show_spinner=False)
def get_movies(endpoint, pages=10):
    movies = []
    for page in range(1, pages + 1):
        r = requests.get(f"{BASE_URL}/movie/{endpoint}", params={
            "api_key": API_KEY, "language": "en-US", "page": page
        })
        if r.status_code == 200:
            movies.extend(r.json().get("results", []))
    return movies

@st.cache_data(show_spinner=False)
def get_movie_credits(movie_id):
    r = requests.get(f"{BASE_URL}/movie/{movie_id}/credits", params={
        "api_key": API_KEY
    })
    if r.status_code == 200:
        return r.json()
    return {}

@st.cache_data(show_spinner=False)
def get_movie_details(movie_id):
    r = requests.get(f"{BASE_URL}/movie/{movie_id}", params={
        "api_key": API_KEY, "language": "en-US"
    })
    if r.status_code == 200:
        return r.json()
    return {}

@st.cache_data(show_spinner=False)
def search_movies(query):
    r = requests.get(f"{BASE_URL}/search/movie", params={
        "api_key": API_KEY, "language": "en-US", "query": query
    })
    if r.status_code == 200:
        return r.json().get("results", [])
    return []

@st.cache_data(show_spinner=False)
def get_genre_list():
    r = requests.get(f"{BASE_URL}/genre/movie/list", params={
        "api_key": API_KEY, "language": "en-US"
    })
    if r.status_code == 200:
        genres = r.json().get("genres", [])
        return {g["id"]: g["name"] for g in genres}
    return {}

# ── Load Data ─────────────────────────────────────────────
with st.spinner("🎬 Loading movie data from TMDb..."):
    popular  = get_movies("popular", 10)
    top_rated = get_movies("top_rated", 10)
    genre_map = get_genre_list()

def build_df(movies):
    rows = []
    for m in movies:
        genres = [genre_map.get(gid, "Unknown") for gid in m.get("genre_ids", [])]
        rows.append({
            "ID":           m["id"],
            "Title":        m.get("title", "N/A"),
            "Release Year": m.get("release_date", "N/A")[:4] if m.get("release_date") else "N/A",
            "Rating":       m.get("vote_average", 0),
            "Votes":        m.get("vote_count", 0),
            "Popularity":   round(m.get("popularity", 0), 1),
            "Genre":        genres[0] if genres else "Unknown",
            "All Genres":   ", ".join(genres),
            "Overview":     m.get("overview", ""),
            "Poster":       f"https://image.tmdb.org/t/p/w200{m['poster_path']}" if m.get("poster_path") else ""
        })
    return pd.DataFrame(rows)

df_popular = build_df(popular)
df_top     = build_df(top_rated)

# ── Tabs ──────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Analytics", "🎬 Director Analysis", "🔥 Popular", "⭐ Top Rated", "🔍 Search"
])

# ── Tab 1: Analytics ──────────────────────────────────────
with tab1:
    st.subheader("📊 Movie Analytics Dashboard")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("🎬 Popular Movies",  len(df_popular))
    m2.metric("⭐ Top Rated",       len(df_top))
    m3.metric("🎭 Genres",          len(genre_map))
    m4.metric("📈 Avg Rating (Top)", round(df_top["Rating"].mean(), 2))

    st.markdown("---")
    ch1, ch2 = st.columns(2)

    with ch1:
        st.markdown("**🎭 Genre Distribution (Popular)**")
        genre_count = df_popular["Genre"].value_counts().reset_index()
        genre_count.columns = ["Genre", "Count"]
        fig1 = px.pie(genre_count, names="Genre", values="Count", hole=0.3,
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig1, use_container_width=True)

    with ch2:
        st.markdown("**⭐ Top 10 Rated Movies**")
        top10 = df_top.sort_values("Rating", ascending=False).head(10)
        fig2 = px.bar(top10, x="Rating", y="Title", orientation="h",
                      color="Rating", color_continuous_scale="Viridis")
        st.plotly_chart(fig2, use_container_width=True)

    ch3, ch4 = st.columns(2)

    with ch3:
        st.markdown("**📅 Movies by Release Year (Top Rated)**")
        year_df = df_top[df_top["Release Year"] != "N/A"].copy()
        year_count = year_df["Release Year"].value_counts().sort_index().reset_index()
        year_count.columns = ["Year", "Count"]
        fig3 = px.line(year_count, x="Year", y="Count", markers=True,
                       color_discrete_sequence=["#e94560"])
        st.plotly_chart(fig3, use_container_width=True)

    with ch4:
        st.markdown("**🎭 Avg Rating by Genre**")
        avg_genre = df_top.groupby("Genre")["Rating"].mean().round(2).reset_index()
        avg_genre.columns = ["Genre", "Avg Rating"]
        avg_genre = avg_genre.sort_values("Avg Rating", ascending=False)
        fig4 = px.bar(avg_genre, x="Genre", y="Avg Rating",
                      color="Avg Rating", color_continuous_scale="RdYlGn",
                      range_y=[0, 10])
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("**📈 Rating vs Popularity**")
    fig5 = px.scatter(df_popular, x="Popularity", y="Rating",
                      hover_name="Title", color="Genre", size="Votes",
                      color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig5, use_container_width=True)

# ── Tab 2: Director Analysis ──────────────────────────────
with tab2:
    st.subheader("🎬 Director Analysis")
    st.info("Fetching director data from TMDb — this may take a moment the first time!")

    @st.cache_data(show_spinner=False)
    def build_director_data(movie_ids):
        director_stats = {}
        progress = st.progress(0)
        for i, mid in enumerate(movie_ids):
            credits = get_movie_credits(mid)
            details = get_movie_details(mid)
            crew = credits.get("crew", [])
            for person in crew:
                if person.get("job") == "Director":
                    name = person["name"]
                    rating = details.get("vote_average", 0)
                    revenue = details.get("revenue", 0)
                    title = details.get("title", "Unknown")
                    year = details.get("release_date", "")[:4]
                    if name not in director_stats:
                        director_stats[name] = {
                            "Movies": [],
                            "Ratings": [],
                            "Revenue": [],
                            "Photo": f"https://image.tmdb.org/t/p/w200{person.get('profile_path')}" if person.get("profile_path") else ""
                        }
                    director_stats[name]["Movies"].append(f"{title} ({year})")
                    director_stats[name]["Ratings"].append(rating)
                    director_stats[name]["Revenue"].append(revenue)
            progress.progress((i + 1) / len(movie_ids))
        progress.empty()
        return director_stats

    # 只用Top Rated前50部做导演分析（速度更快）
    top50_ids = df_top.sort_values("Rating", ascending=False).head(50)["ID"].tolist()
    director_data = build_director_data(tuple(top50_ids))

    # 整理成DataFrame
    dir_rows = []
    for name, data in director_data.items():
        avg_rating  = round(sum(data["Ratings"]) / len(data["Ratings"]), 2)
        total_rev   = sum(data["Revenue"])
        movie_count = len(data["Movies"])
        best_movie  = data["Movies"][data["Ratings"].index(max(data["Ratings"]))]
        dir_rows.append({
            "Director":      name,
            "Movies Count":  movie_count,
            "Avg Rating":    avg_rating,
            "Best Movie":    best_movie,
            "Total Revenue": total_rev,
            "Photo":         data["Photo"]
        })

    df_dir = pd.DataFrame(dir_rows).sort_values("Avg Rating", ascending=False)

    # Metrics
    d1, d2, d3 = st.columns(3)
    d1.metric("🎬 Directors Analyzed", len(df_dir))
    d2.metric("⭐ Highest Avg Rating", df_dir["Avg Rating"].max())
    d3.metric("🏆 Most Prolific", df_dir.sort_values("Movies Count", ascending=False).iloc[0]["Director"])

    st.markdown("---")
    dc1, dc2 = st.columns(2)

    with dc1:
        st.markdown("**🏆 Top 15 Directors by Avg Rating**")
        top_dir = df_dir.head(15)
        fig_d1 = px.bar(top_dir, x="Avg Rating", y="Director",
                        orientation="h", color="Avg Rating",
                        color_continuous_scale="Viridis",
                        range_x=[0, 10])
        st.plotly_chart(fig_d1, use_container_width=True)

    with dc2:
        st.markdown("**🎬 Directors by Number of Movies**")
        prolific = df_dir.sort_values("Movies Count", ascending=False).head(15)
        fig_d2 = px.bar(prolific, x="Movies Count", y="Director",
                        orientation="h", color="Movies Count",
                        color_continuous_scale="Blues")
        st.plotly_chart(fig_d2, use_container_width=True)

    st.markdown("**💰 Avg Rating vs Total Revenue**")
    df_dir_plot = df_dir[df_dir["Total Revenue"] > 0]
    fig_d3 = px.scatter(df_dir_plot, x="Avg Rating", y="Total Revenue",
                        hover_name="Director", size="Movies Count",
                        color="Avg Rating", color_continuous_scale="RdYlGn",
                        labels={"Total Revenue": "Total Revenue (USD)"})
    st.plotly_chart(fig_d3, use_container_width=True)

    st.markdown("---")
    st.subheader("🔍 Director Detail Search")
    dir_search = st.text_input("Search a director name")
    if dir_search:
        result = df_dir[df_dir["Director"].str.contains(dir_search, case=False)]
        if len(result) > 0:
            for _, row in result.iterrows():
                with st.expander(f"🎬 {row['Director']} — ⭐ {row['Avg Rating']} avg"):
                    c1, c2 = st.columns([1, 3])
                    with c1:
                        if row["Photo"]:
                            st.image(row["Photo"], width=120)
                    with c2:
                        st.write(f"**Movies in Dataset:** {row['Movies Count']}")
                        st.write(f"**Average Rating:** {row['Avg Rating']}")
                        st.write(f"**Best Rated Work:** {row['Best Movie']}")
                        if row["Total Revenue"] > 0:
                            st.write(f"**Total Revenue:** ${row['Total Revenue']:,}")
        else:
            st.warning("Director not found in current dataset.")

    st.markdown("---")
    csv_dir = df_dir.drop(columns=["Photo"]).to_csv(index=False).encode("utf-8")
    st.download_button("📤 Export Director Data as CSV", csv_dir,
                       "cinestats_directors.csv", "text/csv")

# ── Tab 3: Popular ────────────────────────────────────────
with tab3:
    st.subheader("🔥 Popular Movies Right Now")

    f1, f2 = st.columns(2)
    with f1:
        genre_options = ["All"] + sorted(df_popular["Genre"].unique())
        genre_sel = st.selectbox("Filter by Genre", genre_options)
    with f2:
        min_rating = st.slider("Minimum Rating", 0.0, 10.0, 5.0, 0.1)

    df_p = df_popular.copy()
    if genre_sel != "All":
        df_p = df_p[df_p["Genre"] == genre_sel]
    df_p = df_p[df_p["Rating"] >= min_rating]
    df_p = df_p.sort_values("Popularity", ascending=False).reset_index(drop=True)

    for _, row in df_p.head(20).iterrows():
        with st.expander(f"🎬 {row['Title']} ({row['Release Year']}) — ⭐ {row['Rating']}"):
            c1, c2 = st.columns([1, 4])
            with c1:
                if row["Poster"]:
                    st.image(row["Poster"], width=100)
            with c2:
                st.write(f"**Genre:** {row['All Genres']}")
                st.write(f"**Popularity:** {row['Popularity']}")
                st.write(f"**Votes:** {row['Votes']:,}")
                if row["Overview"]:
                    st.caption(row["Overview"][:200] + "...")

# ── Tab 4: Top Rated ──────────────────────────────────────
with tab4:
    st.subheader("⭐ Top Rated Movies of All Time")

    year_options = ["All"] + sorted(df_top["Release Year"].unique(), reverse=True)
    year_sel = st.selectbox("Filter by Year", year_options)

    df_t = df_top.copy()
    if year_sel != "All":
        df_t = df_t[df_t["Release Year"] == year_sel]
    df_t = df_t.sort_values("Rating", ascending=False).reset_index(drop=True)

    for _, row in df_t.head(20).iterrows():
        with st.expander(f"⭐ {row['Title']} ({row['Release Year']}) — {row['Rating']}/10"):
            c1, c2 = st.columns([1, 4])
            with c1:
                if row["Poster"]:
                    st.image(row["Poster"], width=100)
            with c2:
                st.write(f"**Genre:** {row['All Genres']}")
                st.write(f"**Votes:** {row['Votes']:,}")
                if row["Overview"]:
                    st.caption(row["Overview"][:200] + "...")

# ── Tab 5: Search ─────────────────────────────────────────
with tab5:
    st.subheader("🔍 Search Any Movie")
    query = st.text_input("Enter a movie title", placeholder="e.g. Inception, Parasite...")

    if query:
        with st.spinner("Searching..."):
            results = search_movies(query)
        if results:
            df_s = build_df(results)
            st.success(f"Found {len(df_s)} results for '{query}'")
            for _, row in df_s.head(10).iterrows():
                with st.expander(f"🎬 {row['Title']} ({row['Release Year']}) — ⭐ {row['Rating']}"):
                    c1, c2 = st.columns([1, 4])
                    with c1:
                        if row["Poster"]:
                            st.image(row["Poster"], width=100)
                    with c2:
                        st.write(f"**Genre:** {row['All Genres']}")
                        st.write(f"**Votes:** {row['Votes']:,}")
                        if row["Overview"]:
                            st.caption(row["Overview"][:200] + "...")
        else:
            st.warning("No results found. Try another title!")

# ── Export ────────────────────────────────────────────────
st.markdown("---")
csv = df_top.to_csv(index=False).encode("utf-8")
st.download_button("📤 Export Top Rated as CSV", csv,
                   "cinestats_top_rated.csv", "text/csv")
