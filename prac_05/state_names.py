"""
CP1404 Practical
State names in a dictionary
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
               "WA": "Western Australia", "ACT": "Australian Capital Territory", "VIC": "Victoria",
               "TAS": "Tasmania"}

state = input("Enter state abbreviation: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid abbreviation")
    state = input("Enter abbreviation: ").upper()

