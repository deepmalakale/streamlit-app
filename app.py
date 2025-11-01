import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np
import io
import requests

# --------------------------------------------------------
# BASIC SETUP
# --------------------------------------------------------
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
sns.set_theme(style="whitegrid")

st.set_page_config(page_title="Data Analysis App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page:",
    ["Welcome", "Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis"],
    key="navigation"
)

# --------------------------------------------------------
# CONSTANT LINKS (YOUR GOOGLE DRIVE FILES)
# --------------------------------------------------------

# 🎥 Video link (Google Drive preview link)
VIDEO_EMBED_LINK = "https://drive.google.com/file/d/1OlRcOU6Pl8e7JqZIxvGdbufq7_CH9cZe/preview"

# 📊 CSV link (Google Drive share link)
CSV_SHARE_LINK = "https://drive.google.com/file/d/1FCsUhG-G0nUnQOfBuAb5mzXolv-UnCc4/view?usp=sharing"

# Convert shared link to direct download link
CSV_FILE_ID = CSV_SHARE_LINK.split("/d/")[1].split("/")[0]
CSV_DIRECT_LINK = f"https://drive.google.com/uc?export=download&id={CSV_FILE_ID}"

# --------------------------------------------------------
# FUNCTION TO LOAD DATA FROM GOOGLE DRIVE
# --------------------------------------------------------
@st.cache_data
def load_data_from_drive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return pd.read_csv(io.StringIO(response.text))
        else:
            st.error("⚠️ Failed to load dataset from Google Drive. Please check the sharing permissions.")
            return None
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        return None

# --------------------------------------------------------
# WELCOME PAGE
# --------------------------------------------------------
if page == "Welcome":
    st.title("🎬 Welcome to the Data Analysis Application 🎉")

    st.write(
        """
        This application is designed for **dynamic data visualization and analysis** using a dataset 
        hosted on **Google Drive** — no upload needed!

        ### 📊 What you can explore:
        - **Univariate Analysis:** Single-variable exploration  
        - **Bivariate Analysis:** Relationships between two variables  
        - **Multivariate Analysis:** Correlations across multiple dimensions  

        ### ⚙️ Features:
        - Automatic data loading from Google Drive  
        - Interactive visualizations with Seaborn & Matplotlib  
        - Instant, browser-based analysis  
        """
    )

    # 🎥 Video Section
    st.markdown("---")
    st.header("🎥 Exploratory Data Analysis Video")

    drive_video_embed = f"""
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <iframe src="{VIDEO_EMBED_LINK}" width="900" height="500" allow="autoplay"></iframe>
    </div>
    """
    st.markdown(drive_video_embed, unsafe_allow_html=True)

    # 📊 Dataset Section
    st.markdown("---")
    st.header("📂 Dataset Used for Analysis")

    st.success("✅ The dataset is automatically loaded from Google Drive (no upload needed).")

    st.markdown(f"[Click here to open dataset in Google Drive]({CSV_SHARE_LINK})")

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:gray;'>Developed for Amazon Prime Video EDA Project 📊</p>",
        unsafe_allow_html=True
    )

# --------------------------------------------------------
# OTHER PAGES (Auto-load CSV)
# --------------------------------------------------------
else:
    st.sidebar.info("Loading dataset from Google Drive...")
    data = load_data_from_drive(CSV_DIRECT_LINK)

    if data is None:
        st.stop()
    else:
        st.sidebar.success("✅ Dataset Loaded Successfully from Google Drive!")

    numeric_columns = data.select_dtypes(include="number").columns.tolist()
    categorical_columns = data.select_dtypes(include="object").columns.tolist()

    def display_plot(fig):
        st.pyplot(fig)

