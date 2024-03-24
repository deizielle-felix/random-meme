from flask import Flask, render_template
from config.config import get_meme

app = Flask(__name__) 
@app.route("/")
def index():
    meme, title, subreddit = get_meme()
    return render_template("index.html", meme=meme, sub=subreddit, title=title)
 
if __name__ == '__main__':
    app.run(debug=True)