#請幫我自訂一個function
#連線至postgres DB
#建立連線環境參數的樣版
import psycopg2

def create_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database = "postgres",
        user = "postgres",
        password = "raspberry",
        port = "5432"
    )
    return conn

def main():
    conn = create_connection()
    if conn:
        print("成功連線至PostgreSQL資料庫")
        conn.close()
    else:
        print("無法連線至PostgreSQL資料庫")

if __name__ == "__main__":
    main()
#這個程式會連線至PostgreSQL資料庫並顯示連線成功或失敗的訊息
#請確保已經安裝psycopg2模組
#可以使用pip install psycopg2-binary來安裝
#請確保PostgreSQL資料庫已經啟動並且可以接受連線
#如果有任何問題，請檢查資料庫的設定和網路連線
#如果需要修改連線參數，請在create_connection函數中修改host、database、user、password和port的值
#這個程式可以用來測試PostgreSQL資料庫的連線是否正常