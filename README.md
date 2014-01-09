wisautprof
==========

Web information systems - Authorship	profiling

# Folder structure
- `DELIVERABLES/` contains 
  - automatically labeled data (separated in to sets, one for testing(1/3) the rest for training(2/3))
  - manually labled data
  - Report 

- `classifiers/` contains the classifiers used to fill in the information about our profiles
  - most are rule base and implement by hand
  - some use external APIs such as ageanalyzer.com or lymbix for age and sentiment detection
- `data/` contains all our data collections (either in .)son or .shelve)
-  `models` is what interacts with the `.shelve` files in `data/` and  structure the information


To rebuild the dataset, you need to run `python buildDataSetsForServer_new.py`. It will 
generate all the data and put it inside `data/test_data/`, than you can copy this new data in 
`DELIVERABLES/auto_labeled_data/`




## dependencies
- python-twitter: https://github.com/bear/python-twitter
- lymbix https://github.com/lymbix/Python-wrapper
- PyQuery http://pythonhosted.org/pyquery/api.html
- nltk http://nltk.org/
- ageanalyzer.com



