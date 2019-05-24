import pandas as pd
import numpy as np

from matplotlib import pyplot

series1 = pd.Series([10,20,30,40])

print(series1)

a = pd.DataFrame(np.random.rand(15,4), columns=['v','w','x','y'])

a.plot.area()
pyplot.show()