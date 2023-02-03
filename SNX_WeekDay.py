from pandas_datareader import data
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

SNX = data.DataReader('^SNX', 'stooq', startTime, endTime)
print(SNX.info())
