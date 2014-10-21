# +==========================+
# = Einstein's Riddle Solver =
# +==========================+
#   Author: Henry Tran
#   Time: 10/21/2014 1:29 AM
#   License: GPL v3
# +==========================+

# Methodology:
# ------------
# An `attribute` can be `House #1's Color` or `House #2's Drink`.
# An `attribute value` can be `Drinks Tea` or `Keeps Dogs`.
#
# I first assume that every house contains every single `possible`
# attribute value.
#
# When a house is conclusive with an attribute, or there is only 1
# `possible` attribute for that house, then that attribute is marked
# as `determined`.
#
# The possibilities of the house `evolve` over time,
# as the rules and process of elimination are iteratively applied
# to each house.
# The process of elimination sees if a house has an attribute that
# none of the other houses have, then marks the attribute as
# `determined`.
#
# This loops until each house has a possibility of only
# 1 attribute, and thus `determined`.
#

# Post Mortem:
# ------------
# This would have been better if I made the attributes an array
# instead of defining them as instance variables.
#
# That way the code would be much shorter
# and I can just iterate through the array,
# rather than repeating the same lines of code over and over.
# 
# Perhaps I'll remake this script to use attributes array,
# but that will be another day.
#

from math import floor

class Attributes:
	NATION		= 0
	COLOR		= 1
	SMOKE		= 2
	DRINK		= 3
	PET			= 4

class Nations:
	BRIT 		= 0
	SWEDE 		= 1
	DANE		= 2
	GERMAN		= 3
	NORWEGIAN 	= 4

class Colors:
	RED			= 0
	BLUE		= 1
	GREEN		= 2
	YELLOW		= 3
	WHITE		= 4

class Smokes:
	DUNHILL		= 0
	PALLMALL	= 1
	BLENDS		= 2
	BLUEMASTER	= 3
	PRINCE		= 4

class Drinks:
	COFFEE		= 0
	TEA			= 1
	MILK		= 2
	BEER		= 3
	WATER		= 4

class Pets:
	CATS		= 0
	HORSES		= 1
	DOGS		= 2
	FISH		= 3
	BIRDS		= 4

determined = [[False]*5, [False]*5, [False]*5, [False]*5, [False]*5]

class House:
	#
	def __init__(self):
		self.leftNeighbor 	= None
		self.rightNeighbor 	= None
		self.houseIndex 	= 0

		# attributes
		self.nations 		= range(5)
		self.colors 		= range(5)
		self.smokes 		= range(5)
		self.drinks 		= range(5)
		self.pets 			= range(5)

		# attribute locks
		self.nationsLock	= False
		self.colorsLock		= False
		self.smokesLock		= False
		self.drinksLock		= False
		self.petsLock		= False

	#
	def getLeftNeighbor(self):
		return self.leftNeighbor

	def getRightNeighbor(self):
		return self.rightNeighbor

	def getHouseIndex(self):
		return self.houseIndex

	def determineAttribute(self, type, attribute):
		if determined[type][attribute]:
			return
		else:
			determined[type][attribute] = True

		if type == Attributes.NATION and not self.nationsLock:
			self.nations = [attribute]
			self.nationsLock = True
		if type == Attributes.COLOR and not self.colorsLock:
			self.colors = [attribute]
			self.colorsLock = True
		if type == Attributes.SMOKE and not self.smokesLock:
			self.smokes = [attribute]
			self.smokesLock = True
		if type == Attributes.DRINK and not self.drinksLock:
			self.drinks = [attribute]
			self.drinksLock = True
		if type == Attributes.PET and not self.petsLock:
			self.pets = [attribute]
			self.petsLock = True

		for house in houses:
			if house != self:
				house.removeAttribute(type, attribute)

	def hasAttribute(self, type, attribute):
		if type == Attributes.NATION:
			return attribute in self.nations
		if type == Attributes.COLOR:
			return attribute in self.colors
		if type == Attributes.SMOKE:
			return attribute in self.smokes
		if type == Attributes.DRINK:
			return attribute in self.drinks
		if type == Attributes.PET:
			return attribute in self.pets
		return False

	def isAttribute(self, type, attribute):
		if type == Attributes.NATION and len(self.nations) == 1:
			return attribute in self.nations
		if type == Attributes.COLOR and len(self.colors) == 1:
			return attribute in self.colors
		if type == Attributes.SMOKE and len(self.smokes) == 1:
			return attribute in self.smokes
		if type == Attributes.DRINK and len(self.drinks) == 1:
			return attribute in self.drinks
		if type == Attributes.PET and len(self.pets) == 1:
			return attribute in self.pets
		return False

	def removeAttribute(self, type, attribute):
		if attribute == None:
			return

		if not self.hasAttribute(type, attribute):
			return

		attributeCount = 0
		lastAttribute = None

		if type == Attributes.NATION and not self.nationsLock:
			self.nations.remove(attribute)
			attributeCount = len(self.nations)
			lastAttribute = self.nations[0]
			if attributeCount == 1:
				self.nationsLock = True
		if type == Attributes.COLOR and not self.colorsLock:
			self.colors.remove(attribute)
			attributeCount = len(self.colors)
			lastAttribute = self.colors[0]
			if attributeCount == 1:
				self.colorsLock = True
		if type == Attributes.SMOKE and not self.smokesLock:
			self.smokes.remove(attribute)
			attributeCount = len(self.smokes)
			lastAttribute = self.smokes[0]
			if attributeCount == 1:
				self.smokesLock = True
		if type == Attributes.DRINK and not self.drinksLock:
			self.drinks.remove(attribute)
			attributeCount = len(self.drinks)
			lastAttribute = self.drinks[0]
			if attributeCount == 1:
				self.drinksLock = True
		if type == Attributes.PET and not self.petsLock:
			self.pets.remove(attribute)
			attributeCount = len(self.pets)
			lastAttribute = self.pets[0]
			if attributeCount == 1:
				self.petsLock = True

		if attributeCount == 1:
			determined[type][lastAttribute] = True
			for house in houses:
				if house != self:
					house.removeAttribute(type, lastAttribute)


