# required imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Diabetes Dashboard",
    layout="centered",
    page_icon="👩‍⚕️",
)

# setup the page
st.sidebar.title("Diabetes 👩‍⚕️")
page = st.sidebar.selectbox("Select Page",["Introduction 📘","Visualization 📊"])

# so that the image is centered
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("diabetes.png", width=900)

st.write("   ")
st.write("   ")
st.write("   ")
# load the dataset
df = pd.read_csv("diabetes.csv")

# introduction
if page == "Introduction 📘":

    st.subheader("01 Introduction 📘")

    st.markdown("##### Data Preview")
    rows = st.slider("Select a number of rows to display",5,20,5)
    st.dataframe(df.head(rows))

    st.markdown("##### Missing values")
    missing = df.isnull().sum()
    st.write(missing)

    if missing.sum() == 0:
        st.success("✅ No missing values found")
    else:
        st.warning("⚠️ you have missing values")

    st.markdown("##### 📈 Summary Statistics")
    if st.button("Show Describe Table"):
        st.dataframe(df.describe())

# data visualization
elif page == "Visualization 📊":
    
    st.subheader("02 Data Viz")

    col_x = st.selectbox("Select X-axis variable",df.columns,index=0)
    col_y = st.selectbox("Select Y-axis variable",df.columns,index=1)

    tab1, tab2, tab3 = st.tabs(["Bar Chart 📊","Line Chart 📈","Correlation Heatmap 🔥"])

    with tab1:
        st.subheader("Bar Chart")
        st.bar_chart(df[[col_x,col_y]].sort_values(by=col_x),use_container_width=True)

    with tab2:
        st.subheader("Line Chart")
        st.line_chart(df[[col_x,col_y]].sort_values(by=col_x),use_container_width=True)

    with tab3:
        st.subheader("Correlation Matrix")
        df_numeric = df.select_dtypes(include=np.number)

        fig_corr, ax_corr = plt.subplots(figsize=(18,14))
        # create the plot with seaborn 
        sns.heatmap(df_numeric.corr(),annot=True,fmt=".2f",cmap='coolwarm')
        ## render the plot in streamlit 
        st.pyplot(fig_corr)
