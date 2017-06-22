import wiringpi as pi,time

import os,struct

import datetime

pi.wiringPiSetup()
i2c=pi.I2C()

temp_dev=i2c.setup(0x48)

i2c.writeReg8(temp_dev,0x03,0x80)
# ADT7410 is broken (because of an electrical short circuit )
# But, ADT7410 indicated any temperature.i dont know what causes an electrical short circuit.
while True:
	temp_data=struct.unpack('2B',os.read(temp_dev,2))
	temp=((temp_data[0] << 8) + temp_data[1])

	if(temp_data[0] >= 0x80):
		temp=temp-65536
	temp=temp/128
	date=time
	print("Time:",datetime.datetime.now())
	print("Temperature:",temp,"C")
	print("")
	time.sleep(60*60)
