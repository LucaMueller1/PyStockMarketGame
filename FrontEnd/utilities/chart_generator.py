from streamlit_echarts import st_echarts
import streamlit as st

def show_stock_chart(theme: str, historical_data, name: str):
    if theme == "dark":
        __show_stock_chart_dark(historical_data, name)
    else:
        __show_stock_chart_light(historical_data, name)


def __show_stock_chart_light(historical_data, name:str):

    options = {
        "title": {
        "text": f"Chart for {name}",
        "textStyle": {
        "fontSize": 16,
        "color": "#000000"},
        },
        "textStyle": {"color": "#000000"},
        "tooltip": {
        "trigger": 'axis'
        },
        "xAxis": {
            "type": 'category',
            "data": [data_point["timestamp"][:10] for data_point in historical_data],
            "splitLine": {
         "show": False
      }
        },
        "yAxis": {
            "type": 'value',
            "splitLine": {
         "show": False
      },
        },
        "series": [{
            "data": [round(data_point["stock_price"],2) for data_point in historical_data],
            "type": 'line'
        }],
        "dataZoom": [{
            "type": 'inside',
            "start": 90
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

def __show_stock_chart_dark(historical_data, name:str):
    options = {
        "title": {
        "text": f"Chart for {name}",
        "textStyle": {
        "fontSize": 16,
        "color": "#000000"},
        },
        "textStyle": {"color": "#000000"},
        "tooltip": {
        "trigger": 'axis'
        },
        "xAxis": {
            "type": 'category',
            "data": [data_point["timestamp"][:10] for data_point in historical_data],
            "splitLine": {
         "show": False
      }
        },
        "yAxis": {
            "type": 'value',
            "splitLine": {
         "show": False
      },
        },
        "series": [{
            "data": [round(data_point["stock_price"],2) for data_point in historical_data],
            "type": 'line'
        }],
        "dataZoom": [{
            "type": 'inside',
            "start": 90
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

def show_portfolio_chart(theme: str, historical_data):
    if theme == "dark":
        __show_portfolio_chart_dark(historical_data)
    else:
       __show_portfolio_chart_light(historical_data)

def __show_portfolio_chart_dark(historical_data):

    options = {
        "title": {
        "text": f"""{round(historical_data[-1]["marketValue"],2):,}$""",
        "textStyle": {
        "fontSize": 30,
        "color": "rgba(255, 255, 255, 1)"},
        },
        "textStyle": {"color": "rgba(255, 255, 255, 1)"},
        "tooltip": {
        "trigger": 'axis'
        },
        "xAxis": {
            "showGrid": "false",
            "data": [data_point["timestamp"][:10] for data_point in historical_data],
            "splitLine": {
         "show": False
      },
        },
        "yAxis": {
            "showGrid": "false",
            "splitLine": {
                "show": False
            },
        },
        "series": [{
            "data": [round(data_point["marketValue"],2) for data_point in historical_data],
            "type": 'line',
            "lineStyle": {"color": '#f63366'}
        }],
        "dataZoom": [{
            "type": 'inside',
            "start": 0,
            "end": 100
        }, {
            "start": 0,
            "end": 10,
        }],
    }

    st_echarts(options=options, height="25em")

def __show_portfolio_chart_light(historical_data):

    options = {
        "title": {
        "text": f"""{round(historical_data[-1]["marketValue"],2):,}$""",
        "textStyle": {
        "fontSize": 30,
        "color": "#000000"},
        },
        "textStyle": {"color": "#000000"},
        "tooltip": {
        "trigger": 'axis'
        },
        "xAxis": {
            "showGrid": "false",
            "data": [data_point["timestamp"][:10] for data_point in historical_data],
            "splitLine": {
         "show": False
      },
        },
        "yAxis": {
            "showGrid": "false",
            "splitLine": {
                "show": False
            },
        },
        "series": [{
            "data": [round(data_point["marketValue"],2) for data_point in historical_data],
            "type": 'line',
            "lineStyle": {"color": '#f63366'}
        }],
        "dataZoom": [{
            "type": 'inside',
            "start": 0,
            "end": 100
        }, {
            "start": 0,
            "end": 10,
        }],
    }

    st_echarts(options=options, height="25em")