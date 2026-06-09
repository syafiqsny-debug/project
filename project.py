import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.image('image-5.png')
st.title("""Welcome to my Dashboard""")


DF = pd.read_csv('bmw (1).csv')
st.subheader("Raw Data")
st.write(DF)

DF.isnull().sum()
DF.dropna(inplace = True)
DF.duplicated().sum()
DF.drop_duplicates(inplace = True)
DF = DF[DF['year'] >= 2019]
DF = DF.rename(columns={'model': 'Model','year' : 'Year', 'price':'Price', 'transmission':'Transmission', 'mileage':'Mileage', 'mpg':'MilesperGallon'})
DF = DF[DF['fuelType']== 'Petrol']
st.subheader("Cleaned Data")
st.write(DF)


#Histogram
st.write("""Objective:
Identifying relation between miles per gallon and its frequency.""")


fig, ax = plt.subplots(figsize=(10, 6))

DF['MilesperGallon'].plot(kind='hist', 
                           edgecolor = 'black',
                    ax=ax)

plt.title('Relation between Miles per Gallon for car and frequency')

plt.xlabel('MilesperGallon')
plt.ylabel('Frequency')
st.pyplot(fig)

#Scatter Plot
st.write("""Objective:
Identifying the range of price for each car model.""")

fig, ax = plt.subplots(figsize = (8, 6))

DF.plot(kind='scatter',
        x='Model',
        y='Price',
        color = 'purple',
        ax=ax)
 
# set the title
plt.title('Comparison of model and price')

ax.set_xticklabels(DF['Model'], rotation=45) 

st.pyplot(fig)
