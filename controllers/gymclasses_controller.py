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

@gymclasses_blueprint.route("/classes/new", methods=["POST"])
def add_class():
    activity_name = request.form['activity_name']
    start_time = request.form['start_time']
    duration = request.form['duration']
    description = request.form['description']
    gymclass = GymClass(activity_name, start_time, duration, description)
    gymclass_repository.save(gymclass)
    return redirect('/classes')    

@gymclasses_blueprint.route("/classes/delete/<id>", methods=["POST"])
def delete_class(id):
    gymclass_repository.delete(id)
    return redirect('/classes')

# @members_blueprint.route("/members/delete/<id>",  methods=["POST"])
# def delete_member(id):
#     member_repository.delete(id)
#     return redirect('/members')

    