class EmptyHouse(House):
	#
	def hasAttribute(self, type, attribute):
		return False

	def determineAttribute(self, type, attribute):
		pass

	def removeAttribute(self, type, attribute):
		pass

def applyRules(house, houseCount, houses):
	# Rule 1. The Brit lives in a red house.
		### NEGATING ###
		if not house.hasAttribute(Attributes.NATION, Nations.BRIT):
			house.removeAttribute(Attributes.COLOR, Colors.RED)
		if not house.hasAttribute(Attributes.COLOR, Colors.RED):
			house.removeAttribute(Attributes.NATION, Nations.BRIT)

		### DETERMINING ###
		if house.isAttribute(Attributes.NATION, Nations.BRIT):
			house.determineAttribute(Attributes.COLOR, Colors.RED)
		if house.isAttribute(Attributes.COLOR, Colors.RED):
			house.determineAttribute(Attributes.NATION, Nations.BRIT)
	# Rule 2. The Swede keeps dogs as pets.
		### NEGATING ###
		if not house.hasAttribute(Attributes.NATION, Nations.SWEDE):
			house.removeAttribute(Attributes.PET, Pets.DOGS)
		if not house.hasAttribute(Attributes.PET, Pets.DOGS):
			house.removeAttribute(Attributes.NATION, Nations.SWEDE)

		### DETERMINING ###
		if house.isAttribute(Attributes.NATION, Nations.SWEDE):
			house.determineAttribute(Attributes.PET, Pets.DOGS)
		if house.isAttribute(Attributes.PET, Pets.DOGS):
			house.determineAttribute(Attributes.NATION, Nations.SWEDE)
	# Rule 3. The Dane drinks tea.
		### NEGATING ###
		if not house.hasAttribute(Attributes.NATION, Nations.DANE):
			house.removeAttribute(Attributes.DRINK, Drinks.TEA)
		if not house.hasAttribute(Attributes.DRINK, Drinks.TEA):
			house.removeAttribute(Attributes.NATION, Nations.DANE)

		### DETERMINING ###
		if house.isAttribute(Attributes.NATION, Nations.DANE):
			house.determineAttribute(Attributes.DRINK, Drinks.TEA)
		if house.isAttribute(Attributes.DRINK, Drinks.TEA):
			house.determineAttribute(Attributes.NATION, Nations.DANE)
	# Rule 4. The Green house is next to, and on the left of the White house.
		### NEGATING ###
		if not house.getRightNeighbor().hasAttribute(Attributes.COLOR, Colors.WHITE):
			house.removeAttribute(Attributes.COLOR, Colors.GREEN)
		if not house.getLeftNeighbor().hasAttribute(Attributes.COLOR, Colors.GREEN):
			house.removeAttribute(Attributes.COLOR, Colors.WHITE)

		### DETERMINING ###
		if house.getRightNeighbor().isAttribute(Attributes.COLOR, Colors.WHITE):
			house.determineAttribute(Attributes.COLOR, Colors.GREEN)
		if house.getLeftNeighbor().isAttribute(Attributes.COLOR, Colors.GREEN):
			house.determineAttribute(Attributes.COLOR, Colors.WHITE)
	# Rule 5. The owner of the Green house drinks coffee.
		### NEGATING ###
		if not house.hasAttribute(Attributes.COLOR, Colors.GREEN):
			house.removeAttribute(Attributes.DRINK, Drinks.COFFEE)
		if not house.hasAttribute(Attributes.DRINK, Drinks.COFFEE):
			house.removeAttribute(Attributes.COLOR, Colors.GREEN)

		### DETERMINING ###
		if house.isAttribute(Attributes.COLOR, Colors.GREEN):
			house.determineAttribute(Attributes.DRINK, Drinks.COFFEE)
		if house.isAttribute(Attributes.DRINK, Drinks.COFFEE):
			house.determineAttribute(Attributes.COLOR, Colors.GREEN)
	# Rule 6. The person who smokes Pall Mall rears birds.
		### NEGATING ###
		if not house.hasAttribute(Attributes.SMOKE, Smokes.PALLMALL):
			house.removeAttribute(Attributes.PET, Pets.BIRDS)
		if not house.hasAttribute(Attributes.PET, Pets.BIRDS):
			house.removeAttribute(Attributes.SMOKE, Smokes.PALLMALL)

		### DETERMINING ###
		if house.isAttribute(Attributes.SMOKE, Smokes.PALLMALL):
			house.determineAttribute(Attributes.PET, Pets.BIRDS)
		if house.isAttribute(Attributes.PET, Pets.BIRDS):
			house.determineAttribute(Attributes.SMOKE, Smokes.PALLMALL)
	# Rule 7. The owner of the Yellow house smokes Dunhill.
		### NEGATING ###
		if not house.hasAttribute(Attributes.COLOR, Colors.YELLOW):
			house.removeAttribute(Attributes.SMOKE, Smokes.DUNHILL)
		if not house.hasAttribute(Attributes.SMOKE, Smokes.DUNHILL):
			house.removeAttribute(Attributes.COLOR, Colors.YELLOW)

		### DETERMINING ###
		if house.isAttribute(Attributes.COLOR, Colors.YELLOW):
			house.determineAttribute(Attributes.SMOKE, Smokes.DUNHILL)
		if house.isAttribute(Attributes.SMOKE, Smokes.DUNHILL):
			house.determineAttribute(Attributes.COLOR, Colors.YELLOW)
	# Rule 8. The man living in the centre house drinks milk.
		middleHouseIndex = floor(houseCount / 2)

		### DETERMINING ###
		if house.getHouseIndex() == middleHouseIndex:
			house.determineAttribute(Attributes.DRINK, Drinks.MILK)
		else:
			house.removeAttribute(Attributes.DRINK, Drinks.MILK)

	# Rule 9. The Norwegian lives in the first house.
		### DETERMINING ###
		if house.getHouseIndex() == 0:
			house.determineAttribute(Attributes.NATION,	Nations.NORWEGIAN)
		else:
			house.removeAttribute(Attributes.NATION, Nations.NORWEGIAN)

	# Rule 10. The man who smokes Blends lives next to the one who keeps cats.
		### NEGATING ###
		if not (house.getLeftNeighbor().hasAttribute(Attributes.PET, Pets.CATS) or
				house.getRightNeighbor().hasAttribute(Attributes.PET, Pets.CATS)
		):
			house.removeAttribute(Attributes.SMOKE, Smokes.BLENDS)

		if not (house.getLeftNeighbor().hasAttribute(Attributes.SMOKE, Smokes.BLENDS) or
				house.getRightNeighbor().hasAttribute(Attributes.SMOKE, Smokes.BLENDS)
		):
			house.removeAttribute(Attributes.PET, Pets.CATS)

		### DETERMINING ###
		if (house.getLeftNeighbor().isAttribute(Attributes.PET, Pets.CATS) or
				house.getRightNeighbor().isAttribute(Attributes.PET, Pets.CATS)
		):
			house.determineAttribute(Attributes.SMOKE, Smokes.BLENDS)

		if (house.getLeftNeighbor().isAttribute(Attributes.SMOKE, Smokes.BLENDS) or
				house.getRightNeighbor().isAttribute(Attributes.SMOKE, Smokes.BLENDS)
		):
			house.determineAttribute(Attributes.PET, Pets.CATS)
	# Rule 11. The man who keeps horses lives next to the man who smokes Dunhill.
		### NEGATING ###
		if not (house.getLeftNeighbor().hasAttribute(Attributes.SMOKE, Smokes.DUNHILL) or
				house.getRightNeighbor().hasAttribute(Attributes.SMOKE, Smokes.DUNHILL)
		):
			house.removeAttribute(Attributes.PET, Pets.HORSES)

		if not (house.getLeftNeighbor().hasAttribute(Attributes.PET, Pets.HORSES) or
				house.getRightNeighbor().hasAttribute(Attributes.PET, Pets.HORSES)
		):
			house.removeAttribute(Attributes.SMOKE, Smokes.DUNHILL)

		### DETERMINING ###
		if (house.getLeftNeighbor().isAttribute(Attributes.SMOKE, Smokes.DUNHILL) or
				house.getRightNeighbor().isAttribute(Attributes.SMOKE, Smokes.DUNHILL)
		):
			house.determineAttribute(Attributes.PET, Pets.HORSES)

		if (house.getLeftNeighbor().isAttribute(Attributes.PET, Pets.HORSES) or
				house.getRightNeighbor().isAttribute(Attributes.PET, Pets.HORSES)
		):
			house.determineAttribute(Attributes.SMOKE, Smokes.DUNHILL)
	# Rule 12. The man who smokes Blue Master drinks beer.
		### NEGATING ###
		if not house.hasAttribute(Attributes.SMOKE, Smokes.BLUEMASTER):
			house.removeAttribute(Attributes.DRINK, Drinks.BEER)
		if not house.hasAttribute(Attributes.DRINK, Drinks.BEER):
			house.removeAttribute(Attributes.SMOKE, Smokes.BLUEMASTER)

		### DETERMINING ###
		if not house.isAttribute(Attributes.SMOKE, Smokes.BLUEMASTER):
			house.determineAttribute(Attributes.DRINK, Drinks.BEER)
		if not house.isAttribute(Attributes.DRINK, Drinks.BEER):
			house.determineAttribute(Attributes.SMOKE, Smokes.BLUEMASTER)
	# Rule 13. The German smokes Prince.
		### NEGATING ###
		if not house.hasAttribute(Attributes.NATION, Nations.GERMAN):
			house.removeAttribute(Attributes.SMOKE, Smokes.PRINCE)
		if not house.hasAttribute(Attributes.SMOKE, Smokes.PRINCE):
			house.removeAttribute(Attributes.NATION, Nations.GERMAN)

		### DETERMINING ###
		if not house.isAttribute(Attributes.NATION, Nations.GERMAN):
			house.determineAttribute(Attributes.SMOKE, Smokes.PRINCE)
		if not house.isAttribute(Attributes.SMOKE, Smokes.PRINCE):
			house.determineAttribute(Attributes.NATION, Nations.GERMAN)
	# Rule 14. The Norwegian lives next to the blue house.
		### NEGATING ###
		if not (house.getLeftNeighbor().hasAttribute(Attributes.COLOR, Colors.BLUE) or
				house.getRightNeighbor().hasAttribute(Attributes.COLOR, Colors.BLUE)
		):
			house.removeAttribute(Attributes.NATION, Nations.NORWEGIAN)

		if not (house.getLeftNeighbor().hasAttribute(Attributes.NATION, Nations.NORWEGIAN) or
				house.getRightNeighbor().hasAttribute(Attributes.NATION, Nations.NORWEGIAN)
		):
			house.removeAttribute(Attributes.COLOR, Colors.BLUE)

		### DETERMINING ###
		if (house.getLeftNeighbor().isAttribute(Attributes.COLOR, Colors.BLUE) or
				house.getRightNeighbor().isAttribute(Attributes.COLOR, Colors.BLUE)
		):
			house.determineAttribute(Attributes.NATION,	Nations.NORWEGIAN)

		if (house.getLeftNeighbor().isAttribute(Attributes.NATION, Nations.NORWEGIAN) or
				house.getRightNeighbor().isAttribute(Attributes.NATION, Nations.NORWEGIAN)
		):
			house.determineAttribute(Attributes.COLOR, Colors.BLUE)

	# Rule 15. The man who smokes Blends has a neighbour who drinks water.
		### NEGATING ###
		if not (house.getLeftNeighbor().hasAttribute(Attributes.DRINK, Drinks.WATER) or
				house.getRightNeighbor().hasAttribute(Attributes.DRINK, Drinks.WATER)
		):
			house.removeAttribute(Attributes.SMOKE,	Smokes.BLENDS)

		if not (house.getLeftNeighbor().hasAttribute(Attributes.SMOKE, Smokes.BLENDS) or
				house.getRightNeighbor().hasAttribute(Attributes.SMOKE, Smokes.BLENDS)
		):
			house.removeAttribute(Attributes.DRINK,	Drinks.WATER)

		### DETERMINING ###
		if (house.getLeftNeighbor().isAttribute(Attributes.DRINK, Drinks.WATER) or
				house.getRightNeighbor().isAttribute(Attributes.DRINK, Drinks.WATER)
		):
			house.determineAttribute(Attributes.SMOKE, Smokes.BLENDS)

		if (house.getLeftNeighbor().isAttribute(Attributes.SMOKE, Smokes.BLENDS) or
				house.getRightNeighbor().isAttribute(Attributes.SMOKE, Smokes.BLENDS)
		):
			house.determineAttribute(Attributes.DRINK, Drinks.WATER)

