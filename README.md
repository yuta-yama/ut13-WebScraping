# Mission to Mars

## Description
A web application that scrapes multiple websites for data related to the Mission to Mars and displays the information in a HTML page using Flask.

## Tools Used
**Web Scraping, Python, BeautifulSoup, Pandas, Splinter, MongoDB, Flask, HTML, CSS, Bootstrap**

## Step 01 - Web Scraping
Splinter was used to navigate the sites below. BeautifulSoup was used to find and parse out the necessary data from HTML elements.

* __NASA Mars News__ - Scraped [NASA Mars News Site](https://mars.nasa.gov/news/) for the latest news title and paragraph text.
* __JPL Mars Space Images__ - Scraped [JPL site](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) for the featured space image using splinter.
* __Mars Weather__ - Scraped the [Mars Weather Twitter Account](https://twitter.com/marswxreport?lang=en) for the latest Mars weather tweet.
* __Mars Facts__ - Scraped the [Mars Facts Webpage](http://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet.
* __Mars Hemisphere__ - Scraped for high resolution images from the [Astrogeology Site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) and displayed them in Bootstrap cards.

## Step 02 - MongoDB and Flask

MongoDB and Flask was used to create a HTML page that displays all the scraped info. Bootstrap was used to structure the design of the HTML templates.

## Finished Result
![mission_to_mars](Images/yuta_mars_screenshot.png)

