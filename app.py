from flask import Flask, render_template, render_template_string, request, redirect, url_for, session, jsonify
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
    code VARCHAR(255), name VARCHAR(255),description NVARCHAR(N),
    qrCode  NVARCHAR(N),barcode  NVARCHAR(N), image  NVARCHAR(N)); """
    mycursor.execute(sql)
    mydb.commit()

    sql = """CREATE TABLE IF NOT EXISTS markets (id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(255), name VARCHAR(255),description NVARCHAR(N),
    country VARCHAR(255),city VARCHAR(255), region VARCHAR(255),
    googleLink  NVARCHAR(N), address  NVARCHAR(N)); """
    mycursor.execute(sql)
    mydb.commit()

    sql = """CREATE TABLE IF NOT EXISTS prices (id INT AUTO_INCREMENT PRIMARY KEY,
    itemId INT, marketId INT,price INT,description NVARCHAR(N)); """
    mycursor.execute(sql)
    mydb.commit()

def insert_item(code, name, description, qrCode, image, barcode):
    sql = """INSERT INTO items (code, name, description, qrCode, image, barcode)
                 VALUES ('{}', '{}', '{}', '{}', '{}', '{}');""".format(code, name, description, qrCode, image, barcode)
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    # print(mycursor.rowcount, "record inserted.")

def insert_market(code, name, description, googleLink, country, city, region,address):
    sql = """INSERT INTO items (code, name, description, googleLink, country, city, region,address)
                 VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(code, name, description,  googleLink, country, city, region,address)
    print(sql)
    mycursor.execute(sql)
    mydb.commit()

def insert_price(itemId, marketId, price, description):
    sql = """INSERT INTO items (itemId, marketId, price, description)
                 VALUES ({}, {}, {}, '{}');""".format(itemId, marketId, price, description)
    print(sql)
    mycursor.execute(sql)
    mydb.commit()

def select_items():
    sql = """SELECT * FROM items;"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return list(myresult)

def select_item():
    sql = """SELECT * FROM items WHERE id = 1;"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x) 
    return list(myresult)

def select_markets():
    sql = """SELECT * FROM markets;"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return list(myresult)

def select_market():
    sql = """SELECT * FROM markets WHERE id = 1;"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x) 
    return list(myresult)

init_db()
# insert_ibtem()
print('select all items')
select_items()
print('one item')
select_one_item()


@app.route('/insertItem', methods=['POST','GET'])
def insertItem():
    if(request.form):
        insert_item(request.form.get('code'),request.form.get('name'),request.form.get('description'),request.form.get('qrCode'),request.form.get('image'),request.form.get('barcode'))
    return render_template('item.html')

@app.route('/insertMarket', methods=['POST','GET'])
def insertMarket():
    if(request.form):
        insert_market(request.form.get('code'),request.form.get('name'),request.form.get('description'),request.form.get('googleLink'),request.form.get('country'),request.form.get('city'),request.form.get('region'),request.form.get('address'))
    return render_template('market.html')

@app.route('/insertPrice', methods=['POST','GET'])
def insertPrice():
    if(request.form):
        insert_price(request.form.get('itemId'),request.form.get('marketId'),request.form.get('price'),request.form.get('description'))
    return render_template('addPrice.html')


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
