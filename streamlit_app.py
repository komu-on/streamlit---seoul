import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()


st.write("Steamlit supports a wide range of data visualizations")

all_users=['Alice','Bob','Charly']
with st.container(border=True):
    users=st.multiselect('Users',all_users, default=all_users)
    rolling_average=st.toggle("Rolling average")

np.random.seed(42)
data=pd.DataFrame(np.random.randn(20, len(users)),columns=users)

if rolling_average:
    data=data.rolling(7).mean().dropna()

tab1, tab2=st.tabs(["Chart", "Dataframe"])
tab1.line_chart(data, height=250)
tab2.dataframe(data, height=250, use_container_width=True)
