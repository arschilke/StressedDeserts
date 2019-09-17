# StressedDeserts

## Requirements to run: 
npm/node

## How to run: 
npm install

node server.js

**Note** If the Google map gives you a blue screen then refresh the page. Sometimes too many requests slow the api and processing process. We are processing ~25000 data points.

## Inspiration
During the HopHacks Hackathon, our team was considering the millions of families in the US who live in areas known as “food deserts”.

## What it does
Food deserts are regions in which affordable access to groceries is limited. In order to raise awareness, we scraped hundreds of webpages to produce a dataset of 24,300 grocery stores across the country and a dataset of 12,000 food banks across America. Through our web app, our users will be able to see food desert areas and find food banks that support those who need it most.

## How we built it
We used Python's Beautiful Soup library to scrap the hundreds of chains and locations listed on www.supermarketpage.com as well as www.feedingamerica.org/find-your-local-foodbank and foodpantries.org. After cleaning and sorting the raw HTML, we used Google's geocoding API to look up the latitude and longitude of each address of our grocery store and food bank data points.

In order to display our data set through a web application, we embedded a heatmap of the store data and markers of the foodbanks with the Google Maps API.

## Challenges we ran into
Web scraping is a picky, messy business. So is learning new documentation on the fly. Through teamwork and dedication, we were able to clean the data to an acceptable standard, although long hours were spent fiddling with types and IndexErrors.

Also, our incredibly large dataset took an incredibly long time to process.

## Accomplishments that we're proud of
We are proud of how well our team worked together.

## What we learned
We learned how to use Python Beautiful Soup, the frustration of web crawling (that website were not built to be crawled but we did it anyway). Lastly, API calls are always expensive.

## What's next for StressedDesert
We would like to spend more time improving data relevance and quality. Although we found ample information to be gathered, our next steps include updating and validating the data.

## Built With
python, javascript, html, css, node.js, express.js, google-maps, google-geocoding, beautiful-soup
