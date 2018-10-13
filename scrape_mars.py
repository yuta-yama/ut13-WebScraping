from splinter import Browser
from bs4 import BeautifulSoup
from datetime import datetime
import time
import collections
import pymongo
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    scrape_data_dict = {}

    ##### SCRAPE NEWS #####
    browser = init_browser()
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = str(soup.find('div', class_='content_title').text)
    news_p = str(soup.find('div', class_='article_teaser_body').text)
    news_time = str(datetime.now())

    scrape_data_dict['news_time'] = news_time
    scrape_data_dict['news_title'] = news_title
    scrape_data_dict['news_p'] = news_p

    ##### SCRAPE FEATURED IMAGE #####
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)

    xpath = '//a[@id="full_image"]'
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()

    browser.is_element_present_by_css("img.fancybox-image", wait_time=1)

    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image_url = soup.find('img', class_='fancybox-image')['src']
    featured_image_url

    if "http:" not in featured_image_url:
        featured_image_url = "https://www.jpl.nasa.gov"+featured_image_url
        
    print('Featured Image: ' + str(featured_image_url))

    scrape_data_dict['featured_image'] = featured_image_url
        
    ##### SCRAPE WEATHER #####
    url = "https://twitter.com/marswxreport"
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    import re
    mars_weather = soup.find(string=re.compile("Sol"))

    scrape_data_dict['weather'] = mars_weather

    ##### SCRAPE FACTS TABLE #####
    url = 'https://space-facts.com/mars/'
    browser.visit
    tables = pd.read_html(url)
    time.sleep(2)
    tables[0]

    df = tables[0]
    df.columns = ['Description', 'Value']

    facts = df.to_html()
    scrape_data_dict['facts'] = facts

    ##### SCRAPE HEMISPHERES #####
    browser = init_browser()
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

    scrape_data_dict['mars_hemis'] = mars_hemis

    return scrape_data_dict

    print("Finished Scraping")