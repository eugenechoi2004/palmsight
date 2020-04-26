import serial
from redis import Redis

cli = Redis("localhost")
ser = serial.Serial('/dev/serial0', 115200)


