import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Question 3 - Python')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")


if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        bins = np.arange(df['Age'].min(), df['Age'].max() + 2) - 0.5
        fig, ax = plt.subplots()
        ax.hist(df['Age'], edgecolor='black', bins=bins)
        ax.set_xlabel('Age')
        ax.set_ylabel('Count')
        ax.set_title('Age Distribution')
        ax.set_xticks(range(df['Age'].min(), df['Age'].max()+1))
        ax.set_xlim([df['Age'].min()-1, df['Age'].max()+1])
        ax.yaxis.get_major_locator().set_params(integer=True)
        st.pyplot(fig)
        
    except:
        st.error("Something went wrong")