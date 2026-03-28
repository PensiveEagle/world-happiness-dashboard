import data_functions
import plotly.express as px
from plotly.graph_objs._figure import Figure as plotly_figure
import pandas as pd

def generate_line_plot( data: pd.DataFrame, x_column: str, y_column: str ) -> plotly_figure:
    plot =px.line( data_frame = data, x = data[x_column], y = data[y_column], labels = { "x": x_column, "y": y_column } )
    return plot
    
if __name__ == "__main__":
    import streamlit as st
    line_chart = generate_line_plot( data_functions.get_data_from_csv(), "happiness", "gdp" )
    print( type( line_chart ) )
    st.title( "test chart" )
    st.plotly_chart( line_chart )