# Analyzing-AQI


# Description:
The "Air Quality Monitoring and Analysis with Raspberry Pi and AWS" project aims to create a comprehensive system for monitoring, data collection, ETL (Extract, Transform, Load), and visualization of air quality in the city. Poor air quality is a critical global issue, and this project addresses it by leveraging the capabilities of Raspberry Pi for data collection and AWS for data processing and analysis.


# Data collection
We are using a Raspberry Pi device to collect the dataset.
We will use MQ sensors and DHT21 sensors to find Smoke, Methane, Carbon Monoxide, Temperature, Humidity, and Air quality from the air.


# Hardware:
- Raspberry PI
- MQ Sensors (MQ2, MQ3, MQ4, MQ5, MQ135)
- DHT21 Sensor (Temperature and humidity sensor)
- MCP3008 ADC
- Breadboard
- Jumper wires


# Connections:
**DHT21 Sensor:**
- VCC to 3.3V on Raspberry Pi
- Data to GPIO pin (GPIO 4)
- GND to GND on Raspberry Pi

**MCP3008 ADC:**
- VDD to 3.3V on Raspberry Pi
- VREF to 3.3V on Raspberry Pi
- AGND to GND on Raspberry Pi
- DGND to GND on Raspberry Pi
- CLK to SPI0 SCLK (GPIO 11)
- DOUT to SPI0 MISO (GPIO 9)
- DIN to SPI0 MOSI (GPIO 10)
- CS/SHDN to GPIO pin (GPIO 8)
- MCP3008 CH0 to the analog output of your MQ sensors.

**MQ Sensors (for each sensor):**
- AOUT pin of each MQ sensor to an analog channel of the MCP3008.
- GND of each MQ sensor to the GND on the breadboard.
- VCC of each MQ sensor to the VCC on the breadboard.


**MQ Sensors Amazon URL:**
https://www.amazon.com/Detection-Sensor-Module-MQ-135-Arduino/dp/B092L81VXB/ref=sr_1_1_sspa?keywords=mq+sensors&qid=1700498217&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1



