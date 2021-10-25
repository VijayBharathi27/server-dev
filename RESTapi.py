
# import scrapper.py  importing the filtered json can also be done using dump and load method
from flask import Flask, render_template, url_for, request, session, redirect
# , reqparse, abort, fields, marshal_with
from flask_restful import Api, Resource

jobs = [{"jobTitle": "webdev", "company": "google", "salary": 10000},
        {"jobTitle": "ceo", "company": "fb", "salary": 20000},
        {"jobTitle": "manager", "company": "apple", "salary": 20000}]

app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jobsearch', methods=['GET'])
def jobsearch():
    desired = []
    for item in jobs:
        if jobs["jobTitle"] == request.form['jobTitle']:
            desired.append(item)
    return "hello world"


@app.route('/jobs')
def jobsFilter():
    return ''


if __name__ == '__main__':
    # should be removed during production
    app.run(debug=True)
