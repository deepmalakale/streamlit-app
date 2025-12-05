Streamlit App on EDA of Amazon Prime TV Shows and Movies    https://app-eda-amazon-prime.streamlit.app/
# 🎬 Amazon Prime Video — Exploratory Data Analysis (EDA)

This project performs **Exploratory Data Analysis (EDA)** on the **Amazon Prime Video dataset**, revealing key insights into its movies and TV shows catalog.  
It includes both **Python-based EDA** and an **interactive Streamlit web app** for visual exploration.

---

## 📊 **Project Overview**

The goal of this analysis is to uncover trends and patterns such as:
- Distribution of content across genres, ratings, and release years.
- Comparison of IMDb Scores, TMDb Popularity, and Runtime.
- Insights into audience preferences across movies and shows.
- Visualizations to support content strategy and recommendations.

The app provides **Univariate**, **Bivariate**, and **Multivariate** analyses through beautiful, interactive plots built using:
`Matplotlib`, `Seaborn`, and `Plotly`.

---

## 🧰 **Tech Stack**

| Component | Technology |
|------------|-------------|
| Language | Python |
| Framework | Streamlit |
| Visualization | Matplotlib, Seaborn, Plotly |
| Data Handling | Pandas, NumPy |
| Hosting | Streamlit Cloud |

---

## 🚀 **App Features**

✅ Welcome video introduction hosted on Google Drive  
✅ Interactive visualizations for each analysis type  
✅ Filterable and dynamic charts  
✅ Clean UI with descriptive text and insights  
✅ Works fully on Streamlit Cloud — no manual file uploads needed  

---

## 🎥 **Welcome Video**

A short video introduction is embedded directly in the app:

🔗 [Watch on Google Drive](https://drive.google.com/file/d/1OlRcOU6Pl8e7JqZIxvGdbufq7_CH9cZe/preview)

---

## 📂 **Dataset**

The dataset used in this project is also hosted on Google Drive for easy access:

🔗 [Amazon Prime Dataset (CSV)](https://drive.google.com/file/d/1FCsUhG-G0nUnQOfBuAb5mzXolv-UnCc4/view?usp=sharing)

Ensure that the dataset sharing settings are set to **“Anyone with the link → Viewer”**.

---

## ⚙️ **Installation**

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/amazon-prime-eda.git
cd amazon-prime-eda

2️⃣ Install dependencies
pip install -r requirements.txt


requirements.txt

streamlit>=1.35.0
pandas>=2.2.2
plotly>=5.22.0
numpy>=1.26.4
matplotlib>=3.8.4
seaborn>=0.13.2

▶️ Run the App Locally
streamlit run app.py


Then open the provided URL in your browser (usually http://localhost:8501).

☁️ Deploy on Streamlit Cloud

Go to Streamlit Cloud
.

Click “New App” → Connect to your GitHub repo.

Select this repository and the main branch.

Deploy — Streamlit Cloud will install dependencies automatically.

Make sure your dataset link (Google Drive) is shared publicly.

🧠 Insights & Learnings

Majority of Amazon Prime content consists of Movies over TV Shows.

IMDb Scores and TMDb Popularity exhibit moderate correlation.

Runtime distribution shows strong concentration around standard movie lengths (~90–120 mins).

Clear trends are visible across release decades, showing platform evolution.

💡 Future Improvements

Add genre-based recommendations using clustering.

Include sentiment analysis from movie/TV show reviews.

Expand dataset with regional content insights.

👩‍💻 Developed By

Deepmala Kale
📊 Data Analyst | Python | EDA | Visualization
🔗 Deployed App: Visit Streamlit App
