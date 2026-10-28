import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "pdet_solar_db"

COLLECTIONS = {
    "pdet": "pdet_municipalities",
    "buildings": "building_footprints"
}

EPSG_WGS84 = 4326
