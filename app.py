
#!/usr/bin/python3
import os
from bottle import route, run, template
import datetime
import pytz

@route('/')

def index():
    """ The Main Page """
    dt = datetime.datetime.now()
    t1 = pytz.timezone('US/Eastern')
    t2 = int(t1.normalize(t1.localize(dt)).strftime('%I'))-1
    t3 = datetime.datetime.now(pytz.utc)
    t3format = t3.strftime("%H:%M")
    t3hour = int(t3.strftime("%H"))
    t4 = pytz.timezone('US/Pacific')
    utc = str(t3format)
    est = str(t1.normalize(t1.localize(dt)).strftime("%I:%M"))
    jmt = str(t2) + ":" + str(t1.normalize(t1.localize(dt)).strftime("%M"))
    pst = str(t4.normalize(t4.localize(dt)).strftime("%I:%M"))
    if 9 <= t3hour <= 17:
        work=1
    else:
        work=0

    info = {"title": "Joel's Presidental Platform",
            "utc": utc,
            "est": est,
            "jmt": jmt,
            "pst": pst,
            "work": work
    }
    
    return template("simple.tpl", info)

if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=argv[1])
    else:
        run(host='localhost', port=8080, debug=True)
