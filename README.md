# InMoov Mini 

InMoov Mini is a scaled down (60%) version of [InMoov](http://inmoov.fr)

The Web Based User Interface is heavily based on the [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

## Usage

Clone this repo
```
git clone https://github.com/bcarroll/inmoov_mini.git
```

Change to the inmoov_mini directory
```
cd inmoov_mini
```

Install the Python pre-requisite modules
```
pip install -r requirements.txt
```

Setup Flask
```
export FLASK_APP=main.py
```

Setup the database
```
flask db init
flask db migrate
flask db upgrade
```

Start the Web User Interface
```
flask run
```

Open a web browser and navigate to http://inmoov_mini:5000
