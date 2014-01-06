from classifiers.Education import OkcupidEducation

test = [
  "High school",
  "graduated from law school",
  "dropped out of law school",
  "Graduated college/university",
  "Working on college/university",
  "Dropped out of space camp",
  "Graduated from masters program"
]

ec = OkcupidEducation()
for s in test:
  print s, ec.getEducationLevelFromString(s)
