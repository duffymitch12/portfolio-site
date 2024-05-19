from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse

# from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler
from api.AdminHandler import AdminHandler
from api.WebpageDataHandler import WebpageDataHandler
import sqlite3
from flask import g

app = Flask(__name__, static_url_path="", static_folder="frontend/build")
# CORS(app) #comment this on deployment
api = Api(app)
DATABASE = "/database/database.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/", defaults={"path": ""})
def serve_index(path):
    return send_from_directory(app.static_folder, "index.html")


@app.route("/experience", defaults={"path": ""})
def serve_experience(path):
    return send_from_directory(app.static_folder, "experience.html")


@app.route("/projects", defaults={"path": ""})
def serve_projects(path):
    return send_from_directory(app.static_folder, "experience.html")

# Resources: Admin, Client
api.add_resource(HelloApiHandler, "/flask/hello")
api.add_resource(WebpageDataHandler, "/api/webpage-data") # TODO: add more endpoints
api.add_resource(AdminHandler, "/api/admin")  # TODO: add more endpoints


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
