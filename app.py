from flask import Flask, render_template
app = Flask(__name__)


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
