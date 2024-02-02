#CS175L
#Lynda Levy
#resturaunt

vegetarian = input("Is anyone in your party vegetarian? ")
vegan = input("Is anyone in your party vegan? ")
gluten = input("Is anyone in your party gluetn-free? ")
    
print(" ")
print("Here are your resturaunt choices.")

if (vegetarian == "no") and (vegan == "no") and (gluten == "no"):
    print("Joe's Gournet Burgers")

if (vegan == "no") and (gluten == "no"):
    print("Mama's Fine Italian")
    
if vegan == "no":
    print("Main Street Pizza Company")
    
print("Corner Cafe")
print("The Chef's Kitchen")

