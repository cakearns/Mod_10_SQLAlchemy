from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

app = Flask(__name__)

# connect to database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# home route
@app.route("/")
def home():
    return (
        f"<center><h2>Welcome to the Hawaii Climate Analysis Local API!</h2></center><br/>"
        f"<center><h3>Select from one of the available routes:</h3></center><br/>"
        f"<center>/api/v1.0/precipitation</center><br/>"
        f"<center>/api/v1.0/stations</center><br/>"
        f"<center>/api/v1.0/tobs</center><br/>"
        f"<center>/api/v1.0/temps/<start>/<end></center>"

    )

# /api/v1.0/precipitation route


@app.route("/api/v1.0/precipitation")
def precip():
    # return the previous year's precipation as a json

    # Calculate the date one year from the last date in data set.
    previousYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
# previousYear

# Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).filter(
        Measurement.date >= previousYear).all()
    session.close()

# dictionary with the date as the key and the precipitation (prcp) as the value
    precipitation = {date: prcp for date, prcp in results}
# convert to a json
    return jsonify(precipitation)

# /api/v1.0/stations route


@app.route("/api/v1.0/stations")
def stations():
    # show list of stations
    # Perform a query to retrieve the names of the stations
    results = session.query(Station.station).all()
    session.close()

    stationList = list(np.ravel(results))

# convert to a json and display
    return jsonify(stations=stationList)

# /api/v1.0/tobs route


@app.route("/api/v1.0/tobs")
def temperatures():
    # return the previous year temperatures
    # Calculate the date one year from the last date in data set
    previousYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
# previous year

# Perform a query to retrieve the names of the temperatures fromt eh most active station form the past year
    results = session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.station == 'USC00519281').filter(Measurement.date >= previousYear).all()

    session.close()

    temperatureList = list(np.ravel(results))

    # return the list of the temperatures
    return jsonify(temperatureList=temperatureList)

# /api/v1.0/start/end and api/v1.0/start`routes


@app.route("/api/v1.0/temps/<start>")
@app.route("/api/v1.0/temps/<start>/<end>")
def dateStats(start=None, end=None):

    # select statement
    selection = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.ave(Measurement.tobs)]
        

    if not end:

        startDate = dt. datetime.strptime(start, "%m%d%Y")

        results = session.query(*selection).filter(Measurement.date >= startDate).all
            
        session.close()

        temperatureList = list(np.ravel(results))

        # return the list of the temperatures
        return jsonify(temperatureList)

    #else:
    startDate = dt.datetime.strptime(start, "%m%d%Y")
    print("print start date",startDate)
    endDate = dt.datetime.strptime(end, "%m%d%Y")
    print("print end date",endDate)

    results = session.query(*selection).filter(Measurement.date >= startDate).filter(Measurement.date >= startDate).filter(Measurement.date <= endDate).all()
        

    session.close()

    temperatureList = list(np.ravel(results))
    return jsonify(temps=temperatureList)


# app launch
if __name__ == '__main__':
    app.run()
