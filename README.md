fetch-food
==========
fetch-food is a back end web-scraper with the purpose to provide current menu data from Nacka Gymnasium's cantina's web page to SkolportlN 2.0. It uses BeautifulSoup along with the built in python HTML parser.


Functionality
=============
1. GET request to http://www.amica.se/nackagymnasium returns the web page containing the menu.
2. Parse the HTML and trim the data to only contain the sought data.
3. Parse the food entries in the menu along with the menu's date-stamp and create structurized entries.
4. POST the entries to http://portaln.se/skola


Components
==========
* fetchfood.py - main
* food.py - contains classes and functions for parsing and handling food entries
* post.py - contains functions for POSTing data to server
* datehelper.py contains helper functions for converting and parsing dates and times
* mail.py - contains functions for sending status/error e-mails
* config.py - config file
* passwd.py - (not on github) contains passwords for POSTing data and sending e-mails
