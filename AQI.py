import Adafruit_DHT
import spidev
import time

# Define the DHT sensor type and GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT21
DHT_PIN = 4

# Define the SPI bus and device
spi = spidev.SpiDev()
spi.open(0, 0)

# Define function to read data from the MQ sensor
def read_mq_sensor(channel):
    adc_value = spi.xfer2([1, (8 + channel) << 4, 0])
    raw_value = ((adc_value[1] & 3) << 8) + adc_value[2]
    return raw_value

try:
    while True:
        # Read DHT21 sensor data
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

        # Read data from each MQ sensor
        mq2_data = read_mq_sensor(0)
        mq3_data = read_mq_sensor(1)
        mq4_data = read_mq_sensor(2)
        mq5_data = read_mq_sensor(3)
        mq135_data = read_mq_sensor(4)

        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%')
            print(f'MQ2: {mq2_data}, MQ3: {mq3_data}, MQ4: {mq4_data}, MQ5: {mq5_data}, MQ135: {mq135_data}')
        else:
            print('Failed to retrieve data from DHT sensor')

        time.sleep(2)  # Adjust the sleep duration as needed

except KeyboardInterrupt:
    spi.close()
    print('Exiting...')
