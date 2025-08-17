import streamlit as st
import datasource_mine
from datetime import date

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人數")
st.subheader("進出站人數顯示區")

@st.cache_resource
def get_stations():
    """取得車站資料"""
    # 假設有一個 get_all_stations() 回傳所有車站名稱
    return datasource_mine.get_all_stations()

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
def fetch_station_data(station, selected_date):
    # 假設 start_date 和 end_date 都設為 selected_date
    return datasource_mine.get_station_data(station, selected_date, selected_date)

data = fetch_station_data(station, selected_date)
if data is not None and not data.empty:
    st.dataframe(data)
else:
    st.info("查無資料")
