from splinter import Browser
from bs4 import BeautifulSoup
from datetime import datetime


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_news():

    browser = init_browser()

    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = str(soup.find('div', class_='content_title').text)
    news_p = str(soup.find('div', class_='article_teaser_body').text)
    time_stamp = str(datetime.now())

    news = {
        "time": time_stamp,
        "title": news_title,
        "paragraph": news_p,
    }

    return news


def scrape_image():

    browser = init_browser()

    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    browser.is_element_present_by_css("img.fancybox-image", wait_time=1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image_url = soup.find('img', class_='fancybox-image')['src']
    time_stamp = str(datetime.now())

    if "http:" not in featured_image_url:
        featured_image_url = "https://www.jpl.nasa.gov"+featured_image_url
        
    image_url = {
        "time": time_stamp,
        "url": featured_image_url,
    }
    
    return image_url


def scrape_weather():

    browser = init_browser()

    url = "https://twitter.com/marswxreport"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    import re
    mars_weather = soup.find(string=re.compile("Sol"))
    time_stamp = str(datetime.now())

    weather = {
        "time": time_stamp,
        "weather": mars_weather,
    }

    return weather


def scrape_facts():

    browser = init_browser()

    import pandas as pd

    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)

    tables[0]

    df = tables[0]
    df.columns = ['Description', 'Value']

    facts = {
        "desc": df.Description,
        "value": df.Value,
    }

    return facts


def scrape_hemis():

    browser = init_browser()

    import time

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_hemis = []

    for i in range(4):
        time.sleep(2)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        src = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2", class_="title").text
        img_url = 'https://astrogeology.usgs.gov' + src
        img_dict = {"title":img_title, "img_url":img_url}
        mars_hemis.append(img_dict)
        browser.back()

    return mars_hemis