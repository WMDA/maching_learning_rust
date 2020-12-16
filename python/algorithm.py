import numpy as np
from datetime import datetime
import bubble_sort as bs
import argparse

def list_length():
    parse = argparse.ArgumentParser()
    parse.add_argument("-l", dest="length", help="Number of iterations")
    options= parse.parse_args()
    if not options.length:
        parse.error('>> Needs length of list.')
    else:
        return options

options=list_length()
print('list length ' + options.length)
sort = np.random.randint(100,size=(int(options.length)))
start=datetime.now()
x=bs.bubble_sort(sort)
stop=datetime.now()
duration= stop-start
print('Time taken to sort:', duration)
