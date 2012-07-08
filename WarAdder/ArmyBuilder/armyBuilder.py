import sqlite3 as lite

def createDB()

	conn = sqlite3.connection('warAdder.db')

	with conn:
		c = conn.cursor()
		c.execute('''CREATE TABLE unitTypes(unitType TEXT, 
						    specialRules TEXT)''')

		c.execute('''CREATE TABLE specialRules(ruleName TEXT, 
						       ruleInfo TEXT)''')

		c.execute('''CREATE TABLE daemonUnits(unitName TEXT, 
						      unitType TEXT, 
						      wS INT, bS INT, s INT, t INT, i INT, a INT, Ld INT, Sv INT, saveType TEXT, pointsPerModel INT)''')

def populateDB()
	conn = sqlite.connection('warAdder.db')

	with conn:
		c = conn.cursor()

		c.executemany("INSERT INTO unitTypes VALUES(




def getArmyInfo()
	
	conn = sqlite3.connection('warAdder.db')
	
	with conn:

		c = conn.cursor()

		continue = 'y'
		while continue == 'y':
			armyName = raw_input('Enter your army name:')
			print 'You entered' , armyName
	
			unitName = raw_input('Enter the unit name:')
			print 'You entered', unitName

			unitType = raw_input('Enter the unit type:')
			print 'You entered', unitType

			statLine = []
			stats = ['WS','BS','S','T','I','A','Ld','Sv']

			for response in statLine:
				for stat in stats:
				userResponse = raw_input('Please enter unit's %s', % stat)		
				statLine.append(userResponse)
			
			print statLine

			pointsPerModel = raw_input('Please enter unit's per model point cost:')
				
			c.execute('INSERT INTO
			continue = raw_input('Would you like to enter another unit? (y/n)')

