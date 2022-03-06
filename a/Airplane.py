from Vehicle import Vehicle

class Airplane(Vehicle):
	# Konstruktor
	def __init__(self):
		self.__type = ""
		self.__age = 0
		self.__wings = 0

	# Setter
	def setType(self, type):
		self.__type = type
	def setAge(self, age):
		self.__age = age
	def setWingsLength(self, wings):
		self.__wings = wings

	# Getter
	def getType(self):
		return self.__type
	def getAge(self):
		return self.__age
	def getWingsLength(self):
		return self.__wings