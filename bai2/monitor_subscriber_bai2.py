import paho.mqtt.client as mqtt
import json
import random
import time

# =========================
# Cau hinh MQTT Broker
# =========================
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"
DEVICE_ID = "sensor01"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Ket noi MQTT broker thanh cong")
    else:
        print(f"Ket noi that bai, ma loi = {rc}")


def generate_sensor_data():
    data = {
        "device_id": DEVICE_ID,
        "temperature": round(random.uniform(25.0, 40.0), 1),
        "humidity": round(random.uniform(30.0, 80.0), 1)
    }
    return data


def main():
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(BROKER, PORT, 60)
    client.loop_start()

    try:
        while True:
            data = generate_sensor_data()
            payload = json.dumps(data)

            result = client.publish(TOPIC, payload)
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"Da gui: {payload}")
            else:
                print("Gui that bai")

            time.sleep(3)

    except KeyboardInterrupt:
        print("\nDa dung sensor publisher")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()