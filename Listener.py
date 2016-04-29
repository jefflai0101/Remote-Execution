#imports
#===============================================================================================================================================
import os
import csv
import time
import datetime
#===============================================================================================================================================
#Obtain current folder path
folderPath = os.path.dirname(os.path.abspath(__file__))

#*********************************Settings*********************************
dbPath = ''
checkInterval = 30					#Default command checking interval
#**************************************************************************

#===============================================================================================================================================
commandPath = os.path.join(dbPath, 'command.txt')
commandRead = ''
doneRead = False

def commandAction(commandRead):
	with open(os.path.join(folderPath, 'list.csv'), 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
		for row in csvreader:
			if (row[0].upper() == commandRead.upper()):
				return row[1]
	csvfile.close()
	return ''

def iRun(commandRead):
	triggerRun = commandAction(commandRead)
	if (triggerRun != ''):
		os.system('start python ' + triggerRun)
		print ('>>>' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
		print ('Executed:\t' + commandRead)


def mainLoop():
	os.system('cls') if os.name == 'nt' else os.system('clear')
	print ('=' * 42)
	print ('>>>Listening')
	while (doneRead == False):
		if (os.path.isfile(commandPath) == False):
			commandFile = open(commandPath, 'w+')
			commandFile.writeline('Nothing')
		else:
			with open(commandPath, 'r') as commandFile:
				commandRead = commandFile.readline()
			if (commandRead != 'Nothing'):
				iRun(commandRead)
				with open(commandPath, 'w') as commandFile:
					commandFile.write('Nothing')
		time.sleep (checkInterval)

mainLoop()
	