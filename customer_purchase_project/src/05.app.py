import streamlit as st, os, pandas as pd
st.title('Uploaded Dataset Explorer')
path = os.path.join('data','processed','dataset_clean.csv')
if not os.path.exists(path):
    st.warning('Run data_prep first')
else:
    df = pd.read_csv(path, parse_dates=True)
    st.dataframe(df.head(200))
