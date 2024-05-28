from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="localhost", user="root", password="root")
cursor = conn.cursor()
query = "DROP DATABASE BestPrice;CREATE DATABASE IF NOT EXISTS BestPrice;"
cursor.execute(query,multi=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="BestPrice"
)
mycursor = mydb.cursor()


def init_db():
    sql = """CREATE TABLE IF NOT EXISTS items (id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(255), name VARCHAR(255),description VARCHAR(255),
    qrCode VARCHAR(255),barcode VARCHAR(255), image VARCHAR(255)); """
    mycursor.execute(sql)
    mydb.commit()


def insert_item():
    sql = """INSERT INTO items (code, name, description, qrCode, image, barcode)
                 VALUES ('1','12','13','11111','0000', '78521' );"""
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def select_items():
    sql = """SELECT * FROM items;"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def select_one_item():
    sql = """SELECT * FROM items WHERE id = 1;"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)        


init_db()
# insert_ibtem()
print('select all items')
select_items()
print('one item')
select_one_item()

@app.route('/')
def mainUsers():
    return render_template('index.html')


@app.route('/item')
def item():
    return render_template('item.html')


@app.route('/market')
def market():
    return render_template('market.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/addPrice')
def addPrice():
    return render_template('addPrice.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
