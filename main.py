import logging as log

def odejmowanie(a, b):
	return float(a-b)

def mnozenie(a,b):
	return float(a*b)

def dzielenie(a,b):
	if b!=0:
	  return a/b
	print("Nie można dzielić przez 0!")
	return None

def srednia():
	log.warning('Uwaga')

