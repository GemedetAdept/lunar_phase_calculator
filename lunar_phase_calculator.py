# TODOs: See block quotes within each function.


def generate_leap_list(year):
	'''Generate saved list of standard/leap years from given year
	A given year is a leap year IF:
		YEAR % 4 == 0
	AND NOT IF:
		YEAR % 100 == 0
	EXCEPT IF:
		YEAR % 400 == 0
	'''


def julian_conv(year):
	'''Convert Gregorian UNIX date to Julian day value
	Call from list of standard and leap years
	Calculate difference from 2000-01-01 to input year
	'''


def chapront_synodic(jul_day):
	'''Calculate precise synodic month duration for a given Julian month/day
	"Éphéméride Lunaire Parisienne" (Chapront-Touzé, Chapront, et. al.)

	Generate list of precise synodic duration for each month in a given year
	'''


def lunar_phase(day):
	'''Output lunar phase on a given day, given:
		* Julian day value
		* Precise synodic month duration (Chapront-Touzé, Chapront)
		* Percentage of elapsed time within synodic month
	Where:
		* Synodic month duration / 8 = Elapsed time per phase 
	'''
