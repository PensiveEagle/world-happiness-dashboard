import plots
import data_functions
import streamlit as st
import pandas as pd

data = data_functions.get_data_from_csv( filepath = "Data/happy.csv" )

st.title( "World Happiness Dashboard" )
x_axis = st.selectbox( "X-axis: ", data.columns, placeholder = "country" )
y_axis = st.selectbox( "Y-axis: ", data.columns, placeholder = "gdp" )
st.subheader( f"{x_axis} by {y_axis}")
st.plotly_chart( plots.generate_line_plot( data = data, x_column = x_axis, y_column = y_axis ))