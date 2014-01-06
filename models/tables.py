
GENDER_TABLE = {
    -1 : "M",
     0 : "U", # unisex or unknown
     1 : "F"
}

GENDER_TABLE_INVERTED = {
  "M" : -1,
  "U" :  0,
  "F" :  1
}

def AGE_REAL_TO_SYS(sysAge):
  if (sysAge > 1 or sysAge < -1):
    raise NameError("yo watch out dude, sysAge must be between -1 and 1, yours is " + sysAge)
  return ((sysAge*50)+50)

def AGE_SYS_TO_REAL(realAge):
  if (realAge > 100 or realAge < 0):
    raise NameError("yo watch out dude, realAge must be between 0 and 100, yours is %s" % realAge)
  return ((realAge-50)/50)

# id -> county
LOCATIONS_TABLE = {
    1  : "Bedfordshire",
    2  : "Berkshire",
    3  : "Buckinghamshire",
    4  : "Cambridgeshire",
    5  : "Cheshire",
    6  : "Cornwall",
    7  : "Cumbria",
    8  : "Derbyshire",
    9  : "Devon",
    10 : "Dorset",
    11 : "Durham",
    12 : "Durham/North Yorkshire",
    13 : "East Riding of Yorkshire",
    14 : "East Sussex",
    15 : "Essex",
    16 : "Gloucestershire",
    17 : "Greater London",
    18 : "Greater Manchester",
    19 : "Hampshire",
    20 : "Herefordshire",
    21 : "Hertfordshire",
    22 : "Isle of Wight",
    23 : "Kent",
    24 : "Lancashire",
    25 : "Leicestershire",
    26 : "Lincolnshire",
    27 : "Merseyside",
    28 : "Norfolk",
    29 : "North Yorkshire",
    30 : "Northamptonshire",
    31 : "Northumberland",
    32 : "Nottinghamshire",
    33 : "Oxfordshire",
    34 : "Rutland",
    35 : "Shropshire",
    36 : "Somerset",
    37 : "South Yorkshire",
    38 : "Staffordshire",
    39 : "Suffolk",
    40 : "Surrey",
    41 : "Tyne and Wear",
    42 : "Warwickshire",
    43 : "West Midlands",
    44 : "West Sussex",
    45 : "West Yorkshire",
    46 : "Wiltshire",
    47 : "Worcestershire"
}
# country -> id
LOCATIONS_TABLE_INVERTED = {v:k for k, v in LOCATIONS_TABLE.items()}


EDUCATION_TABLE = {
    1 : "Low",
    2 : "Mid", 
    3 : "High"
}

EDUCATION_TABLE_INVERTED = {
    "Low" : 1,
    "Mid" : 2, 
    "High" : 3
}

EMOTIONS_TABLE = {
    1 : "Joy", 
    2 : "Trust", 
    3 : "Fear",
    4 : "Surprise",
    5 : "Sadness",
    6 : "Disgust",
    7 : "Anger",
    8 : "Anticipation"
}

POLARITY_TABLE = {
    -1 : "Negative", 
     0 : "Objective", 
     1 : "Positive"
}
