import paho.mqtt.client as mqtt
import json

# =========================
# Cau hinh MQTT Broker
# =========================
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Ket noi MQTT broker thanh cong")
        client.subscribe(TOPIC)
        print(f"Da subscribe topic: {TOPIC}")
    else:
        print(f"Ket noi that bai, ma loi = {rc}")


def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)

        device_id = data.get("device_id", "unknown")
        temperature = data.get("temperature", 0)
        humidity = data.get("humidity", 0)

        print("\n==============================")
        print(f"Device: {device_id}")
        print(f"Temperature: {temperature} C")
        print(f"Humidity: {humidity} %")

        if temperature > 35:
            print("CANH BAO: Nhiet do cao")

        if humidity < 40:
            print("CANH BAO: Do am thap")

        print("==============================")

    except json.JSONDecodeError:
        print("Loi: Payload khong phai JSON hop le")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    try:
        print("Monitoring subscriber dang chay. Nhan Ctrl+C de dung.")
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDa dung monitoring subscriber")
        client.disconnect()


if __name__ == "__main__":
    main()