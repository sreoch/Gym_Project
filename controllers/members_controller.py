from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/new", methods=["POST"])
def add_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    membership_type = request.form['membership_type']
    member = Member(first_name, last_name, age, membership_type)
    member_repository.save(member)
    return redirect('/members')

@members_blueprint.route("/members/show/<id>")
def view_member(id):
    member = member_repository.select(id)
    gymclasses = member_repository.gymclasses(member)
    return render_template("members/show.html", member=member, gymclasses=gymclasses)

@members_blueprint.route("/members/edit/<id>")
def edit_member(id):
    member = member_repository.select(id)
    gymclasses = member_repository.gymclasses(member)
    return render_template("members/edit.html", member = member, gymclasses=gymclasses)
    
@members_blueprint.route("/members/edit/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    membership_type = request.form['membership_type']
    member = Member(first_name, last_name, age, membership_type, id)
    member_repository.update(member)
    return redirect('/members')

@members_blueprint.route("/members/remove_member/<id>",  methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect('/members')

    
