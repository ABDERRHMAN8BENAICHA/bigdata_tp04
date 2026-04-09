from domain.entities import SensorData

class ProcessSensorData:
    def execute(self, raw_data: str) -> SensorData:
        value = int(raw_data)

        # تحويل إلى voltage
        voltage = value * (5.0 / 1023.0)

        # LM35: تحويل إلى درجة حرارة
        temperature = voltage * 100

        return SensorData(round(temperature, 2))