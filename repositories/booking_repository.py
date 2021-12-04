from pdb import run

from db.run_sql import run_sql

from models.gymclass import GymClass
from models.member import Member
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository

# add a booking
def save(booking):
    sql = "INSERT INTO bookings (member_id, gymclass_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.gymclass.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

# select all
def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        location = gymclass_repository.select(row['gymclass_id'])
        booking = Booking(member, location, row['id'])
        bookings.append(booking)
    return bookings

def gymclass(booking):
    sql = "SELECT * FROM gymclasses WHERE id = %s"
    values = [booking.gymclass.id]
    results = run_sql(sql, values)[0]
    gymclass = GymClass(results['activity_name'], results['start_time'], results['duration'], results['description'])
    return gymclass

def member(booking):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [booking.member.id]
    results = run_sql(sql, values)[0]
    member = Member(results['first_name'], results['last_name'], results['age'], results['membership_type'])
    return member

# delete all bookings
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

# delete booking by id
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)