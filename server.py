from flask import Flask, jsonify
import requests
from req import creationDate, link, name, award_count, dataBadges, dataPosts

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"/posts":"First endpoint: creation_date and link", "/badges" : "Second endpoint: name and award_count"})

@app.route("/posts")
def posts():
    return jsonify({'creation_date': creationDate, 'link': link})

@app.route("/badges")
def badges():
    return jsonify({'name': name, 'award_count': award_count})

