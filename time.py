import sched, time
import datetime
import random
import datetime as DT


#seconds_since_epoch = time.time()
#DT.datetime.utcfromtimestamp(seconds_since_epoch)
##datetime.datetime.now()
#ai = DT.datetime.utcfromtimestamp(seconds_since_epoch).isoformat()
#print(ai+"Z")

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    #print ("Doing stuff...")
    print (time.time())

    seconds_since_epoch = time.time()
    DT.datetime.utcfromtimestamp(seconds_since_epoch)
    datetime.datetime.now()
    ai = DT.datetime.utcfromtimestamp(seconds_since_epoch).isoformat()
    print(ai+"Z")


    print (datetime.datetime.strptime)
    rd = random.uniform(0, 2)
    rd2 = round(rd ,2)
    print (rd2)
    
     #do your stuff
    s.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()