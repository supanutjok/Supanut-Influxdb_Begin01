from influxdb import InfluxDBClient
import sched, time
import datetime
import random
import datetime as DT

client = InfluxDBClient(host='localhost', port=8086, username='root', password='root', database='example')
if client:
    print("Connect Complete !")


s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 

    seconds_since_epoch = time.time()
    DT.datetime.utcfromtimestamp(seconds_since_epoch)
    datetime.datetime.now()
    ai = DT.datetime.utcfromtimestamp(seconds_since_epoch).isoformat()

    temperature1 = random.uniform(10, 100)
    temperature = round(temperature1, 2)
    rd = random.uniform(0, 2)
    rd2 = round(rd ,2)
    print (rd2)
    json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": (ai+"Z"),
        "fields": {
        "value": (rd2),
        "temperature": (temperature)
        }
    }
]
    client.write_points(json_body)
    print(ai+"Z")
    #print (time.time())
    print (random.randint(1, 100))
    # do your stuff
    s.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()

#json_body = [
 #   {
  #      "measurement": "cpu_load_short",
   #     "tags": {
    #        "host": "server01",
     #       "region": "us-west"
      #  },
       # "time": "2009-11-10T23:10:00Z",
        #"fields": {
         #   "value": 1.20
        #}
    #}
#]
#client.write_points(json_body)
#result = client.query('select * from cpu;')
#print("Result: {0}".format(result))
#for x in result:
  #  print (x)