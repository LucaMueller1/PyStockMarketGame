import streamlit as st
from streamlit_echarts import st_echarts

st.write("Hello World!")

options = {
    "xAxis": {
        "type": 'category',
        "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    "yAxis": {
        "type": 'value'
    },
    "series": [{
        "data": [820, 932, 901, 934, 1290, 1330, 1320],
        "type": 'line'
    }],
    "dataZoom": [{
        "type": 'inside'
    }, {
        "start": 0,
        "end": 10,
        "handleSize": '80%',
        "handleStyle": {
            "color": '#fff',
            "shadowBlur": 3,
            "shadowColor": 'rgba(0, 0, 0, 0.6)',
            "shadowOffsetX": 2,
            "shadowOffsetY": 2
        }
    }],
};

st_echarts(options=options)