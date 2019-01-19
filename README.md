# Mission to Mars

## Tools Used
### Web Scraping, Python, BeautifulSoup, Pandas, Splinter, MongoDB, Flask, HTML, CSS, Bootstrap

## Description
I built a web application that scrapes multiple websites for data related to the Mission to Mars and displayed the information in a HTML page using Flask.

## Step 01 - Web Scraping
I used Splinter to navigate the sites below and BeautifulSoup to help find and parse out the necessary data from HTML elements.

### NASA Mars News
I scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest news title and paragraph texzt.

### JPL Mars Space Images
I scraped for the featured space image from the JPL site [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars). Using splinter, I navigated the site and found the image url.

### Mars Weather
I scraped from the Mars Weather Twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page.

### Mars Facts
I scraped facts from the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet.

### Mars Hemisphere
I scraped for high resolution images of Mar's hemispheres from [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

## Step 02 - MongoDB and Flask

I used MongoDB with Flask templating to create a HTML page that displays all the information scraped from the URLs above. I created a scrape function in a Python script called 'scrape_mars.py' and a '/scrape' route that imports the Python script.

I also built a template HTML file called 'index.html' that takes all the mars data and displays them in the appropriate HTML elements. I used Bootstrap to structure my HTML template.

I also used Pymongo for CRUD applications for the database. 

## Finished Result
![mission_to_mars](Images/yuta_mars_screenshot.png)

