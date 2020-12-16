import numpy as np
from datetime import datetime
import bubble_sort as bs


sort = np.random.randint(100,size=(100000))
start=datetime.now()
bs.bubble_sort(sort)
stop=datetime.now()
duration= stop-start
print('Time taken to sort:', duration)
