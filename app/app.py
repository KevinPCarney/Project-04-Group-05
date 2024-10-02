from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper
import json

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/machine_learning")
def machine_learning():
    return render_template("machine_learning.html")

@app.route("/tableau1")
def tableau1():
    return render_template("tableau1.html")

@app.route("/tableau2")
def tableau2():
    return render_template("tableau2.html")

@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/works_cited")
def works_cited():
    return render_template("works_cited.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    # parse
    Weather = (content["Weather"])
    Roadway_Type = (content["Roadway_Type"])
    Model_Year = int(content["Model_Year"])
    Passengers_Belted = int(content["Passengers_Belted"])
    Time_of_Day = content["Time_of_Day"]
    Speed_Limit = int(content["Speed_Limit"])
    Roadway_Surface = content["Roadway_Surface"]
   
    preds = modelHelper.makePredictions(Weather, Roadway_Type, Model_Year, Passengers_Belted, Time_of_Day,
                       Speed_Limit, Roadway_Surface)
    return(jsonify({"ok": True, "prediction": preds}))


 
#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
