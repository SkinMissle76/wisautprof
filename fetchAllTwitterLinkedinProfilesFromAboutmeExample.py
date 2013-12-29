from models.AbouemeDB import AboutmeDB
db = AboutmeDB()
interestingUsers = db.getAllUsersWithTwitterAndLinkedinProfiles()
print len(interestingUsers)






