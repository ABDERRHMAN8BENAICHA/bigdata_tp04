class SensorData:
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f"Temperature={self.value}°C"