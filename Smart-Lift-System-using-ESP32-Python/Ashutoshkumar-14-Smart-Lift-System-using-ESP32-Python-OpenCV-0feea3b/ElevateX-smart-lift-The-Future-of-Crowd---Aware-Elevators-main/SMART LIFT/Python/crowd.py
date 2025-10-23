import cv2
import time
import requests  # <-- added for HTTP request

# ========== CONFIGURATION ==========
esp_ip = "http://10.67.132.59"  # 🔁 Replace with your ESP32 IP
floor = 2                      # 🔁 Change for each laptop (1, 2, or 3)
crowdDef = 2                   # Number of people to trigger alert
send_interval = 3             # Seconds between ESP32 updates
# ====================================

face_cascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

crowdCount = 0
last_sent = 0

while True:
    crowdCount = 0
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    img2 = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        crowdCount += 1

    print("Crowd Count")
    print(crowdCount)

    if crowdCount >= crowdDef:
        print("Crowd recorded")
        crowdDetectedFile = "crowd-detected-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"
        cv2.imwrite(crowdDetectedFile, img)
        print("Crowd alert")

    # 🟢 Send to ESP32 every send_interval seconds
    if time.time() - last_sent > send_interval:
        try:
            url = f"{esp_ip}/floor{floor}?count={crowdCount}"
            requests.get(url)
            print(f"Sent to ESP32: {url}")
            last_sent = time.time()
        except Exception as e:
            print("⚠ Error sending to ESP32:", e)

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()