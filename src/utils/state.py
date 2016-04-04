# loaded objects
from utils.csvreader import CsvReader
from items.weapon import Weapon
from items.armour import Armour
from skills.targets import *


weapons = []
armour = []

def loadCSVs():
	weaponcsv = CsvReader.read("..\\data\\wep.csv")
	keys = weaponcsv[0]
	numberOfObjects = len(weaponcsv)
	print("  Loading Weapons")
	for i in range (1,numberOfObjects):
		weapons.append(Weapon(keys,weaponcsv[i]))
		print("    - " + str(weaponcsv[i][1]))
	
	armourcsv = CsvReader.read("..\\data\\armour.csv")
	keys = armourcsv[0]
	numberOfObjects = len(armourcsv)
	print("  Loading Armour")
	for i in range (1,numberOfObjects):
		armour.append(Armour(keys,armourcsv[i]))
		print("    - " + str(armourcsv[i][1]))
	