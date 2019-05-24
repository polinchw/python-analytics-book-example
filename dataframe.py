import pandas as pd
import numpy as np

from matplotlib import pyplot

a = pd.DataFrame(np.random.rand(15,4), columns=['v','w','x','y'])

a.plot.area()
pyplot.show()