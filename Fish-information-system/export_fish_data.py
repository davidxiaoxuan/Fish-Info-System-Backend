import mysql.connector
import pandas as pd

# 连接到 MySQL 数据库
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='davidchen114',
    database='fish_db'
)

# 查询数据
query = "SELECT * FROM core_fish"
df = pd.read_sql(query, conn)

# 保存为 JSON 文件
json_file_path = 'C:/Users/david/Fish-information-system/public/data/fishData.json'
df.to_json(json_file_path, orient='records', lines=True)

print(f"Data has been successfully exported to {json_file_path}")

# 关闭连接
conn.close()
