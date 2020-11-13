from streamlit_echarts import st_echarts
import streamlit as st

def show_chart(historical_data, name:str):

    options = {
        "title": {
        "text": f"Chart for {name}"
        },
        "tooltip": {
        "trigger": 'axis'
        },
        "xAxis": {
            "type": 'category',
            "data": [data_point["timestamp"][:10] for data_point in historical_data]
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [round(data_point["stock_price"],2) for data_point in historical_data],
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
    }

    st_echarts(options=options, height="25em")