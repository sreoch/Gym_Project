from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    members = member_repository.select_all()
    gymclasses = gymclass_repository.select_all()
    return render_template("/bookings/index.html", members=members, gymclasses=gymclasses)

@bookings_blueprint.route("/bookings", methods=["POST"])
def add_booking():
    member_id = request.form['member_id']
    gymclass_id = request.form['gymclass_id']
    member = member_repository.select(member_id)
    gymclass = gymclass_repository.select(gymclass_id)
    booking = Booking(member, gymclass)
    booking_repository.save(booking)
    return redirect('/bookings')

@bookings_blueprint.route("/classes/remove/<id>", methods=["POST"])
def remove_class_booking(id):
    booking = booking_repository.select(id)
    booking_repository.delete(id)
    return redirect('/bookings', booking=booking)