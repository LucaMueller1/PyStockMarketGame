import streamlit as st
import depot_table
from streamlit_echarts import st_echarts

data = [
  {
    "symbol": "AAA",
    "logoUrl": "https://logodix.com/logo/1931235.png",
    "stockName": "AAA",
    "amount": 5,
    "stock_price": 3.13,
    "stock_buyin_price": 2,
    "countryId": "Germany",
    "industry": "STONKS"
  },
  {
    "symbol": "BBB",
    "logoUrl": "https://dlskits.com/wp-content/uploads/2018/05/512x512-Logo-Juventus-for-Dream-League-Soccer.png",
    "stockName": "Juve",
    "amount": 2,
    "stock_price": 1.11,
    "stock_buyin_price": 2.22,
    "countryId": "England",
    "industry": "Military"
  }
]

def run(session_state):

    st.write("Hello World!")
    st.write(session_state.auth_key)

    show_chart()

    markdown_table = depot_table.DepotTable(data)
    html = """ <table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table> """
    st.markdown(html, unsafe_allow_html=True)

    if st.button("log out"):
        session_state.page = "login"
        st.experimental_rerun()

def show_chart():
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
