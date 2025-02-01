#Write a program to solve a classic puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

heads=35
legs=94
def r_c():
    rab=(legs-2*heads)/2
    chi=heads-rab
    print(rab, chi)
r_c()