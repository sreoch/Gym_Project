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

# select gymclass by id

# show members attending a gymclass

# add member to class? -TODO
