# werkix-api

News filter API developed on Fastapi framework.

## Description

wekix api is a simple api that fetches news article from GNews API and implements simple filtering methods.

## Getting Started

### Dependencies

* Python 3.5+, Ubuntu 18+(Optional), Windows 10+ (Optional)

### Installing

* Clone the project
* Generate Gnews apikey by registering an account on [Gnews](https://gnews.io/)
* Change ***apikey = "GNews api_key here"*** with your API Key in main.py
* Install the following python library on your computer running Linux or Windows by running the commands 
```
pip3 install fastapi

pip3 install "uvicorn[standard]"

pip3 install urllib3
```

### Executing program
* From the project folder, run the following command to test the API
```
uvicorn main:app --reload
```

* Usually the API will run on default port 8000.
* Type [http://localhost:8000/docs](http://localhost:8000/docs) on the browser for a graphical documentation of the API and testing 

## Authors
[Joel Kumwenda](https://www.linkedin.com/in/joel-kumwenda/)
