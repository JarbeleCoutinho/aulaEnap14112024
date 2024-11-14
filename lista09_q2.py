import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

df.head(3)

st.title('Localização das comunidades quilombolas (2022)')