def processOfElimination(house, houses):
	for nation in house.nations:
		isDetermined = True
		for otherHouse in houses:
			if otherHouse != house:
				if nation in otherHouse.nations:
					isDetermined = False
					break
		if isDetermined:
			house.determineAttribute(Attributes.NATION, nation)
			break
	for color in house.colors:
		isDetermined = True
		for otherHouse in houses:
			if otherHouse != house:
				if color in otherHouse.colors:
					isDetermined = False
					break
		if isDetermined:
			house.determineAttribute(Attributes.COLOR, color)
			break
	for smoke in house.smokes:
		isDetermined = True
		for otherHouse in houses:
			if otherHouse != house:
				if smoke in otherHouse.smokes:
					isDetermined = False
					break
		if isDetermined:
			house.determineAttribute(Attributes.SMOKE, smoke)
			break
	for drink in house.drinks:
		isDetermined = True
		for otherHouse in houses:
			if otherHouse != house:
				if drink in otherHouse.drinks:
					isDetermined = False
					break
		if isDetermined:
			house.determineAttribute(Attributes.DRINK, drink)
			break
	for pet in house.pets:
		isDetermined = True
		for otherHouse in houses:
			if otherHouse != house:
				if pet in otherHouse.pets:
					isDetermined = False
					break
		if isDetermined:
			house.determineAttribute(Attributes.PET, pet)
			break

