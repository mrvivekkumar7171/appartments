import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.set_page_config(page_title="Apartment Price Predictor", page_icon="👋", layout="wide")


with open('A:/CODES/PROJECTS/appartments/models/df.pkl','rb') as file:
    df = pickle.load(file)

with open('A:/CODES/PROJECTS/appartments/models/pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)


st.header('Price Predictor')

property_type = st.selectbox('Property Type',['flat','house'], index=0)
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()), index=0)
property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()), index=1)

col1, col2, col3 = st.columns(3)
with col1:
    bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist()), index=2))
with col2:
    bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist()), index=2))
with col3:
    balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()), index=1)

col1, col2, col3 = st.columns(3)
with col1:
    built_up_area = float(st.number_input('Built Up Area', value=2))
with col2:
    servant_room = float(st.selectbox('Servant Room',[0.0, 1.0], index=1))
with col3:
    store_room = float(st.selectbox('Store Room',[0.0, 1.0], index=1))

col1, col2, col3 = st.columns(3)
with col1:
    furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()), index=2)
with col2:
    luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()), index=2)
with col3:
    floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()), index=2)



if st.button('Predict', type="primary", width="stretch"):

    # form a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.markdown("""<style>div[data-testid="stAlert"] {text-align: center;}</style>""", unsafe_allow_html=True)
    st.success(f"**The Price of the flat is between {low:.2f} Cr and {high:.2f} Cr.**")