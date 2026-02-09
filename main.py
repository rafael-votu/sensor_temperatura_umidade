import dht
import machine
from time import sleep

pinsensor = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
sensor = dht.DHT22(pinsensor)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        umid = sensor.humidity()
        print(f"Temperatura: {temp} °C")
        print(f"Umidade: {umid} %")
        print("___________________________________________________________________")
    except Exception as e:
        print(f"Erro na leitura: {e}")
    
    sleep(2)