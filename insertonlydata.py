from influxdb import InfluxDBClient
import sched, time
import datetime
import random
import datetime as DT

client = InfluxDBClient(host='localhost', port=8086, username='root', password='root', database='example')
if client:
    print("Connect Complete !")
 
json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "1540611121.0468316",
        "fields": {
            "value": 0.75
        }
    }
]
client.write_points(json_body)
#result = client.query('select * from cpu;')
#print("Result: {0}".format(result))
#for x in result:
  #  print (x)