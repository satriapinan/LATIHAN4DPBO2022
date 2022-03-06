class Person:
	# Konstruktor
	def __init__(self):
		self.__nik = ""
		self.__name = ""
		self.__gender = ""
		self.__alvaible = True

	# Setter
	def setNIK(self, nik):
		self.__nik = nik
	def setName(self, name):
		self.__name = name
	def setGender(self, gender):
		self.__gender = gender

	# Getter
	def getNIK(self):
		return self.__nik
	def getName(self):
		return self.__name
	def getGender(self):
		return self.__gender
	def getAlvaible(self):
		return "Sedang tidur." if (self.__alvaible == False) else "Siap kerja!" 

	# Method
	def sleep(self, sleep):
		self.__alvaible = True if (sleep == 'n') else False
