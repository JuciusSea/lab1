import paho.mqtt.client as mqtt
import json

# =========================
# Cau hinh MQTT Broker
# =========================
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"
DEVICE_ID = "light01"

light_status = "OFF"


def publish_status(client):
    payload = {
        "device_id": DEVICE_ID,
        "status": light_status
    }
    client.publish(TOPIC_STATUS, json.dumps(payload))
    print(f"Da gui trang thai: {payload}")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Ket noi MQTT broker thanh cong")
        client.subscribe(TOPIC_CMD)
        print(f"Da subscribe topic dieu khien: {TOPIC_CMD}")
        publish_status(client)
    else:
        print(f"Ket noi that bai, ma loi = {rc}")


def on_message(client, userdata, msg):
    global light_status

    command = msg.payload.decode("utf-8").strip().upper()
    print(f"Nhan lenh: {command}")

    if command == "ON":
        light_status = "ON"
        publish_status(client)
    elif command == "OFF":
        light_status = "OFF"
        publish_status(client)
    else:
        print("Lenh khong hop le. Chi chap nhan ON hoac OFF.")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    try:
        print("Smart Light Device dang chay. Nhan Ctrl+C de dung.")
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDa dung thiet bi")
        client.disconnect()


if __name__ == "__main__":
    main()