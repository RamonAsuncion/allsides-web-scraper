import time
import sys

width_max = 40

sys.stdout.write('[%s]' % ((' ') * width_max))
sys.stdout.flush()
sys.stdout.write('\b' * (width_max + 1))

for i in range(width_max):
    time.sleep(0.1)
    sys.stdout.write('#')
    sys.stdout.flush()

sys.stdout.write(']\n')
