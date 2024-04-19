import serial
import time

try:
    # Open the serial port (change the port name as per your system)
    ser = serial.Serial('/dev/tty.usbmodem14201', 9600)  # Change 'COM4' to your Arduino's port

    # Delay to let Arduino initialize
    time.sleep(2)

    # Continuously send the command to turn on the LED
    while True:
        ser.write(b'1')  # Send the command to turn on the LED
        time.sleep(1)    # Delay for 1 second before sending the next command

except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the serial port when done or when an error occurs
    ser.close()
