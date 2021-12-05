from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gymclass import GymClass
import repositories.gymclass_repository as gymclass_repository

gymclasses_blueprint = Blueprint("gymclasses", __name__)

@gymclasses_blueprint.route("/classes")
def classes():
    gymclasses = gymclass_repository.select_all()
    return render_template("gymclasses/index.html", gymclasses=gymclasses)