# scraping is triggered when user goes to the relative path "/jobsearch"
# ,render_template, url_for,  session, redirect,
from flask import Flask, jsonify, request
# , reqparse, abort, fields, marshal_with
#from flask_restful import Api , Resource
from scraper import scraping

app = Flask(__name__)


@app.route('/jobsearch', methods=['POST'])
def jobsearch():

    data = scraping()
    return jsonify(data)


@app.route('/jobs', methods=['GET'])
def jobs():
    return 'html render'  # render_template('index.html')


if __name__ == '__main__':
    # should be removed during production
    app.run(host="localhost", debug=True)
