import streamlit as st
import numpy as np
import pandas as pd
import time

def test_func():
    """
    関数内のヒアドキュメントは表示されないので、docstringとして利用可能
    """

    st.write('function call test')

st.title('My first app')

# イベント発火ごとに再描画されるが？
st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

if st.checkbox('Show text'):
    st.write('checkbox enable')

option = st.selectbox(
    'Which number do you like best?',
     df['first column']
)

st.write('You selected: ', option)

# 変数を変えても同じテキストだとIDが重複する
sidebar_option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column']
)

st.write('You selected:', sidebar_option)

# input test
# cf: https://docs.streamlit.io/en/stable/api.html#streamlit.text_input
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# file upload
from PIL import Image
import io 
uploaded_file = st.file_uploader('Choose a image file')

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    st.image(
        image, caption='upload images',
        use_column_width=True
    )

test_func()

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon']
# )
# st.map(map_data)

def describe_progress_bar():
    st.write('Starting a long computation...')

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    st.write('...and now we\'re done!')
