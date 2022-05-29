'''
Suppose you're s service provider offering a set of services. Each of the services has a set of features for serivce consumers to select or input according to his/her requirements. It becomes difficult to accomodate all the services in one web page stacking all the services. Naturally, a multiplage application is the best for this kind of requirement. Unfortunately, Streamlit has no direct method to add a tab for a new page in a single page, while using some of the existing
features we can create a work around for building up your streamlit application with multiple pages.
----------------------
THIS IS THE THIRD APP
'''
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def app():
    st.title("Service 3")
    st.write("Welcome to service three!")
    
    df = px.data.iris()
    fig = go.Figure()
    trace = go.Scatter3d(
        x = df['sepal_width'],
        y = df['sepal_length'],
        z = df['petal_length'],
        mode = 'markers',
        marker = dict(
            size = 4,
            color = df['petal_width'],
            colorscale = 'Viridis',
            opacity = 0.7
            )
        )
    fig.add_trace(trace)
    st.plotly_chart(fig)