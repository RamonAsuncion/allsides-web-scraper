![Logo](https://camo.githubusercontent.com/995bca3303dc80891a41e382ab3e6ba27601ed62/68747470733a2f2f64322e616c7465726e6174697665746f2e6e65742f646973742f69636f6e732f616c6c73696465735f3130313336302e706e673f77696474683d3634266865696768743d3634266d6f64653d63726f702675707363616c653d66616c7365)

# Allsides Webscraper

Allsides Webscraper is a web scraper made in Python to parse data from https://www.allsides.com/media-bias/media-bias-ratings.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install what is necessary for the web scraper.

```bash
pip install requests
pip install beautifulsoup4
pip install lxml
pip install rich
```

## Contributing

This project will not be worked on anymore once I have parsed all the data I needed.
However, I will still look at pull requests.

## Usage

python allsides.py

The output will be in a allside.json file.

Find the script's directory, mine was located in: Desktop\Allsides Webscraper and run the script.
![GIF](http://g.recordit.co/LlJ5jP5Pqw.gif)

## Example 
##### ABC News
```json
[{"News Source": "ABC News (Online)", "AllSides Bias Rating": "left-center", "News Media Info": "https://www.allsides.com/news-source/abc-news-media-bias", "Agree": 23795, "Disagree": 13522, "Ratio": "1.760", "Community feedback": "Agree", "News Source Site": "http://abcnews.go.com/", "Established": "6/15/1945", "Owned by": "The Walt Disney Company"}]
```

## License
[![License](http://img.shields.io/:license-mit-blue.svg)](http://mit-license.org)
- [MIT](https://choosealicense.com/licenses/mit/)
