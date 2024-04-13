import sqlite3


class MY_DB():
    def connect(self, name = "data.db"):
        self.conn = sqlite3.connect(name)
    
    def close(self):
        self.conn.close()

    def create_table(self, table_name, columns):
        print(table_name)
        print(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for column_name, data_type in columns.items():
            query += f"{column_name} {data_type}, "
        query = query[:-2]  # Loại bỏ dấu phẩy cuối cùng và khoảng trắng dư thừa
        query += ");"

        self.conn.execute(query)
    def insert_data(self, table_name, data):

        cursor = self.conn.cursor()

    
        query = f"INSERT INTO {table_name} ("
        columns = ', '.join(data.keys())
        values = ', '.join(['?' for _ in data.keys()])
        query += f"{columns}) VALUES ({values})"

        cursor.execute(query, list(data.values()))
        self.conn.commit()

    def update_data(self,table_name, data, condition):

        cursor = self.conn.cursor()
        query = f"UPDATE {table_name} SET "
        for key, value in data.items():
            query += f"{key} = ?, "
        query = query[:-2]  
        query += f" WHERE {condition}"

        cursor.execute(query, list(data.values()))

        # Lưu các thay đổi
        self.conn.commit()
    def delete_data(self,table_name, condition):
        cursor = self.conn.cursor()
        query = f"DELETE FROM {table_name} WHERE {condition}"
        cursor.execute(query)
        self.conn.commit()
        
    def order_by_id(self,table_name):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {table_name} ORDER BY id"
        cursor.execute(query)

    def select_all(self,table_name):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {table_name}"
        self.result = cursor.execute(query)
        return self.result
    def get_table_columns(self, table_name):
        cursor = self.conn.cursor()

        cursor.execute("PRAGMA table_info({})".format(table_name))

        columns = cursor.fetchall()

        columns_list = [column[1] for column in columns]

        return columns_list
<<<<<<< HEAD
    def check_value_exist(self, table_name, column_name, value):
        cursor = self.conn.cursor()
        query = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = ?"
        cursor.execute(query, (value,))
        count = cursor.fetchone()[0]
        if count > 0:
            return True
        else:
            return False
=======
>>>>>>> 2542a42e6b3bdd52084d22447e81cea35590f49f
#### code sử dụng classs MY_DB()
#Create table
# database_properties = {
#     "users": {
#         "id": "INTEGER PRIMARY KEY",
#         "username": "TEXT NOT NULL",
#         "email": "TEXT NOT NULL"
#     }
# }
# mydb = MY_DB()
# mydb.connect("database.db")

# # Tạo bảng với các thuộc tính được chỉ định
# for table_name, columns in database_properties.items():
#     mydb.create_table(table_name, columns)
# user_data = {
#     "id":11120,
#     "username": "john_doe",
#     "email": "john.doe@example.com"
# }
#insert data
# mydb.insert_data("users", user_data)
# mydb.update_data(
#     "users",
#     {"username": "new_username", "email": "new_email@example.com"},
#     "id = 1"
# )
#delete data
#delete_data("users", "id = 1")

#//sort data
#sorted_data = order_by_id("users")
# mydb.close() 