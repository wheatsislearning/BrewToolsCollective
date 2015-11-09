print("THIS IS A PROGRAM TO CONVERT EXTRACT TO ALLGRAIN!")

#EXTRACT TO ALL-GRAIN
#Amount of liquid malt extract x 1.23 - amount of pale malt
#(example: 6.6 lbs. liquid malt extract x 1.23 = 8.1 lbs. pale malt)
#Amount of dry malt extract x 1.45 - amount of pale malt
#(example: 5 lbs. dry malt extract x 1.45 = 7.25 lbs. pale malt)
#Amount of liquid wheat extract x 1.07 - amount of wheat malt
#(example: 6.6 lbs. wheat extract x 1.07 = 7 lbs. wheat malt)

LME =input("how much LME (in pounds) is used?")
DME =input("how much DME (in pounds) is used?")
LWE =input("how much Liquid Wheat Extract is used?")

GrainLME = float(LME) * 1.23
GrainDME = float(DME) * 1.45
GrainLWE = float(LWE) * 1.07
print("\n")
print("Your calculated amount of malty grains from LME is " + str(float(GrainLME)) + " pounds")
print("\n")
print("Your calculated amount of delcious oats from DME is " + str(float(GrainDME)) + " pounds")
print("\n")
print("Your calculated amount of wheaty fermentables from LWE is " + str(float(GrainLWE)) + " pounds")
print("\n")
print(GrainLME)
print(GrainDME)
print(GrainLWE)

