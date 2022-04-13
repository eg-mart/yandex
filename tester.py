from db_session import create_session
from Jobs import Jobs
from User import User

s = create_session()
usr = User()
job = Jobs()
job.team_leader = usr
