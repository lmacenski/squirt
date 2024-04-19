# Import the necessary Nanpy module
from nanpy import ArduinoApi, SerialManager

# Initialize the connection to the Arduino (adjust the port if needed)
try:
    connection = SerialManager(device='/dev/ttyUSB1')  # Change the port as necessary
    a = ArduinoApi(connection=connection)
    print("hi")

except:
    print('Connection failed. Check your setup.')