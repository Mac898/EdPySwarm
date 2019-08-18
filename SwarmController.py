import pigpio
import time

pi = pigpio.pi()

pulsetime = 0.0006
starttime = 0.005
gpiopin = 18
freq = 38000
full = 1000000
none = 0

def startIRPulse():
    pi.hardware_PWM(gpiopin, freq, full)
    time.sleep(pulsetime)
    pi.hardware_PWM(gpiopin, freq, none)
def oneIRPulse():
    pi.hardware_PWM(gpiopin, freq, full)
    time.sleep(pulsetime)
    time.sleep(pulsetime)
    pi.hardware_PWM(gpiopin, freq, none)
    time.sleep(pulsetime)
def zeroIRPulse():
    pi.hardware_PWM(gpiopin, freq, full)
    time.sleep(pulsetime)
    pi.hardware_PWM(gpiopin, freq, none)
    time.sleep(pulsetime)

def makeIRPulse(data):
    startIRPulse()
    for item in data:
        if item == 0:
            zeroIRPulse()
        if item == 1:
            oneIRPulse()

rawdata = input("Enter data, including inverted data.")
testdata = list(rawdata)
makeIRPulse(testdata)
