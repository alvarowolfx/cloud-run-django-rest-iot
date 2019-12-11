import sys
from sensor import wifi_connect, send_data, get_distance, show_error, deep_sleep

try:
    wifi_connect()

    samples = 10
    distance = 0
    for i in range(0, samples):
        distance += get_distance()

    distance = distance/10
    print('Distance = {}cm'.format(distance))
    data = {'distance': distance}
    send_data(data)

except Exception as exc:
    sys.print_exception(exc)
    show_error()

deep_sleep()
