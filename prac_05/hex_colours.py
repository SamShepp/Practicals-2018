"""
CP1404 Practical
Hexadecimal colour lookup
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "blue1": "#0000ff", "BlueViolet": "#8a2be2",
                "Brown": "#a52a2a", "CadetBlue1": "#98f5ff", "Chartreuse1": "#7fff00",
                "Chocolate": "#d2691e", "Coral": "#ff7f50", "CornFlowerBlue": "#6495ed",
                "Cyan1": "#00ffff"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
