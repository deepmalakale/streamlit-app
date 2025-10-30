import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings
import numpy as np

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
sns.set_theme(style="whitegrid")

# Set wide layout
st.set_page_config(page_title="Data Analysis App", layout="wide")

# ----------------------------
# Path for uploaded CSV
# ----------------------------
app_data_folder = "app_data"
os.makedirs(app_data_folder, exist_ok=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page:",
    ["Welcome", "Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis"],
    key="navigation"
)

# ----------------------------------------------------------------
# WELCOME PAGE
# ----------------------------------------------------------------
if page == "Welcome":
    st.title("Welcome to the Data Analysis Application 🎉")

    st.write(
        """
        This application is designed for dynamic data visualization and analysis using your uploaded dataset. It supports:

        - **Univariate Analysis:** Single-variable exploration.
        - **Bivariate Analysis:** Explore relationships between two variables.
        - **Multivariate Analysis:** Advanced insights involving multiple variables.

        ### Features include:
        - Interactive visualizations.
        - Seamless data upload and processing.
        - Advanced plots with custom options.

        Navigate through the sidebar options to begin your journey! 📊
        """
    )

    # ---------------------------
    # CSV Download Link
    # ---------------------------
    st.markdown("---")
    st.header("📥 Download Sample Dataset")

    # Check for CSV files in the app_data folder
    csv_files = [f for f in os.listdir(app_data_folder) if f.lower().endswith(".csv")]

    if csv_files:
        csv_path = os.path.join(app_data_folder, csv_files[0])  # take the first CSV
        with open(csv_path, "rb") as f:
            csv_bytes = f.read()
        st.download_button(
            label="Download CSV",
            data=csv_bytes,
            file_name=csv_files[0],
            mime='text/csv'
        )
    else:
        st.info("No CSV file found in the `app_data/` folder. Upload a CSV to enable download.")

    st.markdown("---")
    st.header("🎥 Exploratory Data Analysis Video on the sample Dataset")

    # Folder where videos are stored
    video_folder = "videos"
    os.makedirs(video_folder, exist_ok=True)

    # Get all video files in the folder
    video_files = [
        f for f in os.listdir(video_folder)
        if f.lower().endswith((".mp4", ".mov", ".avi", ".mkv"))
    ]

    if video_files:
        # Apply styling for YouTube-like frame
        st.markdown(
            """
            <style>
            .stVideo > video {
                width: 1280px !important;
                height: 720px !important;
                display: block;
                margin-left: auto;
                margin-right: auto;
                border-radius: 12px;
                box-shadow: 0px 4px 25px rgba(0,0,0,0.4);
                object-fit: cover;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        for vid in video_files:
            st.subheader(f"▶️ {vid}")
            video_path = os.path.join(video_folder, vid)
            with open(video_path, "rb") as f:
                video_bytes = f.read()
            st.video(video_bytes, format="video/mp4", start_time=0)
    else:
        st.info("🎬 No videos found in the `videos/` folder. Add `.mp4` files to display them here.")

# ----------------------------------------------------------------
# OTHER PAGES (Require CSV)
# ----------------------------------------------------------------
else:
    st.sidebar.title("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file here", type=["csv"], key="uploader")

    if uploaded_file:
        # Save uploaded CSV to app_data folder
        save_path = os.path.join(app_data_folder, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        data = pd.read_csv(save_path)
        st.sidebar.success(f"✅ Dataset '{uploaded_file.name}' Loaded Successfully!")
    else:
        st.sidebar.info("Please upload a dataset to proceed.")
        st.stop()

    numeric_columns = data.select_dtypes(include="number").columns.tolist()
    categorical_columns = data.select_dtypes(include="object").columns.tolist()

    def display_plot(fig):
        st.pyplot(fig)

# ----------------------------------------------------------------
# UNIVARIATE ANALYSIS
# ----------------------------------------------------------------
    if page == "Univariate Analysis":
        st.title("Univariate Analysis")
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

# ----------------------------------------------------------------
# BIVARIATE ANALYSIS
# ----------------------------------------------------------------
    elif page == "Bivariate Analysis":
        st.title("Bivariate Analysis")
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

# ----------------------------------------------------------------
# MULTIVARIATE ANALYSIS
# ----------------------------------------------------------------
    elif page == "Multivariate Analysis":
        st.title("Multivariate Analysis")
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
