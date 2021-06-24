"""
Flask Server Module
REST API that fetches specific resources from Stack Exchange API.
Author: Cesar Cajas
"""

from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def endpoint_home():
    '''
    First endpoint "Home": Information about all the paths (endpoints) of the API
    '''
    return jsonify(
        {
            'To view "creation_date" and "link" of 3 first/oldest posts from 31/05/21': "/posts",
            'To view The "name" and "award_count" of the 10 first badges': "/badges",
        }
    )


@app.route("/posts")
def endpoint_posts():
    '''
    Requests made to Stack Exchange API ('creation_date' and 'link'), list creation and posting
    '''
    r_posts = requests.get("https://bit.ly/3gScM2o")
    posts_data = r_posts.json()

    list_posts = []
    for post in posts_data["items"]:
        creation_date = [post["creation_date"]]
        link = [post["link"]]
        list_posts.append({"creation_date": creation_date, "link": link})
    return jsonify(list_posts)


@app.route("/badges")
def endpoint_badges():
    '''
    Requests made to Stack Exchange API ('name' and 'award_count'), list creation and posting
    '''
    r_badges = requests.get("https://bit.ly/3zVLH5S")
    badges_data = r_badges.json()

    list_badges = []
    for badge in badges_data["items"]:
        name = [badge["name"]]
        award_count = [badge["award_count"]]
        list_badges.append({"name": name, "award_count": award_count})
    return jsonify(list_badges)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6789, debug=True)
