
# Mod_10_SQLAlchemy

* I connected to the SQl database called hawaii.sqlite

* I performed SQl queries using an engine = create_engine("sqlite:///hawaii.sqlite"

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

* I created python classes and objects into a new model using Base = automap_base() and Base.prepare(engine, reflect=True); Measurement = Base.classes.measurement; Station = Base.classes.station; 

I linked from Python to the database session = Session(engine)

* Use the SQLAlchemy Inspector to view table names in the database. Plotted results. 
I used:
ResultDF.plot(x='date', y='precipitation', rot=90)
plt.xlabel('Date')
plt.ylabel('Inches of Precipitation')          
plt.show()


* Use Flask to create and run a server.
used app = Flask(__name__)


* Define endpoints using Flask's `@app.route` decorator.
Used: @app.route("/api/v1.0/precipitation"); @app.route("/api/v1.0/stations"); @app.route("/api/v1.0/tobs"); @app.route("api/v1.0/start"); and
@app.route("api/v1.0/start/end")
 

# Calculate the date one year from the last date in data set.
previousYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#previousYear

# Perform a query to retrieve the data and precipitation scores
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= previousYear).all().\
filter(Measurement.date >=previousYear).all

* Extract query-variable path values from get requests.
results = session.query(Station.station).all()
    session.close()
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= previousYear).all()
           results = session.query(*selection).filter(Measurement.date >= startDate)
            .filter(Measurement.date >= startDate)\
            .filter(Measurement.date <= endDate).all()    


* Return JSONified query results from API endpoints.
 return jsonify(precipitation)
 return jsonify(stationList)
 return jsonify(temperatureList)
 

