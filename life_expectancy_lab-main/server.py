# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    canData = []
    for x in data["Canada"].values():
        canData.append(x)
    usaData = []
    for x in data["United States"].values():
        usaData.append(x)
    mexData = []
    for x in data["Mexico"].values():
        mexData.append(x)
    canLine = []
    for i in range(len(canData) - 1):
        canLine.append([canData[i], canData[i + 1]])
    usaLine = []
    for i in range(len(usaData) - 1):
        usaLine.append([usaData[i], usaData[i + 1]])
    mexLine = []
    for i in range(len(mexData) - 1):
        mexLine.append([mexData[i], mexData[i + 1]])
    ages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    years = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
    return render_template("index.html", years=data["Canada"].keys(),Canada=canLine,Us=usaLine,Mex=mexLine,ages=ages,years2=years)
    
@app.route('/year')
def year():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    year = request.args.get("year")
    Mex = 90 - ((data["Mexico"][year]) - 50) * 2
    Canada = 90 - ((data["Canada"][year]) - 50) * 2
    Us = 90 - ((data["United States"][year]) - 50) * 2
    years = [["Mexico", data["Mexico"][year]],["Canada", data["Canada"][year]],["United States", data["United States"][year]],
    ]
    return render_template(
        "year.html", year=year, Mex=Mex, Us=Us, Canada=Canada, years=years
    )


app.run(debug=True)
