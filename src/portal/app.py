import streamlit as st
from src import widget, visualization, image_clf, time_series

selectbox_result = st.sidebar.selectbox(
    'Tutorials',
    ('Widget', 'Visualization', 'Image Classification', 'Time Series')
)

if selectbox_result == 'Widget':
    widget.main()
elif selectbox_result == 'Visualization':
    visualization.main()
elif selectbox_result == 'Image Classification':
    image_clf.main()
elif selectbox_result == 'Time Series':
    time_series.main()