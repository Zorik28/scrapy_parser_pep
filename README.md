# scrapy_parser_pep

### Description
The parser can perform the following functions:
1. Parses PEP number, name and status and saves to .csv file
2. Counts the number of all pep documents, sums the number of documents for each category


### Technology
- Python 3.9.6
- Scrapy 2.5.1


### Project run on local server
1. Install and activate the virtual environment:
```py -m venv venv```
```. venv/Scripts/activate```

2. Install dependencies from requirements.txt:
```py -m pip install --upgrade pip```
```pip install -r requirements.txt```

4. Run the spider!:
```scrapy crawl pep```


### Example

The output of the parser in .csv:

"Status","Quantity"
"Accepted","48"
"Active","31"
"April Fool!","1"
"Deferred","37"
"Draft","27"
"Final","269"
"Rejected","121"
"Superseded","20"
"Withdrawn","56"
"Total","610"



#### Author
Karapetian Zorik   
Russian Federation, St. Petersburg, Kupchino.