from flask import Flask, render_template

app = Flask(__name__)      # <-- create app object

@app.route("/editor")      # <-- define a route
def editor():              # <-- function which sends
                           #     data to the client
    return render_template("editor.html")   # <-┐
                            #     template sent to client