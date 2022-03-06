class Vehicle:
	# Konstruktor
	def __init__(self):
		self.__fuel = ""
		self.__passengers = 0
		self.__alvaible = True

	# Setter
	def setFuel(self, fuel):
		self.__fuel = fuel
	def setPassengers(self, passengers):
		self.__passengers = passengers

	# Getter
	def getFuel(self):
		return self.__fuel
	def getPassengers(self):
		return self.__passengers
	def getAlvaible(self):
		return "Di jalan." if (self.__alvaible == False) else "Di Garasi" 

	# Method
	def move(self, move):
		self.__alvaible = True if (move == 'n') else False