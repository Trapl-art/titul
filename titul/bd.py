import pyodbc
from flask import Flask, render_template, url_for, request, redirect

# Параметры подключения
server = '(localdb)\MSSQLLocalDB'
database = 'Titul1'
username = ""
password = ""

# Строка подключения
app = Flask(__name__)
connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Создание соединения
try:
    connection = pyodbc.connect(connection_string)
    print("Успешное подключение к базе данных")

    # Создание курсора
    cursor = connection.cursor()

    # Выполнение запроса
    cursor.execute("SELECT * FROM feed")
    result = cursor.fetchall()
    print(result)

    # Вывод результатов
    for row in cursor:
        print(row)

except pyodbc.Error as ex:
    print("Ошибка при подключении к базе данных:", ex)




@app.route('/', methods=['POST', 'GET'])
def index():
    cursor.execute("SELECT fulname FROM feed")
    name = cursor.fetchall()
    return render_template("index", name=name)
    cur = connect.cursor()
    cur.execute("SELECT feedback FROM feed")
    feedback = cur.fetchall()
    return render_template("indexs", feedback=feedback)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


