import wiringpi as pi, time

led_pin=23
#  23 pin (GPIO number to connect to LED )

pi.wiringPiSetupGpio()
pi.pinMode(led_pin,1)

while True:
	pi.digitalWrite(led_pin,1)
	time.sleep(1)
	pi.digitalWrite(led_pin,0)
	time.sleep(1)
