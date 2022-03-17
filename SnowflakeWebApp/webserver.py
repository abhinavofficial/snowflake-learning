# Import packages
from flask import Flask, render_template, request
from snowflakeConnection import sfconnect
import pandas as pd

# Flask Web Application
app = Flask("my website")


@app.route('/')
def homepage():
    cur = cnx.cursor().execute("SELECT COLOR_NAME, COUNT(*) "
                               "FROM COLORS "
                               "GROUP BY COLOR_NAME "
                               "HAVING COUNT(*) > 50 "
                               "ORDER BY COUNT(*) DESC")
    rows = pd.DataFrame(cur.fetchall(), columns=['Color Name', 'Votes'])
    dfhtml = rows.to_html(index=False)
    return render_template('index.html', dfhtml=dfhtml)


@app.route('/submit')
def submitPage():
    return render_template('submit.html')


@app.route('/thanks4submit', methods=["POST"])
def thanks4submit():
    colorname = request.form.get("cname")
    username = request.form.get("uname")
    cnx.cursor().execute("INSERT INTO COLORS(COLOR_UID, COLOR_NAME) " +
                         "SELECT COLOR_UID_SEQ.nextval, '" + colorname + "'")
    return render_template("thanks4submit.html", colorname=colorname, username=username)


@app.route('/coolcharts')
def coolcharts():
    cur = cnx.cursor().execute("SELECT COLOR_NAME, COUNT(*) "
                               "FROM COLORS "
                               "GROUP BY COLOR_NAME "
                               "ORDER BY COUNT(*) DESC")
    data4charts = pd.DataFrame(cur.fetchall(), columns=['color', 'votes'])
    data4chartsJSON = data4charts.to_json(orient='records')
    return render_template("coolcharts.html", data4chartsJSON=data4chartsJSON)


# Snowflake
cnx = sfconnect()


app.run()