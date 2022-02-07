import streamlit as st
import plotly.figure_factory as ff
import numpy as np
from PIL import Image
import plotly.express as px
import pandas as pd

df = pd.read_csv('result_table.csv')


image = Image.open('logo.jpeg')

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("")

with col2:
    st.image(image)


with col3:
    st.write("")
"""
# Table Visualization!. 
"""



# Draw some dummy content in main page and sidebar.
def draw_all(
    key,
    plot=False,
):

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.write('R1')
        r1 = st.checkbox("10%", key=key)

    with col2:
        st.write('R2')
        r2 = st.checkbox("15%", key=key)


    with col3:
        st.write('R3')
        r3 = st.checkbox("20%", key=key)

    st.markdown('#')
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.write('T1')
        t1 = st.checkbox("5 min ⏱️", key=key)

    with col2:
        st.write('T2')
        t2 = st.checkbox("10 min ⏱️", key=key)


    with col3:
        st.write('T3')
        t3 = st.checkbox("15 min ⏱️", key=key)
    # st.checkbox("Is this cool or what?", key=key)
    # st.radio(
    #     "How many balloons?",
    #     ["1 balloon ", "2 balloons 🎈🎈", "3 balloons 🎈🎈🎈"],
    #     key=key,
    # )



    # if plot:
    #     st.write("Oh look, a plot:")
    #     x1 = np.random.randn(200) - 2
    #     x2 = np.random.randn(200)
    #     x3 = np.random.randn(200) + 2

    #     hist_data = [x1, x2, x3]
    #     group_labels = ["Group 1", "Group 2", "Group 3"]

    #     fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

    #     st.plotly_chart(fig, use_container_width=True)

    # #st.file_uploader("You can now upload with style", key=key)
    # time_value = st.slider(
    #     "Choose the Time: ", min_value=5, max_value=15, step=5, key=key
    # )
    st.markdown('#')
    col1, col2 = st.columns([1,1])

    with col1:

        """
        ## Number 1. 
        """
        if r1 and t1:
            st.write('30')
            st.balloons()
        elif r1 and t2:
            st.write('50')
            st.balloons()

        elif r1 and t3:
            st.write('85')
            st.balloons()

        elif r2 and t1:
            st.write('63')
            st.balloons()

        
        elif r2 and t2:
            st.write('74')
            st.balloons()


        elif r2 and t3:
            st.write('10')
            st.balloons()


        elif r3 and t1:
            st.write('94')
            st.balloons()

        
        elif r3 and t1:
            st.write('110')
            st.balloons()


        
        elif r3 and t2:
            st.write('12')
            st.balloons()




    with col2:

        """
        ## Number 2. 
        """
        if r1 and t1:
            st.write('30')
        elif r1 and t2:
            st.write('50')
        elif r1 and t3:
            st.write('85')
        
        elif r2 and t1:
            st.write('63')
        
        elif r2 and t2:
            st.write('74')

        elif r2 and t3:
            st.write('10')

        elif r3 and t1:
            st.write('94')
        
        elif r3 and t1:
            st.write('110')

        
        elif r3 and t2:
            st.write('12')

    if plot:
        #col1 , col2 = st.columns([1,1])
       # with col1:
            """
        ## Plot Rate and temperature vs Number1. 
        """
            st.write("Here is the plot using number1")
        #  st.json({"data": [1, 2, 3, 4]})
        #  st.dataframe({"data": [1, 2, 3, 4]})
        #  st.table({"data": [1, 2, 3, 4]})
            fig = px.line_3d(df, x=df.Rate, y=df.Time, z=df.number1)
            fig2 = px.line_3d(df, x=df.Rate, y=df.Time, z=df.number2)
            st.plotly_chart(fig,use_container_width=True)
            

       # with col2:
         #   st.write("Here is the plot using number2")
         #   fig2 = px.line_3d(df, x=df.Rate, y=df.Time, z=df.number2)
            """
            ## Plot Rate and temperature vs Number2. 
            """
            st.plotly_chart(fig2, use_container_width=True)


draw_all("main", plot=True)
