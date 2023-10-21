from flask import Flask, render_template
import requests
from post import *

app = Flask(__name__)
post_objects = []
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()
for blog in data:
    post_object = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    post_objects.append(post_object)


@app.route('/')
def home():
    return render_template("index.html", blogs=data)


@app.route('/post/<int:index>')
def show_blog(index):
    return render_template("post.html", post_objects=post_objects, index=index)


if __name__ == "__main__":
    app.run(debug=True)
