import wiringpi as pi,time

bt_pin=17

pi.wiringPiSetupGpio()
pi.pinMode(bt_pin,0)

pi.pullUpDnControl(bt_pin,2)

while True:
	if(pi.digitalRead(bt_pin)==0):
		print("Switch ON")
	else:
		print("Switch OFF")

	time.sleep(1)
