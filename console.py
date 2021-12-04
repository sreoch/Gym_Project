import pdb

from models.member import Member
from models.gymclass import GymClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gymclass_repository as gymclass_repository

member_repository.delete_all()
gymclass_repository.delete_all()

member_1 = Member('Scott', 'Reoch', 20, 'standard')
member_repository.save(member_1)

member_2 = Member('Matthew', 'Robson', 30, 'pro')
member_repository.save(member_2)

gymclass_1 = GymClass('Yoga', '13:00', 30, 'Intense Yoga session!')
gymclass_repository.save(gymclass_1)





pdb.set_trace()


