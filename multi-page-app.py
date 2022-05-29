'''
Suppose you're s service provider offering a set of services. Each of the services has a set of features for serivce consumers to select or input according to his/her requirements. It becomes difficult to accomodate all the services in one web page stacking all the services. Naturally, a multiplage application is the best for this kind of requirement. Unfortunately, Streamlit has no direct method to add a tab for a new page in a single page, while using some of the existing
features we can create a work around for building up your streamlit application with multiple pages.
----------------------
This is the main app that is for service consumer to go through the service catgory and select one of the service he/she needs to use.
'''

import service1, service2, service3, service4
import streamlit as st

services = {
    'service1': service1,
    'service2': service2,
    'service3': service3,
    'service4': service4,

}

st.sidebar.title("Service Category")
selection = st.sidebar.radio("Please select the service:", list(services.keys()))
service = services[selection]
service.app()