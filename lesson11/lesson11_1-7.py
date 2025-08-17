import streamlit as st
import lesson11.datasource_mine as datasource_mine
from datetime import date

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人數")
st.subheader("進出站人數顯示區")

@st.cache_resource
def get_stations():
    """取得車站資料"""
    return datasource_mine.get_stations_names()

stations = get_stations()
if stations is None:
    st.error("無法取得車站資料，請稍後再試。")
    st.stop()

common_stations = ["臺北", "高雄", "臺中", "臺南", "基隆"]

quick_options = common_stations + (["其他"] if len(stations) > len(common_stations) else [])
choice = st.sidebar.radio("快速選擇常用車站", quick_options)

if choice == "其他":
    station = st.sidebar.selectbox(
        "請選擇車站",
        stations,
    )
else:
    station = choice

# 新增日期選擇欄位
selected_date = st.sidebar.date_input("選擇日期", value=date(2023, 1, 1), min_value=date(2023, 1, 1), max_value=date(2023, 12, 31))

st.write("您選擇的車站:", station)
st.write("您選擇的日期:", selected_date)

# 查詢資料並顯示
@st.cache_data
def get_station_data(station, selected_date):
    # 請確認 datasource.py 有下方這個函數，或根據實際情況修改名稱
    # 如果沒有 get_station_info，請將下行函數名稱改為正確的，例如 get_station_data
    return datasource_mine.get_station_data(station, selected_date)

data = get_station_data(station, selected_date)
if data is not None and not data.empty:
    st.dataframe(data)
else:
    st.info("查無資料")
