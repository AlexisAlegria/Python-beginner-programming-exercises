import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

print(spin_chamber())

#  DON'T CHANGE THE CODE ABOVE
def fire_gun(spinnerPosition):
	# YOUR CODE HERE
		for spinnerPosition in range (1,6):
			if spinnerPosition == bullet_position:
				print("You are dead!")
			else:
				print("Keep playing!")

print(fire_gun(spin_chamber))