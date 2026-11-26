from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():

    if request.method=="POST":                                                     
        name=request.form["name"]
        email=request.form["email"]
        connecton=sqlite3.connect("database.db")
        cursor=connecton.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
        """)
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
        connecton.commit()
        connecton.close()

        return render_template("thankyou.html")
        
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)