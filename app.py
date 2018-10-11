from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

## ROUTES ##

@app.route('/')
def home():
    
    mars_info = mongo.db.collection.find()

    return render_template('index.html', mars_info=mars_info)

@app.route('/scrape')
def scrape():

    news = scrape_mars.scrape_news()
    image = scrape_mars.scrape_image()
    weather = scrape_mars.scrape_weather()
    facts = scrape_mars.scrape_facts()
    hemis = scrape_mars.scrape_hemis()

    mars_dict = {
        "news_title": news["title"],
        "news_p": news["paragraph"],
        "image": image["url"],
        "weather": weather["weather"],
        "fact_desc": facts["desc"],
        "fact_value": facts["value"],
        "hemis_title": hemis["title"],
        "hemis_url": hemis["img_url"],
    }

    mongo.db.collection.insert_one(mars_dict)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

