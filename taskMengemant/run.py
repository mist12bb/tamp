import bundler as bl
from flask import Flask, request, render_template

app = Flask(__name__)

tasks = bl.tasks


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get", methods=["GET", "POST"])
def get():
    modefy_task = bl.modefy_task

    if request.method == 'post':
        pirnt(true)

    form = request.form
    return render_template("box.html", tasks=tasks, modefy_task=modefy_task, form=form, str=str)


@app.route("/tasks")
def tasksApp():

    return render_template("tasks.html", tasks=tasks)


app.run(port=1581, debug=True, host="127.0.0.1")
