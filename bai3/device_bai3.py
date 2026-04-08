import paho.mqtt.client as mqtt

# =========================
# Cau hinh MQTT Broker
# =========================
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Ket noi MQTT broker thanh cong")
        client.subscribe(TOPIC_STATUS)
        print(f"Da subscribe topic trang thai: {TOPIC_STATUS}")
    else:
        print(f"Ket noi that bai, ma loi = {rc}")


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print("\nTrang thai nhan duoc:")
    print(payload)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print("Nhap lenh ON, OFF hoac EXIT")

    try:
        while True:
            command = input("Nhap lenh: ").strip().upper()

            if command == "EXIT":
                print("Ket thuc chuong trinh")
                break

            if command not in ["ON", "OFF"]:
                print("Lenh khong hop le. Vui long nhap ON, OFF hoac EXIT.")
                continue

            result = client.publish(TOPIC_CMD, command)
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"Da gui lenh {command} toi light01")
            else:
                print("Gui lenh that bai")

    except KeyboardInterrupt:
        print("\nDa dung controller")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()