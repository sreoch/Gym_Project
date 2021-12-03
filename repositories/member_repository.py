from db.run_sql import run_sql
from models.gymclass import GymClass
from models.member import Member

# save a member function
#   SQL query with placeholder
#   set values
#   run sql function
#   set member id at pos 0
#   return member
def save(member):
    sql = "INSERT INTO members(first_name, last_name, age, membership_type) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [member.first_name, member.last_name, member.age, member.membership_type]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member


# show all members

# select member from id

# delete member from id

# delete all members

# show members in particular class
