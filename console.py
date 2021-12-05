import pdb
from models import booking

from models.member import Member
from models.gymclass import GymClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
member_repository.delete_all()
gymclass_repository.delete_all()

member_1 = Member('Scott', 'Reoch', 20, 'standard')
member_repository.save(member_1)
member_2 = Member('Matthew', 'Robson', 30, 'pro')
member_repository.save(member_2)

gymclass_1 = GymClass('Yoga', '13:00', 30, 'Intense Yoga session!')
gymclass_repository.save(gymclass_1)

gymclass_2 = GymClass('Cardio', '15:00', 60, 'Running and cycling!')
gymclass_repository.save(gymclass_2)

booking_1 = Booking(member_1, gymclass_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_2, gymclass_2)
booking_repository.save(booking_2)

booking_3 = Booking(member_1, gymclass_2)
booking_repository.save(booking_3)

pdb.set_trace()


