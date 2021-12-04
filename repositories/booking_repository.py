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
