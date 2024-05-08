from pysql import MY_DB

mydb = MY_DB()
mydb.connect("data.db")
data = {
    "id":3,
    "color": "green",
    "address": "Ha Noi, Viet Nam",
    "type":"consummer",
    "price":1000
}
# mydb.insert_data("goods_data",data)
# s = mydb.select_all_columns("goods_data")
result = mydb.select_data("goods_data", "id = 2")
# print(s)
print(result)