# --------------------------------------------------------
# UNIVARIATE ANALYSIS
# --------------------------------------------------------
    if page == "Univariate Analysis":
        st.title("📊 Univariate Analysis")
        st.header("Explore Single-Variable Trends")

        fig, axes = plt.subplots(2, 2, figsize=(22, 13))

        hist_col = st.selectbox("Select column for Histogram:", numeric_columns, key="hist")
        sns.histplot(data[hist_col], kde=True, ax=axes[0, 0])
        axes[0, 0].set_title(f"Histogram of {hist_col}", fontsize=25, color="red", weight="bold")

        if categorical_columns:
            count_col = st.selectbox("Select column for Countplot:", categorical_columns, key="countplot")
            sns.countplot(data=data, x=count_col, ax=axes[0, 1])
            axes[0, 1].set_title(f"Countplot of {count_col}", fontsize=25, color="red", weight="bold")

        if categorical_columns:
            pie_col = st.selectbox("Select column for Pie Chart:", categorical_columns, key="pie")
            num_categories = st.slider("Number of top categories for Pie Chart:", 3, 10, 5)
            top_categories = data[pie_col].value_counts().head(num_categories)
            top_categories.plot.pie(autopct='%1.1f%%', ax=axes[1, 0], textprops={'fontsize': 20})
            axes[1, 0].set_title(f"Pie Chart of {pie_col}", fontsize=25, color="red", weight="bold")

        box_col = st.selectbox("Select column for Boxplot:", numeric_columns, key="box")
        sns.boxplot(data=data, x=box_col, ax=axes[1, 1])
        axes[1, 1].set_title(f"Boxplot of {box_col}", fontsize=25, color="red", weight="bold")

        plt.tight_layout()
        display_plot(fig)

# --------------------------------------------------------
# BIVARIATE ANALYSIS
# --------------------------------------------------------
    elif page == "Bivariate Analysis":
        st.title("🔗 Bivariate Analysis")
        st.header("Explore Relationships Between Two Variables")

        fig, axes = plt.subplots(2, 2, figsize=(22, 13))

        line_x = st.selectbox("X for Line Plot:", numeric_columns, key="line_x")
        line_y = st.selectbox("Y for Line Plot:", numeric_columns, key="line_y")
        sns.lineplot(data=data, x=line_x, y=line_y, ax=axes[0, 0])
        axes[0, 0].set_title(f"Line Plot: {line_x} vs {line_y}", fontsize=25, color="red", weight="bold")

        scatter_x = st.selectbox("X for Scatter Plot:", numeric_columns, key="scatter_x")
        scatter_y = st.selectbox("Y for Scatter Plot:", numeric_columns, key="scatter_y")
        sns.scatterplot(data=data, x=scatter_x, y=scatter_y, ax=axes[0, 1])
        axes[0, 1].set_title(f"Scatter Plot: {scatter_x} vs {scatter_y}", fontsize=25, color="red", weight="bold")

        if categorical_columns:
            bar_x = st.selectbox("X for Bar Plot (Categorical):", categorical_columns, key="bar_x")
            bar_y = st.selectbox("Y for Bar Plot (Numeric):", numeric_columns, key="bar_y")
            sns.barplot(data=data, x=bar_x, y=bar_y, ax=axes[1, 0])
            axes[1, 0].set_title(f"Bar Plot: {bar_x} vs {bar_y}", fontsize=25, color="red", weight="bold")

        if categorical_columns:
            box_x = st.selectbox("X for Boxplot (Categorical):", categorical_columns, key="box_x_bi")
            box_y = st.selectbox("Y for Boxplot (Numeric):", numeric_columns, key="box_y_bi")
            sns.boxplot(data=data, x=box_x, y=box_y, ax=axes[1, 1])
            axes[1, 1].set_title(f"Boxplot: {box_x} vs {box_y}", fontsize=25, color="red", weight="bold")

        plt.tight_layout()
        display_plot(fig)

# --------------------------------------------------------
# MULTIVARIATE ANALYSIS
# --------------------------------------------------------
    elif page == "Multivariate Analysis":
        st.title("🌐 Multivariate Analysis")
        st.header("Discover Patterns Across Multiple Variables")

        st.subheader("Pairplot")
        if numeric_columns:
            pairplot_cols = st.multiselect("Select columns for Pairplot:", numeric_columns,
                                           default=numeric_columns[:min(3, len(numeric_columns))])
            if pairplot_cols:
                pairplot_fig = sns.pairplot(data[pairplot_cols])
                st.pyplot(pairplot_fig.fig)
            else:
                st.warning("Please select at least one column for the Pairplot.")
        else:
            st.error("No numeric columns available for Pairplot.")

        st.subheader("Heatmap")
        if numeric_columns:
            fig, ax = plt.subplots(figsize=(20, 15))
            corr = data[numeric_columns].corr()
            mask = np.triu(np.ones_like(corr, dtype=bool))
            sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm", ax=ax)
            ax.set_title("Correlation Heatmap", fontsize=25, color="red", weight="bold")
            display_plot(fig)
        else:
            st.error("No numeric columns available for Heatmap.")
