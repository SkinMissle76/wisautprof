from models.tables import GENDER_TABLE_INVERTED
import string
## TODO 
# this expects a soft link to data in . by it may make windows 
# freak out so it needs to change
import random


DATA_DIR = "./data/"
FILE_NAME = "name_to_gender.json"

class Gender:

  data = {}

  def __init__(self):
    # imports
    import json

    f = open(DATA_DIR + FILE_NAME, "r")
    self.data = json.loads(f.read())

    if self.data == {}:
      raise NameError("Something is wrong with the data, it hasn't been fetched")



  def _formatName(self, name):
    # the name needs to be be title cased,
    # and the extra spaces are removed
    formatedName = name.title().strip()
    for p in string.punctuation:
      formatedName = formatedName.replace(p, "")
    words = formatedName.split()

    return self._getBiggerWord(words)

  def _getBiggerWord(self, words):
    lengths = [len(w) for w in words]
    maxlength = max(lengths)
    indexBiggerWord = lengths.index(maxlength)
    return words[indexBiggerWord]




  def getGender(self, name):
    formatedName = self._formatName(name)
    if self.data.has_key(formatedName):
      gender = self.data[formatedName]  # found gender "M", "F" or "U"

      if gender not in GENDER_TABLE_INVERTED.keys():
        raise NameError("Found incorrect gender in data, fix it now!")

      return GENDER_TABLE_INVERTED[gender]
    else:
      r = random.randint(0,100)
      if r < 50:
        return -1
      else:
        return 1


    

