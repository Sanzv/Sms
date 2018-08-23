'''Proram to calculate number of days, hrs ,mins,secs from the time input in miliseconds using different functions'''


def calc_secs(ms):
	return(ms/1000)

def calc_mins(ms):
	divideWith= 1000*60
	return(ms/divideWith)

def calc_hrs(ms):
	divideWith= 1000*60*60
	return(ms/divideWith)

def calc_days(ms):
	divideWith= 1000*60*60*24
	return(ms/divideWith)

ms=int(input("Enter the miliseconds: \t"))
'''sec=calc_secs(ms)
min=calc_mins(sec)
hr=calc_hrs(min)
day=calc_days(hr)'''

print("Seconds : {} ".format(calc_secs(ms)))
print("Minutes : {} ".format(calc_mins(ms)))
print("Hours : {} ".format(calc_hrs(ms)))
print("Days : {} ".format(calc_days(ms)))
