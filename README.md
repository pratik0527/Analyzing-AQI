# Analyzing-AQI

# Data collection
We are using Raspberry Pi device to collect the dataset.
We will use MQ sensors and DHT21 sensor to find Smoke, Methane, Carbon Monoxide, Temperature, Humidity and Air quality from the air.


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

