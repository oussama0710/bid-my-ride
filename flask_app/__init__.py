from flask import Flask

app = Flask(__name__)
app.secret_key = "adamcheater"

DB = "bid_my_ride_schema"