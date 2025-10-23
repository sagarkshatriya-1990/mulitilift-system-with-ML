# 🚀 Smart Lift System using ESP32, Python & OpenCV

A prototype of an **intelligent, camera-based crowd-aware elevator system** built using **ESP32**, **Arduino C**, **Python**, and **OpenCV**. This system automatically detects the most crowded floor using live camera feeds and navigates the lift to serve that floor. Once the task is done, the lift returns to the ground floor, simulating an efficient smart building infrastructure.

---

## 📌 Key Features

- 🧠 **Crowd Detection** using OpenCV and Haar Cascade classifier.
- 🔁 **Lift Navigation** logic controlled by ESP32 and DC gear motor.
- 📡 **HTTP-based Wi-Fi Communication** between Python and ESP32.
- 🌐 **Built-in Web Server** hosted on ESP32 to receive floor requests.
- 🔦 **LED Indicators** to show lift’s current position (per floor).
- 🧲 **Reed Switches** with magnets to accurately detect floor stops.
- 🛠️ **Modular & Scalable** setup allowing multiple cameras and floors.

---

## 🖼️ Real-World Applications

- 🏥 **Hospitals**: Prioritize floors with more patients/staff waiting.
- 🏫 **Schools/Colleges**: Smart elevator scheduling during class hours.
- 🏢 **Smart Offices**: Improve elevator efficiency in peak times.
- 🏬 **Shopping Malls**: Crowd handling during rush hours.

---

## 🛠️ Hardware Components

| Component              | Quantity | Description                            |
|------------------------|----------|----------------------------------------|
| ESP32 Dev Board        | 1        | Main controller, Wi-Fi capable         |
| DC Gear Motor          | 1        | Drives lift movement                   |
| L298N Motor Driver     | 1        | Controls motor direction/speed         |
| Reed Switches          | 3        | Floor detection via magnetic sensors   |
| LEDs                   | 3        | Indicate lift location                 |
| Magnets                | 3        | Activate reed switches per floor       |
| Jumper Wires, Breadboard | -      | Prototyping                            |
| Power Supply           | 1        | Motor and ESP32 powering               |

---

## 💻 Software & Libraries

- **Arduino IDE** – For ESP32 programming
- **Python 3.x**
- **OpenCV** (`cv2`) – For face detection
- **`requests`** – For HTTP requests to ESP32
- **Haar Cascade** – Pre-trained face detection model

## 📁 File Structure

```
Smart-Lift-System/
├── ArduinoCode.txt                  # ESP32 lift control logic (Arduino C)
├── crowd.py                         # Python script for face detection using laptop cameras
├── model/
│   └── haarcascade_frontalface_default.xml  # Haar Cascade model for face detection
└── README.md                        # Project documentation
```


## ⚙️ Setup Instructions

### 1. 🔌 Upload ESP32 Code

- Open `ArduinoCode.txt` in Arduino IDE.
- Go to **Tools > Board > ESP32 Dev Module** (install ESP32 core if needed).
- Update your Wi-Fi `ssid` and `password`.
- Connect and upload the code to ESP32.
- Open **Serial Monitor** to note the IP address after connection.

### 2. 🧠 Configure Python Script

- Ensure camera access is working (built-in or external webcam).
- Place the `haarcascade_frontalface_default.xml` inside the `model/` folder.
- Open `crowd.py` and set:
- esp_ip = 'http://<ESP32_IP>'  # Replace with ESP32 IP address
- floor = 0  # Change this per device (0, 1, 2)

### 3. 📦 Install Dependencies

- pip install opencv-python requests

### 4. ▶️ Run the Script

- python crowd.py

## 🔄 Working Mechanism

- Each laptop (placed on a floor) runs crowd.py and uses a webcam to detect the number of faces.
  
- If detected crowd ≥ 2, it sends an HTTP request like:
- http://<ESP32_IP>/floor0?count=3
- ESP32 collects requests from all floors and determines the most crowded one.

- Using a DC motor (controlled by L298N), the lift moves to that floor.

- Reed switches help detect when the lift reaches the target floor.

- After servicing, the lift automatically returns to floor 0.

## 📉 System Block Diagram (Textual Description)

```
+------------------+      HTTP POST      +------------------+
| Python (crowd.py)| ------------------> | ESP32 Web Server |
| OpenCV Face Count|                     | Processes Floor  |
+------------------+                     | Requests & Moves |
                                         | Lift via Motor   |
                                         +--------+---------+
                                                  |
                          +------------------------+------------------------+
                          |                        |                        |
                   [Motor Driver]         [Reed Switch System]       [LEDs per Floor]
                   [DC Gear Motor]        [Floor Detection]         [Lift Position]
```

## 📈 Performance Observations

- ✅ Reliable up to 3 floors.
- 💡 Face detection works best with proper lighting.
- ⚡ Low latency in Wi-Fi HTTP communication.
- 🧲 Magnet-reed switch detection offers decent positional accuracy.

## 🌱 Future Enhancements

- 🔊 Voice Command Integration using Google Assistant.
- 🧍‍♂️ People Counting with YOLO or advanced deep learning models.
- 📲 Mobile App to remotely call the lift.
- 🧭 Shortest Path Optimization for multi-lift systems.
- 🔒 Access Control with RFID for secure floor entry.

## 🧠 Learnings & Skills Applied

- Internet of Things (IoT) communication
- Real-time computer vision with Python
- Embedded systems and motor control
- HTTP protocol and web server handling on ESP32
- Sensor integration and hardware debugging

## 📬 Contributing
- Have suggestions or want to extend this project?
- Feel free to fork, clone, or raise an issue.
- Pull requests are welcome!

## 📄 License
- This project is open-source and available under the MIT License.
