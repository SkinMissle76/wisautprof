import sys, os
from models.testDataBuilder import testDataBuilder


if len(sys.argv) > 1:
  path = sys.argv[1]
  print "generating in", path
  btd = testDataBuilder(shelveFilename="female_merge.shelve")
else:
  btdf = testDataBuilder(shelveFilename="female_merge.shelve")
  btdf.run()
  btdm = testDataBuilder(shelveFilename="males_merge.shelve")
  btdm.run()




