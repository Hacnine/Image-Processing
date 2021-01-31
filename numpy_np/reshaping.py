import numpy as np

values = np.arange(12).reshape(4, 3)
print(values)
print("Col:", np.mean(values, axis=0))
print("Row", np.mean(values, axis=1))