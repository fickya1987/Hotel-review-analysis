# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
#import plotly.figure_factory as ff



st.title('Hotel Review Analysis')

@st.cache
def load_data(nrows):
    data = pd.read_csv('C:\Users\ficky alkarim\Documents\Angkasa Pura Customer Experience 2024\Hotel-review-analysis-main\hotelreviews.csv', nrows=nrows)
    return data

reviews=load_data(500)

#Hotel review data
st.subheader('hotel reviews')
st.write(reviews)

st.bar_chart(reviews['Reviewer_Score'])
df = pd.DataFrame(reviews[:200], columns = ['Reviewer_Score','Review_Total_Negative_Word_Counts','Review_Total_Positive_Word_Counts'])
df.hist()
st.pyplot()

st.line_chart(df)

chart_data = pd.DataFrame(reviews[:40], columns=['Reviewer_Score', 'Review_Total_Negative_Word_Counts'])
st.area_chart(chart_data)

