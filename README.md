HUONG DAN CHAY BAI THUC HANH MQTT BANG PYTHON

Thong tin sinh vien:
- Ho va ten: Le Minh Hai
- Ma sinh vien: B21DCCN317

1. Moi truong yeu cau
- Python 3.x
- Thu vien paho-mqtt
- IDE hoac VS Code

2. Cai dat thu vien
Mo terminal va chay lenh:
pip install paho-mqtt

3. MQTT Broker su dung
- Broker: broker.hivemq.com
- Port: 1883

Day la public broker, khong can tao tai khoan de test co ban.

4. Danh sach file
- publisher_bai1.py
- subscriber_bai1.py
- sensor_publisher_bai2.py
- monitor_subscriber_bai2.py
- device_bai3.py
- controller_bai3.py

5. Cach chay tung bai

=== BAI 1: GUI VA NHAN THONG DIEP CO BAN ===

Terminal 1:
python subscriber_bai1.py

Terminal 2:
python publisher_bai1.py

- Subscriber se lang nghe topic: iot/lab/message
- Publisher se gui thong diep len topic: iot/lab/message
- Noi dung gui kem ma sinh vien va ho ten sinh vien

Vi du payload:
Xin chao tu client Python MQTT - B21DCCN317 - Le Minh Hai

=== BAI 2: MO PHONG CAM BIEN NHIET DO, DO AM ===

Terminal 1:
python monitor_subscriber_bai2.py

Terminal 2:
python sensor_publisher_bai2.py

- Sensor Publisher gui du lieu moi 3 giay
- Topic gui: iot/lab/sensor01/data
- Du lieu gui o dang JSON

Vi du:
{
  "device_id": "sensor01",
  "temperature": 36.1,
  "humidity": 38.7
}

- Neu nhiet do > 35 do C thi hien canh bao nhiet do cao
- Neu do am < 40% thi hien canh bao do am thap

=== BAI 3: HE THONG DIEU KHIEN DEN THONG MINH ===

Terminal 1:
python device_bai3.py

Terminal 2:
python controller_bai3.py

- Device nhan lenh tu topic: iot/lab/light01/cmd
- Device gui trang thai len topic: iot/lab/light01/status
- Controller cho phep nhap lenh ON, OFF, EXIT

Vi du:
Nhap lenh: ON
Da gui lenh ON toi light01

Trang thai nhan duoc:
{"device_id": "light01", "status": "ON"}

6. Ket qua dat duoc
- Ket noi thanh cong toi MQTT broker
- Publish va subscribe dung topic
- Gui nhan thong diep MQTT co ban
- Mo phong du lieu cam bien dang JSON
- Kiem tra canh bao nhiet do va do am
- Dieu khien thiet bi den thong minh theo mo hinh hai chieu

7. Luu y
- Co the thay doi broker trong tung file neu muon dung broker khac
- Neu public broker dong nguoi dung, co the doi topic thanh topic rieng de tranh trung du lieu
- Nen mo 2 terminal khac nhau de test publisher/subscriber hoac device/controller