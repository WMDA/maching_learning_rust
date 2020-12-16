import numpy as np
from datetime import datetime
import bubble_sort as bs
import argparse
import sys

def list_length():
    parse = argparse.ArgumentParser()
    parse.add_argument("-l", dest="length", help="Needs number of values to sort")
    options= parse.parse_args()
    if not options.length:
        parse.error('>> Needs number of values to sort.')
    else:
        return options


options=list_length()

try:
    length=int(options.length)
    print('list length ' + options.length)
    sort = np.random.randint(100,size=(length))
    try:
        start=datetime.now()
        bs.bubble_sort(sort)
        stop=datetime.now()
        duration= stop-start
        print('Time taken to sort:', duration)
    except KeyboardInterrupt:
        print('\nUser requested shut down')
        sys.exit()
except ValueError:
    print('>> ERROR: Please enter a number')
    sys.exit()
