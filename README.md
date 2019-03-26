# CPP Reddit Bot

This is a Reddit bot for the Cal Poly Pomona subreddit.  Its goal
is to provide users information about CPP's organizations and/or
events through queries like

`!CPPbot genre Technology`

The bot will be built in Python using a Reddit API wrapper called
praw (Python Reddit API Wrapper). The bot will be gathering data
from myBar through the use of a web scraping tool called Scrapy.

For more information on PRAW and Scrapy as well as installing
Python, see the links below

### Python
https://www.python.org/downloads

### PRAW
https://praw.readthedocs.io/en/latest

### Scrapy
http://doc.scrapy.org/en/latest/intro/overview.html

Also, I recommend setting up a virtual environment (virtualenv)
for creating and running Python projects

### Virtualenv
https://packaging.python.org/guides/installing-using-pip-and-virtualenv

### Tasks

For those who would like to contribute, here are some tasks to work on for the bot:
* Parsing bot queries (e.g. `!CPPbot genre technology` `!CPPbot search food` `!CPPbot category religious`)
* Making requests on myBAR site
* Posting results on Reddit
* Hosting/running the project on an external server
