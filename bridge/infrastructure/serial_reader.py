import serial

class SerialReader:
    def __init__(self, port: str, baudrate: int = 9600):
        self.ser = serial.Serial(port, baudrate)

    def read(self) -> str:
        return self.ser.readline().decode().strip()