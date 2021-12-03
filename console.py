import pdb

from models.member import Member
from models.gymclass import GymClass
from models.booking import Booking

import repositories.member_repository as member_repository

member_1 = Member('Scott', 'Reoch', 20, 'standard')
member_repository.save(member_1)





