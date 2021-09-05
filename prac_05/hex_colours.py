"""
CP1404/ Practical
Colour codes in a dictionary
"""
CODE_TO_COLOUR = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "black": "#000000",
                  "cadetblue4": "#53868b",
                  "chartreuse4": "#458b00", "cornflowerblue": "#6495ed", "darkgoldenrod1": "#ffb90f",
                  "darkorchid4": "#68228b",
                  "darkseagreen4": "#698b69"}

print(CODE_TO_COLOUR)

colour_name = input("Colour name: ")
while colour_name != "":
    if colour_name not in CODE_TO_COLOUR:
        print("Colour not available")
        colour_name = input("Colour name: ")
    print(f"The colour code for the colour {colour_name} is {CODE_TO_COLOUR.get(colour_name)}.")
    colour_name = input("Colour name: ")

print("Goodbye!")
