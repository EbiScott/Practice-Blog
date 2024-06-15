
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient



def create_app():
    app = Flask(__name__)
    client = MongoClient()
    app.db = client.microblog

    @app.route("/", methods=["POST", "GET"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y- %m- %d")
            entries.append((entry_content, formatted_date)) 
            app.db.entries.insert({"content": entry_content, "date": formatted_date})


        entries_with_date = [
            (
                entry["content"],
                entry["date"], 
                datetime.datetime.strptime(entry["date"], "%Y- %m- %d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
        
        return render_template("home.html", entries=entries_with_date)


    if __name__ == "__main__":
        app.run( debug=True )