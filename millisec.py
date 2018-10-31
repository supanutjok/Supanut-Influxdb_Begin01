import threading
import time
from influxdb import InfluxDBClient
import sched
import datetime
import random
import datetime as DT

client = InfluxDBClient(host='localhost', port=8086, username='root', password='root', database='example')
if client:
    print("Connect Complete !")

def hello(*args):
    #print(str(time.ctime()))

    seconds_since_epoch = time.time()
    DT.datetime.utcfromtimestamp(seconds_since_epoch)
    datetime.datetime.now()
    ai = DT.datetime.utcfromtimestamp(seconds_since_epoch).isoformat()

    temperature1 = random.uniform(10, 100)
    temperature = round(temperature1, 2)

    ram_load = random.randint(20, 100)
    #ram_load2 = round(ram_load, 2)

    ram_temp = random.uniform(1, 120)
    ram_temp2 = round(ram_temp, 2)

    rd = random.uniform(0, 2)
    rd2 = round(rd ,2)
    print (rd2)


    json_body = [
    {
        "measurement": "cpu_load",
        "tags": {
            "host": "server02",
            "region": "Thailand"
        },
        "time": (ai+"Z"),
        "fields": {
        "value": (rd2),
        "temperature": (temperature)
        },
        "measurement": "ram_load",
        "tags": {
            "host": "server02",
            "region": "Thailand"
        },
        "time": (ai+"Z"),
        "fields": {
        "value": (ram_load),
        "temperature": (ram_temp2)
        }

    }
]
    client.write_points(json_body)
    print(ai+"Z")
    #print (time.time())
    print (random.randint(1, 100))
    #next=int(args[0])+1
    threading.Timer(0.1, hello,[str(next)]).start()

hello()