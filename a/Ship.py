from Vehicle import Vehicle

class Ship(Vehicle):
	# Konstruktor
	def __init__(self):
		self.__age = 0
		self.__type = ""
		self.__country = ""

	# Setter
	def setAge(self, age):
		self.__age = age
	def setType(self, type):
		self.__type = type
	def setCountry(self, country):
		self.__country = country

	# Getter
	def getAge(self):
		return self.__age
	def getType(self):
		return self.__type
	def getCountry(self):
		return self.__country