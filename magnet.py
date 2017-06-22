import wiringpi as pi,time

hl_pin=17

pi.wiringPiSetupGpio()
pi.pinMode(hl_pin,0)
pi.pullUpDnControl(hl_pin,2)


while True:
	if(pi.digitalRead(hl_pin)==0):
		print("South Pole")
	else:
		print("North Pole")

	time.sleep(1)
