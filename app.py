from flask import Flask, render_template
from flask import render_template_string
from flask import request, redirect
from flask import url_for, session, jsonify
from flask import send_file
from base64 import b64encode
import mysql.connector

app = Flask(__name__)
#establish connection to mysql
conn = mysql.connector.connect(host="localhost", user="root", password="root")
cursor = conn.cursor()
# query = "DROP DATABASE BestPrice;CREATE DATABASE IF NOT EXISTS BestPrice;"
# create database BestPrice
query = "CREATE DATBASE IF NOT EXISTS BestPrice;"
cursor.execute(query, multi=True)
#establish connection to databases BestPrice
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database="BestPrice")
mycursor = mydb.cursor()

# create tables for database
def init_db():
    sql = """CREATE TABLE IF NOT EXISTS items
     (id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(255), name VARCHAR(255),description VARCHAR(5000),
    qrCode  VARCHAR(5000),barcode  VARCHAR(5000), image  LONGBLOB ); """
    mycursor.execute(sql)
    mydb.commit()

    sql = """CREATE TABLE IF NOT EXISTS markets
     (id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(255), name VARCHAR(255),description VARCHAR(5000),
    country VARCHAR(255),city VARCHAR(255), region VARCHAR(255),
    googleLink  VARCHAR(5000), address  VARCHAR(5000)); """
    mycursor.execute(sql)
    mydb.commit()

    sql = """CREATE TABLE IF NOT EXISTS prices
     (id INT AUTO_INCREMENT PRIMARY KEY,
    itemId INT, marketId INT,price INT,description VARCHAR(5000)); """
    mycursor.execute(sql)
    mydb.commit()


init_db()
# insert item
def insert_item(code, name, description, qrCode, image, barcode):
    try:
        sql = ''
        print(sql)
        mycursor.execute("""INSERT INTO items
         (code, name, description, qrCode, image, barcode)
         VALUES (%s,%s,%s,%s, %s,%s);""", (code, name, description, qrCode,
                                           image, barcode))
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        print(f"Error while connecting to MySQL: {e}")

# insert market
def insert_market(code, name, description, googleLink,
                  country, city, region, address):
    sql = """INSERT INTO markets (code, name, description,
     googleLink, country, city, region,address)
     VALUES ('{}', '{}', '{}', '{}',
      '{}', '{}', '{}', '{}');""".format(code, name,
                                         description, googleLink,
                                         country, city, region, address)
    print(sql)
    mycursor.execute(sql)
    mydb.commit()

#insert price
def insert_price(itemId, marketId, price, description):
    sql = """INSERT INTO prices (itemId, marketId, price, description)
                 VALUES ({}, {}, {}, '{}');""".format(itemId, marketId,
                                                      price, description)
    print(sql)
    mycursor.execute(sql)
    mydb.commit()

# update all item columns 
def update_item_All(code, name, description, qrCode, image, barcode,_id):
    try:
        sql = ''
        print(sql)
        mycursor.execute("""UPDATE items
         SET code= %s ,name=%s, description=%s, qrCode=%s, image=%s, barcode=%s 
         WHERE id= %s ;""", (code, name, description, qrCode,
                                           image, barcode,_id))
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        print(f"Error while connecting to MySQL: {e}")

# update all item columns except image 
def update_item(code, name, description, qrCode, barcode,_id):
    try:
        sql = ''
        print(sql)
        mycursor.execute("""UPDATE items
         SET code= %s ,name=%s, description=%s, qrCode=%s, barcode=%s 
         WHERE id= %s ;""", (code, name, description, qrCode,barcode,_id))
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")
    except Exception as e:
        print(f"Error while connecting to MySQL: {e}")

# update market
def update_market(code, name, description, googleLink,
                  country, city, region, address,_id):
    mycursor.execute("""UPDATE markets SET code = %s , name= %s, description= %s,
     googleLink= %s, country= %s, city= %s, region= %s,address= %s 
     WHERE id= %s;""",(code, name, description, googleLink, country, city, region, address,_id))
    mydb.commit()

