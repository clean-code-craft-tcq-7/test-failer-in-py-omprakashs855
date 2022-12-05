from __init__ import *
from alerter_network_stub import network_alert_stub

def alert_in_celcius(farenheit):
    global threshold_record_list
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 1
        threshold_record_list.append(returnCode)

def alerter_test():
    global threshold_record_list
    threshold_record_list = []
    alert_in_celcius(400.5)
    alert_in_celcius(303.6)
    # Test less than 100 celius
    alert_in_celcius(100)
    # Test 100 celcius
    alert_in_celcius(212)
    assert(alert_failure_count == threshold_record_list.count(500))
    print(f'{alert_failure_count} alerts failed.')
    return True

if alerter_test():
    print('All is well (maybe!)')
