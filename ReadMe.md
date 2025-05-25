****"🌬️ GaurdianAir – VOC Detector for Raspberry Pi 5"****

---

description: |
  GaurdianAir is a smart **Volatile Organic Compound (VOC) detector** using the **Raspberry Pi 5**, **SenseHat**, and **MQ-135 sensor**.
  It monitors air quality in real-time and visualizes data through interactive graphs on a sleek dashboard powered by **Flask**.

---

overview: |
  GaurdianAir empowers users to track air quality efficiently, helping identify harmful organic compounds.
  Designed for Raspberry Pi 5 with SenseHat, it uses sensor data processed with RTIMULib to provide accurate readings.
  The Flask dashboard displays the data live, making it easy to monitor and analyze VOC levels.

---

features:
  - "🌡️ Real-time VOC detection with MQ-135 sensor"
  - "📊 Interactive Flask dashboard for data visualization"
  - "🔧 Easy setup with virtual environment support"
  - "🖥️ Raspberry Pi 5 optimized"

---

built_with:
  - "🐍 Python 3"
  - "🎛️ SenseHat + MQ-135 Sensor"
  - "🖥️ Flask Web Framework"
  - "📈 Matplotlib / Plotly (for graphing)"
  - "🔧 RTIMULib for sensor data"
  - "🐧 Raspberry Pi OS"

---

security_notice: |
  ⚠️ **Important:**  
  Sensitive files such as the Firebase **ServiceAccountKey** are **NOT** included in this repository and should **never** be shared publicly.  
  Users must obtain their own keys and configure them locally to keep the project secure.

---

problems_encountered: |
  Due to the Raspberry Pi 5’s security limitations with Firebase, direct use of Firebase libraries was unreliable.
  To mitigate this, the application runs inside a **Python virtual environment** to isolate dependencies and improve stability.  
  Additionally, the project uses **LGPIO** instead of the default **RPi.GPIO** library because of compatibility and performance issues on the Pi 5.

---

RTIMU: |
  ModuleNotFoundError: No module named 'RTIMU' - this may appear as I could not push the RTIMU files to GitHub as it is in itself a GIT repository.
  This will need to be installed to run the code also. 

---

author:
  name: "Jason Price"
  role: "Final Year BSc. (Hons) Internet Systems Development student"
  location: "Ireland"
  linkedin: "https://www.linkedin.com/in/jasonpricedev/"
