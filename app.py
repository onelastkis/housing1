import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('Calfornia Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
House_Price_filter = st.slider('Minimal Median House Price:', 0.0, 500001, 200000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults



df= df[(df.median_house_value >= House_Price_filter)]


df= df[df.ocean_proximity.isin(location_filter)]


filter=st.radio('Choose income level',
        ['Low','Medium','High'])
if filter=='High':
    df = df[df.median_house_value >4.5]
elif filter=='Medium':
    df = df[(df.median_house_value <4.5)&(df.median_house_value >2.5)]
elif filter=='Low':
    df = df[df.median_house_value <=2.5]


# show on map
st.map(df)
