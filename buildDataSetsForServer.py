import sys, os
from models.testDataBuilder import testDataBuilder


if len(sys.argv) > 1:
  path = sys.argv[1]
  print "generating in", path
  btd = testDataBuilder(shelveFilename="female_merge.shelve")
else:
  btd = testDataBuilder(shelveFilename="female_merge.shelve")

btd.run()