# select all items
def select_items():
    sql = """SELECT id,code,name,description,barcode,image FROM items;"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return list(myresult)

# select one item by id
def select_item(id):
    sql = """SELECT id,code,name,description,barcode,image FROM items WHERE id = {};""".format(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    return list(myresult)

# select all markets
def select_markets():
    sql = """SELECT * FROM markets;"""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return list(myresult)

# select one market by id
def select_market(id):
    sql = """SELECT * FROM markets WHERE id = {};""".format(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return list(myresult)

# search all prices for item by name or code or barcode
def select_prices(searchText):
    sql = """SELECT items.image, items.name,prices.price,markets.name,
            items.id as itemId ,markets.id as marketId
            FROM prices
            JOIN markets ON prices.marketId=markets.id
            JOIN items ON prices.itemId=items.id WHERE items.name LIKE '%{}%'
            OR items.barcode LIKE '%{}%' OR
            items.code LIKE '%{}%';""".format(searchText, searchText,
                                              searchText)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return list(myresult)

# save item action
@app.route('/insertItem/<int:id>', methods=['POST', 'GET'])
def insertItem(id):   
    if (request.form):
        # print(request.form.get('image'))
        # with open(request.form.get('image'), 'rb') as file:
        #     binaryData = file.read()
        if 'image' not in request.files:
            return "No image part in the request", 400
        file = request.files['image']
        if id == 0:
            if file.filename == '':
                return "No image selected for uploading", 400

            if file:
                image_data = file.read()
            insert_item(request.form.get('code'),
                        request.form.get('name'),
                        request.form.get('description'),
                        request.form.get('qrCode'),
                        image_data, request.form.get('barcode'))
        else:
            if file.filename == '':
                update_item(request.form.get('code'),
                            request.form.get('name'),
                            request.form.get('description'),
                            request.form.get('qrCode'),
                            request.form.get('barcode'),
                            id)
            else:
                if file.filename == '':
                    return "No image selected for uploading", 400

                if file:
                    image_data = file.read()
                update_item_All(request.form.get('code'),
                                request.form.get('name'),
                                request.form.get('description'),
                                request.form.get('qrCode'),
                                image_data,
                                request.form.get('barcode'),
                                id)
    return render_template('item.html')

# save market action
@app.route('/insertMarket/<int:id>', methods=['POST', 'GET'])
def insertMarket(id):
    print(request.form)
    if (request.form):
        if id == 0:
            insert_market(request.form.get('code'),
                          request.form.get('name'),
                          request.form.get('description'),
                          request.form.get('googleLink'),
                          request.form.get('country'),
                          request.form.get('city'),
                          request.form.get('region'),
                          request.form.get('address'))
        else:
            update_market(request.form.get('code'),
                          request.form.get('name'),
                          request.form.get('description'),
                          request.form.get('googleLink'),
                          request.form.get('country'),
                          request.form.get('city'),
                          request.form.get('region'),
                          request.form.get('address'),
                          id)

    return render_template('market.html')

# save price action
@app.route('/insertPrice', methods=['POST', 'GET'])
def insertPrice():
    if (request.form):
        insert_price(request.form.get('itemId'),
                     request.form.get('marketId'),
                     request.form.get('price'),
                     request.form.get('description'))
    return render_template('addPrice.html')

# home page
@app.route('/')
def mainUsers():
    return render_template('index.html')

# retrieve item by id
@app.route('/item/<int:id>')
def item_id(id):
    data = []
    itemData = select_item(id)
    for x in itemData:
        # The returned data will be a list of list
        image = x[5]
        # Decode the string
        # image = base64.b64decode(image)
        image = b64encode(image).decode("utf-8")
        data.append([x[0], x[1], x[2], x[3], x[4], image])
        print(x[3], x[4])
        if len(data) > 0:
            return render_template('item.html', data=data[0])
    return render_template('item.html')

# retrieve market by id
@app.route('/market/<id>', methods=['GET'])
def market_id(id: int):
    data = select_market(id)
    return render_template('market.html', data=data[0])

# item page
@app.route('/item')
def item():
    return render_template('item.html')

# market page
@app.route('/market')
def market():
    return render_template('market.html')

# add price page
@app.route('/addPrice')
def addPrice():
    items = select_items()
    markets = select_markets()
    print(items)
    return render_template('addPrice.html', markets=markets, items=items)

# search page
@app.route('/search')
def search():
    prices = []
    if (request.args):
        searchText = request.args.get('searchText')
        pricesData = select_prices(searchText)
        for data in pricesData:
            # The returned data will be a list of list
            image = data[0]
            # Decode the string
            # image = base64.b64decode(image)
            image = b64encode(image).decode("utf-8")
            prices.append([image, data[1], data[2], data[3], data[4], data[5]])
    return render_template('search.html', prices=prices)

# about page
@app.route('/about')
def about():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
