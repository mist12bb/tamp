from flask import Flask , request, render_template, redirect, url_for
#from my_data_base import entering_dict, new_enterign, date

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def home():

    return render_template("index.html")

""" @app.route("/show")
def get_entring():
    #entring = entering_dict.copy()
    return render_template("show.html", ed = 'entring')

@app.route("/set", methods = ["GET", "POST"])
def set_new_enitring():
    form = request.form
    #!set_entring = new_enterign
    return render_template("set.html" , form = form, set = 'set_entring', date = date.now()) """

app.run(debug=True, port = 2230)