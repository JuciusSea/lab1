import paho.mqtt.client as mqtt
from datetime import datetime

# =========================
# Cau hinh MQTT Broker
# =========================
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Ket noi MQTT broker thanh cong")
        client.subscribe(TOPIC)
        print(f"Da subscribe topic: {TOPIC}")
    else:
        print(f"Ket noi that bai, ma loi = {rc}")


def on_message(client, userdata, msg):
    receive_time = datetime.now().strftime("%H:%M:%S")
    payload = msg.payload.decode("utf-8")

    print("\nNhan duoc message:")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {payload}")
    print(f"Time: {receive_time}")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    try:
        print("Subscriber dang chay. Nhan Ctrl+C de dung.")
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDa dung subscriber")
        client.disconnect()


if __name__ == "__main__":
    main()