from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

## ROUTES ##

@app.route('/')
def home():
    mars_data = mongo.db.mars_data.find_one()
    return render_template('index.html', mars_data=mars_data)

@app.route('/scrape')
def scrape():
    mars_data = mongo.db.mars_data
    mars_scrape_data = scrape_mars.scrape()
    mars_data.update({}, mars_scrape_data, upsert=True)
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)