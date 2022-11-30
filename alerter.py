alert_failure_count = 0
temperature_threshold = 100


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

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    print(returnCode)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1


alert_in_celcius(400.5)
alert_in_celcius(303.6)
assert(alert_failure_count == 0)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
