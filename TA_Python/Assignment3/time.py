from time import time
from time import ctime

seconds = time()
print(f'Time in floating point: {seconds}')

f = ctime(seconds)
print(f'Time in d-m-y format: {f}')


