import paho.mqtt.client as mqtt
from datetime import datetime

# =========================
# Cau hinh MQTT Broker
# =========================
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"

HO_TEN = "Le Minh Hai"
MA_SV = "B21DCCN317"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Ket noi MQTT broker thanh cong")
    else:
        print(f"Ket noi that bai, ma loi = {rc}")


def main():
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print("Nhap noi dung can gui. Nhap 'exit' de thoat.")

    while True:
        msg = input("Nhap message: ").strip()
        if msg.lower() == "exit":
            break

        if not msg:
            msg = "Xin chao tu client Python MQTT"

        payload = f"{msg} - {MA_SV} - {HO_TEN}"
        result = client.publish(TOPIC, payload)

        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"[{now}] Da gui: {payload}")
        else:
            print("Gui that bai")

    client.loop_stop()
    client.disconnect()
    print("Da ngat ket noi")


if __name__ == "__main__":
    main()