from Person import Person
from Job import Job

class Driver(Person, Job):
	# Konstruktor
	def __init__(self):
		self.__licenseID = ""
		self.__active = ""
		self.__vehicle = ""

	# Setter
	def setLicenseID(self, licenseID):
		self.__licenseID = licenseID
	def setActiveUntil(self, active):
		self.__active = active
	def setVehicleType(self, vehicle):
		self.__vehicle = vehicle

	# Getter
	def getLicenseID(self):
		return self.__licenseID
	def getActiveUntil(self):
		return self.__active
	def getVehicleType(self):
		return self.__vehicle