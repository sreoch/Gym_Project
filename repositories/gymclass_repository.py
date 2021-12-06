from pdb import run
from db.run_sql import run_sql
from models.gymclass import GymClass
from models.member import Member

# save a gymclass function
def save(gymclass):
    sql = "INSERT INTO gymclasses (activity_name, start_time, duration, description) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [gymclass.activity_name, gymclass.start_time, gymclass.duration, gymclass.description]
    results = run_sql(sql, values)
    gymclass.id = results[0]["id"]
    return gymclass

# select all gymclasses
def select_all():
    gymclasses = []

    sql = "SELECT * FROM gymclasses"
    results = run_sql(sql)
    
    for row in results:
        gymclass = GymClass(row['activity_name'], row['start_time'], row['duration'], row['description'], row['id'])
        gymclasses.append(gymclass)
    return gymclasses

# select gymclass by id
def select(id):
    gymclass = None
    sql = "SELECT * FROM gymclasses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gymclass = GymClass(result['activity_name'], result['start_time'], result['duration'], result['description'], result['id'])
    return gymclass

# delete all
def delete_all():
    sql = "DELETE FROM gymclasses"
    run_sql(sql)

# delete by id 
def delete(id):
    sql = "DELETE FROM gymclasses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

# show members in class? -TODO
def members(gymclass):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE gymclass_id = %s"
    values = [gymclass.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['membership_type'], row['id'])
        members.append(member)

    return members

