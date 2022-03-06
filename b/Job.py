class Job:
	# Konstruktor
	def __init__(self):
		self.__nip = ""
		self.__company = ""
		self.__position = ""

	# Setter
	def setNIP(self, nip):
		self.__nip = nip
	def setCompany(self, company):
		self.__company = company
	def setPosition(self, position):
		self.__position = position

	# Getter
	def getNIP(self):
		return self.__nip
	def getCompany(self):
		return self.__company
	def getPosition(self):
		return self.__position