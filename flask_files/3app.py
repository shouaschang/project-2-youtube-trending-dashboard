# Import Dependenices 
import numpy as np
import pandas as pd
import sqlalchemy
import psycopg2
import os

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, jsonify, render_template

#Create engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/Youtube_project')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
session = Session(engine)

# Create an app
app = Flask(__name__)

# home page
@app.route("/")
def home():
    return (     
        render_template("index.html")
    )


@app.route("/api/data")
def precipitation():
 def data():
    sel = [
    Base.classes.youtube.video_id,
    Base.classes.youtube.trending_date,
    Base.classes.youtube.category_id,
    Base.classes.youtube.views,
    Base.classes.youtube.category,
    Base.classes.youtube.likes,
    Base.classes.youtube.dislikes,
    Base.classes.youtube.comments_count
    ]
    results = db.session.query(*sel).all()
    season_data = []
    for video_id, trending_date, category_id, views, category, likes, dislikes, comments_count  in results:
        season_dict = {}
        season_dict["video_id"] = video_id
        season_dict["trending_date"] = trending_date
        season_dict["category_id"] = category_id
        season_dict["views"] = views
        season_dict["category"] = category
        season_dict["likes"] = likes
        season_dict["dislikes"] = dislikes
        season_dict["comments_count"] = comments_count
        
        season_data.append(season_dict)
    return jsonify(season_data)
    return jsonify(data)


if __name__ == "_main_":
    app.run(debug=True)