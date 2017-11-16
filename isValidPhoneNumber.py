import re
phone_number=str(raw_input("enter phone number\n"))
s=re.search(r"[1]?[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-]?\d{4}",phone_number)
def main():
	
	if len(phone_number)==12 :
		validNumber()
	elif len(phone_number)==14 :
		validNumber()
	elif len(phone_number)==10 :
		validNumber()
	elif len(phone_number)==16 :
		validNumber()
	elif len(phone_number)==11 :
		validNumber()
	else:
		print "invalid phone number"
def validNumber():
	try:
		a=s.group(0)
		if a==phone_number:
			print "valid phone number"
		else:
			print "invalid phone number"

	except AttributeError:
 		print "invalid phone number"
main()
