from pyquery import PyQuery

class Linkedin:

  def getProfile(self, url):
    doc = self._getDocument(url)
    return {
      "url"                 : url,
      "fullName"            : self._getFullName(doc),
      "firstName"           : self._getFirstName(doc),
      "lastName"            : self._getLastName(doc),
      "education"           : self._getEducation(doc),
      "descriptionSummary"  : self._getDescriptionSummary(doc),
      "locality"            : self._getLocation(doc),
      "industry"            : self._getIndustry(doc),
      "skills"              : self._getSkills(doc)
    }

  def _getDocument(self, url):
    #page = urllib2.urlopen(url)
    #return BeautifulSoup(page)
    PQ = PyQuery(url = url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'})
    return PQ

  def _getEducation(self, doc):
    schoolNamesDOM =  doc(".position.education").find(".summary")
    schoolNames = [schoolNamesDOM.eq(i).text() for i in range(0, len(schoolNamesDOM))]

    periodStartsDOM = doc(".position.education").find(".dtstart")
    periodEndsDOM =  doc(".position.education").find(".dtend")
    periodStarts = [periodStartsDOM.eq(i).attr("title") for i in range(0, len(periodStartsDOM))]
    periodEnds = [periodEndsDOM.eq(i).attr("title") for i in range(0, len(periodEndsDOM))]

    education = []
    for i in range(0, len(schoolNames)):
      position = {
        "school" : schoolNames[i],
        "period" : {"start" : periodStarts[i], "end" : periodEnds[i] }
      }
      education.append(position)
    return education

  def _getDescriptionSummary(self, doc):
    descriptionSummaryDOM = doc("#profile-summary .description.summary")
    return descriptionSummaryDOM.text()

  def _getLocation(self, doc):
    locationDOM = doc(".locality")
    return locationDOM.text()

  def _getIndustry(self, doc):
    industryDOM = doc(".industry")
    return industryDOM.text()

  def _getFullName(self, doc):
    fullNameDOM = doc(".full-name")
    return fullNameDOM.text()

  def _getFirstName(self, doc):
    firstNameDOM = doc(".given-name")
    return firstNameDOM.text()

  def _getLastName(self, doc):
    lastNameDOM = doc(".family-name")
    return lastNameDOM.text()

  def _getSkills(self, doc):
    skillsDOM = doc(".skills .competency")
    skills = [skillsDOM.eq(i).text() for i in range(0, len(skillsDOM))]
    return skills

