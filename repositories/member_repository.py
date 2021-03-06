from pdb import run
from db.run_sql import run_sql
from models.gymclass import GymClass
from models.member import Member
from models.booking import Booking

# save a member function
#   SQL query with placeholder
#   set values
#   run sql function
#   set member id at pos 0
#   return member
def save(member):
    sql = "INSERT INTO members (first_name, last_name, age, membership_type) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [member.first_name, member.last_name, member.age, member.membership_type]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member


# show all members
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['membership_type'], row['id'])
        members.append(member)
    return members

# select member from id
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['age'], result['membership_type'], result['id'])
    return member

# delete member from id
def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# delete all members
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

# show classes booked by member
def gymclasses(member):
    gymclasses = []

    sql = "SELECT gymclasses.* FROM gymclasses INNER JOIN bookings ON bookings.gymclass_id = gymclasses.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gymclass = GymClass(row['activity_name'], row['start_time'], row['duration'], row['description'], row['id'])
        gymclasses.append(gymclass)
    return gymclasses

def update(member):
    sql = "UPDATE members SET (first_name, last_name, age, membership_type) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.age, member.membership_type, member.id]
    run_sql(sql, values)

def remove_bookings_from_member(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


