# الصورة الأساسية - Python خفيف
FROM python:3.11-slim

# معلومات
LABEL author="IoT Student"
LABEL description="Capteur IoT MQTT"

# مجلد العمل داخل الـ container
WORKDIR /app

# نسخ ملف المتطلبات أولاً
COPY requirements.txt .

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# نسخ كود الـ sensor
COPY sensor.py .

# الأمر الذي يشتغل عند تشغيل الـ container
CMD ["python", "sensor.py"]