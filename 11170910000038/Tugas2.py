import time
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    # handle failed import
    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.output(12, GPIO.HIGH)
print("Led 1 must be on")
time.sleep(1)
print("Led 1 must be off")
GPIO.output(12, GPIO.LOW)

GPIO.output(16, GPIO.HIGH)
print("Led 2 must be on")
time.sleep(1)
print("Led 2 must be off")
GPIO.output(16, GPIO.LOW)

GPIO.output(18, GPIO.HIGH)
print("Led 3 must be on")
time.sleep(1)
print("Led 3 must be off")
GPIO.output(18, GPIO.LOW)

GPIO.cleanup()