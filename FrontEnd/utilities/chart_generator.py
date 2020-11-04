from streamlit_echarts import st_echarts

def show_chart(historical_data):

    options = {
        "xAxis": {
            "type": 'category',
            "data": [data_point["timestamp"][:9] for data_point in historical_data]
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [data_point["stock_price"] for data_point in historical_data],
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

    st_echarts(options=options)