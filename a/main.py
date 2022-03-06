from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane

# Tampilan awal Input
print("=========")
print("| INPUT |")
print("=========\n")

# Vehicle

print("===== Buat Kendaraan =====\n")

# Input banyak Vehicle
jumlahVehicle = int(input("Masukan banyak Kendaraan yang ingin dibuat : "))
print()

# Alokasi dan sekaligus instansiasi untuk banyak Vehicle
vehicle = [Vehicle() for i in range(jumlahVehicle)]

# Perulangan input data untuk setiap Vehicle
for i in range(jumlahVehicle):
	print("--------------------------")
	print("Masukan Data Kendaraan", i+1, "|")
	print("--------------------------")

	vehicle[i].setFuel(input("Fuel Type      : "))
	vehicle[i].setPassengers(input("Max Passengers : "))

# Ship

print("\n===== Buat Kapal =====\n")

# Input banyak Ship
jumlahShip = int(input("Masukan banyak Kapal yang ingin dibuat : "))
print()

# Alokasi dan sekaligus instansiasi untuk banyak Ship
ship = [Ship() for i in range(jumlahShip)]

# Perulangan input data untuk setiap Ship
for i in range(jumlahShip):
	print("----------------------")
	print("Masukan Data Kapal", i+1, "|")
	print("----------------------")

	ship[i].setType(input("Type                   : "))
	ship[i].setAge(int(input("Age                    : ")))
	ship[i].setFuel(input("Fuel Type              : "))
	ship[i].setPassengers(input("Max Passengers         : "))
	ship[i].setCountry(input("Country of Manufacture : "))
	ship[i].move(input("Moving?(y/n)           : "))

# Airplane

print("\n===== Buat Pesawat =====\n")

# Input banyak Airplane
jumlahAirplane = int(input("Masukan banyak Pesawat yang ingin dibuat : "))
print()

# Alokasi dan sekaligus instansiasi untuk banyak Airplane
airplane = [Airplane() for i in range(jumlahAirplane)]

# Perulangan input data untuk setiap Airplane
for i in range(jumlahAirplane):
	print("------------------------")
	print("Masukan Data Pesawat", i+1, "|")
	print("------------------------")

	airplane[i].setType(input("Type           : "))
	airplane[i].setAge(int(input("Age            : ")))
	airplane[i].setFuel(input("Fuel Type      : "))
	airplane[i].setPassengers(input("Max Passengers : "))
	airplane[i].setWingsLength(int(input("Wings Length   : ")))
	airplane[i].move(input("Moving?(y/n)   : "))

# Tampilan awal Output
print("\n==========")
print("| OUTPUT |")
print("==========\n")

# Vehicle

print("===== Kendaraan =====\n")
# Perulangan output data untuk setiap Vehicle
for i in range(jumlahVehicle):
	for j in range(len(str(i)) + 17):
		print("-", end="")
	print("\nData Kendaraan", i+1, "|")
	for j in range(len(str(i)) + 17):
		print("-", end="")
	print()
	print("Fuel Type      :", vehicle[i].getFuel())
	print("Max Passengers :", vehicle[i].getPassengers())

# Ship

print("\n===== Kapal =====\n")
# Perulangan output data untuk setiap Ship
for i in range(jumlahShip):
	for j in range(len(ship[i].getType()) + 13):
		print("-", end="")
	print("\nData Kapal", ship[i].getType(), "|")
	for j in range(len(ship[i].getType()) + 13):
		print("-", end="")
	print()
	print("Type                   :", ship[i].getType())
	print("Age                    :", ship[i].getAge())
	print("Fuel Type              :", ship[i].getFuel())
	print("Max Passengers         :", ship[i].getPassengers())
	print("Country of Manufacture :", ship[i].getCountry())
	print("Status                 :", ship[i].getAlvaible())

# Airplane

print("\n===== Pesawat =====\n")
# Perulangan output data untuk setiap Airplane
for i in range(jumlahAirplane):
	for j in range(len(airplane[i].getType()) + 15):
		print("-", end="")
	print("\nData Pesawat", airplane[i].getType(), "|")
	for j in range(len(airplane[i].getType()) + 15):
		print("-", end="")
	print()
	print("Type           :", airplane[i].getType())
	print("Age            :", airplane[i].getAge())
	print("Fuel Type      :", airplane[i].getFuel())
	print("Max Passengers :", airplane[i].getPassengers())
	print("Wings Length   :", airplane[i].getWingsLength())
	print("Status         :", airplane[i].getAlvaible())