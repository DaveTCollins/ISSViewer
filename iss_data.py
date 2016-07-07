import json
import requests
import sched, time

s = sched.scheduler(time.time, time.sleep)

def get_position():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    data = json.loads(r.text)
    print data['iss_position']['latitude']
    print data['iss_position']['longitude']

while True:
    get_position()
    time.sleep(5)

