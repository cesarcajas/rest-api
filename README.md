# REST-API I2CAT v2
REST-API I2CAT v2 fetches specific resources from [Stack Exchange API](stackexchange.com/docs), such as:

* The “creation_date” and “link” of the 3 first/oldest posts from 31/5/2021.
* The “name” and “award_count” of the 10 first badges shown when sorting by rank and ordering in ascending manner.

# Installation
## Prerequisites and first try.
This API is based on python (sourcecode/server.py) and can be run on Linux or Windows.

The API uses [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/) server and [requests](https://docs.python-requests.org/en/master/) library to work properly (requirements).

This version is developed to run with [Docker](docker.com). To try it you need to execute it as follows:

```
docker run -ti -p 6789:6789 serverapp
```
With this command you can expose the port 6789 to be public and run it as the same port as is working into the container.

# End Points
## Home endpoint
In this endpoint we can see the paths that we can access to see the different queries. We have set 2 endpoints:

* /posts
* /badges

You should see something like this:

```
{
  "To view \"creation_date\" and \"link\" of 3 first/oldest posts from 31/05/21": "/posts", 
  "To view The \"name\" and \"award_count\" of the 10 first badges": "/badges"
}

```

## Posts endpoint
Accessing into this path we can show the “creation_date” and “link” of the 3 first/oldest posts from 31/5/2021.

You should see something like this:
```
[
  {
    "creation_date": [
      1622419218
    ], 
    "link": [
      "https://stackoverflow.com/q/67766658"
    ]
  }, 
  {
    "creation_date": [
      1622419223
    ], 
    "link": [
      "https://stackoverflow.com/a/67766659"
    ]
  }, 
  {
    "creation_date": [
      1622419239
    ], 
    "link": [
      "https://stackoverflow.com/a/67766660"
    ]
  }
]

```

## Badges endpoint
Accessing into this path we can show the “name” and “award_count” of the 10 first badges shown when sorting by rank and ordering in ascending manner.

You should see something like this:

```
[
  {
    "award_count": [
      3
    ], 
    "name": [
      "amazon-s3"
    ]
  }, 
  {
    "award_count": [
      5
    ], 
    "name": [
      "security"
    ]
  }, 
  {
    "award_count": [
      3
    ], 
    "name": [
      "makefile"
    ]
  }, 
  {
    "award_count": [
      1
    ], 
    "name": [
      "tinymce"
    ]
  }, 
  {
    "award_count": [
      4
    ], 
    "name": [
      "jframe"
    ]
  }, 
  {
    "award_count": [
      4
    ], 
    "name": [
      "wordpress"
    ]
  }, 
  {
    "award_count": [
      1
    ], 
    "name": [
      "uiviewcontroller"
    ]
  }, 
  {
    "award_count": [
      5
    ], 
    "name": [
      "ansible"
    ]
  }, 
  {
    "award_count": [
      15
    ], 
    "name": [
      "vue.js"
    ]
  }, 
  {
    "award_count": [
      1
    ], 
    "name": [
      "asp.net-mvc-2"
    ]
  }
]
```
# Code
## Setting up the Server with Flask
```
from flask import Flask, jsonify

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6789, debug=True)
```

## Requests
```
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
```
