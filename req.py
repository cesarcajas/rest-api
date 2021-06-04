import requests

urlPosts = "https://api.stackexchange.com/2.2/posts?pagesize=3&fromdate=1622419200&order=desc&sort=creation&site=stackoverflow"
rP = requests.get(urlPosts)
dataPosts = rP.json()

for post in dataPosts['items']:
    creationDate = [post['creation_date']]
    link = [post['link']]

urlBadges = "https://api.stackexchange.com/2.2/badges?pagesize=10&order=asc&sort=rank&site=stackoverflow"
rB = requests.get(urlBadges)
dataBadges = rB.json()

for badge in dataBadges['items']:
    name = badge['name']
    award_count = badge['award_count']

