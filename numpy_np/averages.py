import numpy as np

values = np.arange(12).reshape(4, 3)
print(values)
# calculating mean means = average
print("Col:", np.mean(values, axis=0))
print("Row", np.mean(values, axis=1))

# average
print(['3*5+4*1+8*4/ 3'], np.average( values[1], weights=[.5, 1, 4]))