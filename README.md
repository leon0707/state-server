### install packages

0. `virtualenv venv`
1. `source venv/bin/activate`
2. `pip install -r requirements.txt`

### run app

0. `python generate_file.py`

1. `export FLASK_ENV=development`

2. `python app.py` or `python app1.py`

### send request

`curl -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/`
