from __init__ import *

def network_alert_stub(celcius):
    global temperature_threshold
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    alert_check = 200
    if celcius > temperature_threshold:
        alert_check = 500
    return alert_check