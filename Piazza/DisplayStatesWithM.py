"""
Question -
Display all states starting with the letter M

states = [ 'Alabama','Alaska','Arizona','Arkansas',
'California','Colorado','Connecticut','Delaware','Florida',
'Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas',
'Kentucky','Louisiana','Maine','Maryland','Massachusetts',
'Michigan','Minnesota','Mississippi','Missouri','Montana',
'Nebraska','Nevada','New Hampshire','New Jersey','New Mexico',
'New York','North Carolina','North Dakota','Ohio','Oklahoma',
'Oregon','Pennsylvania','Rhode Island','South Carolina',
'South Dakota','Tennessee','Texas','Utah','Vermont','Virginia',
'Washington','West Virginia','Wisconsin','Wyoming' ]
"""

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas',
          'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
          'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
          'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
          'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
          'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


# Code -

def check(elements):
    for checkAlpha in elements:
        if checkAlpha == "M":
            return checkAlpha
        else:
            return 0


for Iterating in states:
    checkingReturn = check(Iterating)
    if checkingReturn != 0:
        print(Iterating)


"""
Answer - 

Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
"""

