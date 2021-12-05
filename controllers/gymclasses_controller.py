from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gymclass import GymClass
import repositories.gymclass_repository as gymclass_repository

gymclasses_blueprint = Blueprint("gymclasses", __name__)

@gymclasses_blueprint.route("/classes")
def classes():
    gymclasses = gymclass_repository.select_all()
    return render_template("gymclasses/index.html", gymclasses=gymclasses)

@gymclasses_blueprint.route("/classes/<id>")
def show_class(id):
    gymclass = gymclass_repository.select(id)
    members = gymclass_repository.members(gymclass)
    return render_template("gymclasses/show.html", gymclass=gymclass, members=members)

