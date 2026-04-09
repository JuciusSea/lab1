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

![a9ec21068a540b0a5245](https://github.com/user-attachments/assets/de345721-3e82-4977-8c99-43cba8bb7280)

Terminal 2:
python publisher_bai1.py

![7bf799433211b34fea00](https://github.com/user-attachments/assets/8332cdda-c7e8-41b0-b171-a9c5d7af1702)


- Subscriber se lang nghe topic: iot/lab/message
- Publisher se gui thong diep len topic: iot/lab/message
- Noi dung gui kem ma sinh vien va ho ten sinh vien

Ket qua:
subcriber:

![ec5aca516103e05db912](https://github.com/user-attachments/assets/385041cc-54d7-4a73-9e29-29ec9454acd7)

publisher:

![ebaa184d4c10cd4e9401](https://github.com/user-attachments/assets/16a387cf-6a17-402b-a97a-fc161e25295a)

=== BAI 2: MO PHONG CAM BIEN NHIET DO, DO AM ===

Terminal 1:
python monitor_subscriber_bai2.py

Terminal 2:
python sensor_publisher_bai2.py

- Sensor Publisher gui du lieu moi 3 giay
- Topic gui: iot/lab/sensor01/data
- Du lieu gui o dang JSON

monitor_subcriber:

![ef840f455a18db468209](https://github.com/user-attachments/assets/2f878db1-87eb-45a6-9b5d-c65bbe1effd4)


sensor_publisher:

![17633211674ce612bf5d](https://github.com/user-attachments/assets/3f32f66a-386f-4652-aca8-bc07fa117e9c)


=== BAI 3: HE THONG DIEU KHIEN DEN THONG MINH ===

Terminal 1:
python device_bai3.py

![4ec98df5dca85df604b9](https://github.com/user-attachments/assets/7a6fa1b7-049d-4ca7-b521-bde492c93852)


Terminal 2:
python controller_bai3.py

![b0e590f7c1aa40f419bb](https://github.com/user-attachments/assets/58c777c4-7baf-4510-82d0-e89f72a5d51e)

- Device nhan lenh tu topic: iot/lab/light01/cmd
- Device gui trang thai len topic: iot/lab/light01/status
- Controller cho phep nhap lenh ON, OFF, EXIT



6. Ket qua dat duoc
- Ket noi thanh cong toi MQTT broker
- Publish va subscribe dung topic
- Gui nhan thong diep MQTT co ban
- Mo phong du lieu cam bien dang JSON
- Kiem tra canh bao nhiet do va do am
- Dieu khien thiet bi den thong minh theo mo hinh hai chieu
