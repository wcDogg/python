# Python CSV, JSON, and Markdown

OS agnostic functions to convert CSV and JSON files to other formats using default modules - specifically, no Pandas. 

* CSV to Markdown table (with bold first row and col options)
* CSV to JSON records (list of dictionaries)
* CSV to JSON records with select columns
* CSV to JSON keyed dictionary (simple nested dictionaries)
* JSON records to CSV
* JSON simple nested to CSV

`configure.py` is how I define directory and file paths - using it is optional. 

## About JSON

When converting between CSV and JSON in either direction, there are 2 JSON formats you can use - records or simple nested. Examples below. 

IMPORTANT: For JSON to CSV, each record / nested dictionary must contain all keys else values will not map to their correct columns. 

JSON records format is equivalent to a Python list of dictionaries: 
```
[
    {
        "character": "1",
        "telephony": "One",
        "phonic": "WUN",
        "morse": "* - - - -"
    },
    {
        "character": "2",
        "telephony": "Two",
        "phonic": "TOO",
        "morse": "* * - - -"
    }
]
```

JSON simple nested format is equivalent to a Python dictionary where each key contains a simple dictionary:
```
{
    "AF": {
        "Country Name": "Afghanistan",
        "ISO2": "AF",
        "ISO3": "AFG",
        "Top Level Domain": "af",
        "FIPS": "AF",
        "ISO Numeric": "004"
    },
    "AL": {
        "Country Name": "Albania",
        "ISO2": "AL",
        "ISO3": "ALB",
        "Top Level Domain": "al",
        "FIPS": "AL",
        "ISO Numeric": "008"
    }
}
```