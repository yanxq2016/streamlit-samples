'''
Suppose you're s service provider offering a set of services. Each of the services has a set of features for serivce consumers to select or input according to his/her requirements. It becomes difficult to accomodate all the services in one web page stacking all the services. Naturally, a multiplage application is the best for this kind of requirement. Unfortunately, Streamlit has no direct method to add a tab for a new page in a single page, while using some of the existing
features we can create a work around for building up your streamlit application with multiple pages.
----------------------
THIS IS THE FIRST APP
'''
import streamlit as st
def app():
    st.title("Application 1")
    st.write("Welcome to application one!")
