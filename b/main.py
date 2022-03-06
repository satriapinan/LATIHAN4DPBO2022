from Person import Person
from Job import Job
from Driver import Driver

# Tampilan awal Input
print("=========")
print("| INPUT |")
print("=========\n")

# PERSON

print("===== Buat Person =====\n")

# Input banyak Person
jumlahPerson = int(input("Masukan banyak Person yang ingin dibuat : "))
print()

# Alokasi dan sekaligus instansiasi untuk banyak Person
person = [Person() for i in range(jumlahPerson)]

# Perulangan input data untuk setiap Person
for i in range(jumlahPerson):
	print("-----------------------")
	print("Masukan Data Person", i+1, "|")
	print("-----------------------")

	person[i].setNIK(input("NIK    : "))
	person[i].setName(input("Name   : "))
	person[i].setGender(input("Gender : "))

# JOB

print("\n===== Buat Pekerjaan =====\n")

# Input banyak Job
jumlahJob = int(input("Masukan banyak Pekerjaan yang ingin dibuat : "))
print()

# Alokasi dan sekaligus instansiasi untuk banyak Job
job = [Job() for i in range(jumlahJob)]

# Perulangan input data untuk setiap Job
for i in range(jumlahJob):
	print("--------------------------")
	print("Masukan Data Pekerjaan", i+1, "|")
	print("--------------------------")

	job[i].setNIP(input("NIP      : "))
	job[i].setCompany(input("Company  : "))
	job[i].setPosition(input("Position : "))

# DRIVER

print("\n===== Buat Pengemudi =====\n")

# Input banyak Driver
jumlahDriver = int(input("Masukan banyak Pengemudi yang ingin dibuat : "))
print()

# Alokasi dan sekaligus instansiasi untuk banyak Driver
driver = [Driver() for i in range(jumlahDriver)]

# Perulangan input data untuk setiap Driver
for i in range(jumlahDriver):
	print("--------------------------")
	print("Masukan Data Pengemudi", i+1, "|")
	print("--------------------------")

	driver[i].setNIK(input("NIK                : "))
	driver[i].setName(input("Name               : "))
	driver[i].setGender(input("Gender             : "))
	driver[i].setNIP(input("NIP                : "))
	driver[i].setCompany(input("Company            : "))
	driver[i].setPosition(input("Position           : "))
	driver[i].setLicenseID(input("License ID         : "))
	driver[i].setActiveUntil(input("Active Until(year) : "))
	driver[i].setVehicleType(input("Vehicle Type       : "))
	driver[i].sleep(input("Sleep?(y/n)        : "))

# Tampilan awal Output
print("\n=========")
print("| OUTPUT |")
print("=========\n")

# Person

print("===== Person =====\n")
# Perulangan output data untuk setiap Person
for i in range(jumlahPerson):
	for j in range(len(person[i].getName()) + 7):
		print("-", end="")
	print("\nData", person[i].getName(), "|")
	for j in range(len(person[i].getName()) + 7):
		print("-", end="")
	print()
	print("NIK    :", person[i].getNIK())
	print("Name   :", person[i].getName())
	print("Gender :", person[i].getGender())

# Job

print("\n===== Pekerjaan =====\n")
# Perulangan output data untuk setiap Job
for i in range(jumlahJob):
	for j in range(len(job[i].getNIP()) + 7):
		print("-", end="")
	print("\nData", job[i].getNIP(), "|")
	for j in range(len(job[i].getNIP()) + 7):
		print("-", end="")
	print()
	print("NIP      :", job[i].getNIP())
	print("Company  :", job[i].getCompany())
	print("Position :", job[i].getPosition())

# Driver

print("\n===== Pengemudi =====\n")
# Perulangan output data untuk setiap Driver
for i in range(jumlahDriver):
	for j in range(len(driver[i].getName()) + 17):
		print("-", end="")
	print("\nData Pengemudi", driver[i].getName(), "|")
	for j in range(len(driver[i].getName()) + 17):
		print("-", end="")
	print()
	print("NIK                :", driver[i].getNIK())
	print("Name               :", driver[i].getName())
	print("Gender             :", driver[i].getGender())
	print("NIP                :", driver[i].getNIP())
	print("Company            :", driver[i].getCompany())
	print("Position           :", driver[i].getPosition())
	print("License ID         :", driver[i].getLicenseID())
	print("Active Until(year) :", driver[i].getActiveUntil())
	print("Vehicle Type       :", driver[i].getVehicleType())
	print("Status             :", driver[i].getAlvaible())