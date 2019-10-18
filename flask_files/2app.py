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

# Flask Setup
#################################################
app = Flask(__name__)




# dialect+driver://username:password@host:port/database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/Youtube_project"
db = SQLAlchemy(app)

# Reflect database into  a new model
Base = automap_base()
# Reflect the tables
Base.prepare(db.engine, reflect=True)

trending = Base.Classes.youtube


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (     
        render_template("index.html")
    )

@app.route("/data")
def data():
   sel = [
   Trending.video_id,
   Trending.trending_date,
   Trending.category_id,
   Trending.views,
   Trending.category,
   Trending.likes,
   Trending.dislikes,
   Trending.comments_count
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



