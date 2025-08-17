import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Make sure this is called to load the environment variables

def get_station_data(station, selected_date):
    try:
        # Use environment variables for the connection details
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port=os.getenv("PORT", "5432")  # Default to 5432 if not set
        )

        query = """
        SELECT r."日期", s."stationName", r."進站人數", r."出站人數"
        FROM "每日各站進出站人數" r
        JOIN "台鐵車站資訊" s
          ON s."stationName" = %s
          AND r."車站代碼" = s."stationCode"
        WHERE r."日期" = %s;
        """
        df = pd.read_sql(query, conn, params=(station, selected_date))

        return df  # Return the DataFrame directly

    except psycopg2.Error as e:
        print(f"資料庫連線或查詢失敗：{e}")
        return None
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")
        return None
    finally:
        # Ensure resources are released properly
        if 'conn' in locals():
            conn.close()
