import csv
import time
import threading
from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials, db
from gpiozero import DigitalInputDevice, OutputDevice, Device
from gpiozero.pins.lgpio import LGPIOFactory

# Using LGPIO as RPi.GPIO does not run well on virtual environment
Device.pin_factory = LGPIOFactory()

# Assigning pin 17 to the buzzer
BUZZER_PIN = 17
buzzer = OutputDevice(BUZZER_PIN)

# Initializing SenseHat
sense = SenseHat()

# Initializing MQ-135 sensor on GPIO 4
mq135_sensor = DigitalInputDevice(4)

# Setting up Firebase
cred = credentials.Certificate("/home/k00268716/python/firestore/GaurdianAir/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://futtechproj-default-rtdb.europe-west1.firebasedatabase.app'
})

# Referencing air quality data in Firebase
air_quality_ref = db.reference('/air_quality_data')

# Referencing alarm trigger in Firebase
alarm_ref = db.reference('alarm')

# Function to monitor alarm status and control the buzzer
def monitor_alarm():
    print("Monitoring for alarm...")
    prev_state = None
    while True:
        try:
            # Fetching the alarm state
            state = alarm_ref.get()
            
            # Get the state of "triggered"
            triggered = state.get('triggered', False)

            # Check if alarm state is triggered
            if triggered:
                buzzer.on()  # Turn on buzzer
                print("Alarm ON")
            else:
                buzzer.off()  # Turn off buzzer
                print("Alarm OFF")

            # Only print if the alarm state has changed
            if triggered != prev_state:
                print(f"Alarm status changed: {'ON' if triggered else 'OFF'}")
                prev_state = triggered

            time.sleep(1)

        except KeyboardInterrupt:
            # CTRL + C to interrupt code
            print("\nCTRL + C pressed. Turning off buzzer and exiting...")
            buzzer.off()  # Turn off the buzzer
            break  # Exit the loop
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)

    buzzer.close()

# Function to log sensor data and push it to Firebase
def log_sensor_data():
    csv_filename = "sensor_data.csv"
    try:
        with open(csv_filename, mode="r") as file:
            pass
    except FileNotFoundError:
        with open(csv_filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)", "Pressure (hPa)", "Air Quality (VOC)"])

    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.writer(file)

        while True:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            # Read Sense HAT data
            temperature = round(sense.get_temperature(), 2)
            humidity = round(sense.get_humidity(), 2)
            pressure = round(sense.get_pressure(), 2)

            # Read air quality from MQ-135
            air_quality = mq135_sensor.value  # 1 = Clean, 0 = Pollution Detected

            # Write to CSV file
            writer.writerow([timestamp, temperature, humidity, pressure, "Clean" if air_quality else "Pollution Detected"])

            file.flush()  # Ensure it's saved

            # Push to Firebase
            data = {
                'timestamp': timestamp,
                'temperature': temperature,
                'humidity': humidity,
                'pressure': pressure,
                'air_quality': "Clean" if air_quality else "Pollution Detected"
            }
            air_quality_ref.push(data)

            print(f"📤 Logged: {data}")

            time.sleep(300)  # Set to 5 mins before another check

if __name__ == "__main__":
    # Start the alarm monitoring and sensor logging in parallel
    alarm_thread = threading.Thread(target=monitor_alarm)
    sensor_thread = threading.Thread(target=log_sensor_data)

    # Start both threads
    alarm_thread.start()
    sensor_thread.start()

    # Wait for both threads to finish 
    alarm_thread.join()
    sensor_thread.join()