def fillHouses(houses):
	# Determines house neighbors
	houseIndex = 0
	lastHouse = EmptyHouse()
	for house in houses:
		lastHouse.rightNeighbor = house
		house.leftNeighbor = lastHouse
		lastHouse = house

		house.houseIndex = houseIndex
		houseIndex += 1
	houses[-1].rightNeighbor = EmptyHouse()

def printHouses(houses):
	for house in houses:
		print "== %i ==" % house.getHouseIndex()

		nations = "nations: "
		for nation in house.nations:
			nations += (["BRIT", "SWEDE", "DANE", "GERMAN", "NORWEGIAN"])[nation] + " "
		print nations

		colors = "colors: "
		for color in house.colors:
			colors += (["RED", "BLUE", "GREEN", "YELLOW", "WHITE"])[color] + " "
		print colors

		smokes = "smokes: "
		for smoke in house.smokes:
			smokes += (["DUNHILL", "PALLMALL", "BLENDS", "BLUEMASTER", "PRINCE"])[smoke] + " "
		print smokes

		drinks = "drinks: "
		for drink in house.drinks:
			drinks += (["COFFEE", "TEA", "MILK", "BEER", "WATER"])[drink] + " "
		print drinks

		pets = "pets: "
		for pet in house.pets:
			pets += (["CATS", "HORSES", "DOGS", "FISH", "BIRDS"])[pet] + " "
		print pets

def isUnsolved(houses):
	for house in houses:
		if len(house.nations) > 1:
			return True
		if len(house.colors) > 1:
			return True
		if len(house.smokes) > 1:
			return True
		if len(house.drinks) > 1:
			return True
		if len(house.pets) > 1:
			return True
	return False

####

#
houses = [House(), House(), House(), House(), House()];

#
fillHouses(houses)

# do a few rule passes on the houses.
while isUnsolved(houses):
	for house in houses:
		applyRules(house, len(houses), houses)

	for house in houses:
		processOfElimination(house, houses)

#
printHouses(houses)
