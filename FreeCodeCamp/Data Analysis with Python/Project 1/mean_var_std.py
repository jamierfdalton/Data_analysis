import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    calculations = {
      'mean': [],
      'variance': [],
      'standard deviation': [],
      'max':[],
      'min':[],
      'sum':[]
    }

    series = np.array([list[:3],list[3:6],list[6:]])

    meanY = []
    varY = []
    stdY = []
    maxY = []
    minY = []
    sumY = []

    meanX = []
    varX = []
    stdX = []
    maxX = []
    minX = []
    sumX = []

    i = 0

    while i < len(series):
        meanY.append(series[:,i].mean())
        varY.append(series[:,i].var())
        stdY.append(series[:,i].std())
        maxY.append(series[:,i].max())
        minY.append(series[:,i].min())
        sumY.append(series[:,i].sum())
        i += 1

    for i in series:
        meanX.append(i.mean())
        varX.append(i.var())
        stdX.append(i.std())
        maxX.append(i.max())
        minX.append(i.min())
        sumX.append(i.sum())

    calculations['mean'].append(meanY)
    calculations['mean'].append(meanX)
    calculations['mean'].append(series.mean())
    calculations['variance'].append(varY)
    calculations['variance'].append(varX)
    calculations['variance'].append(series.var())
    calculations['standard deviation'].append(stdY)
    calculations['standard deviation'].append(stdX)
    calculations['standard deviation'].append(series.std())
    calculations['max'].append(maxY)
    calculations['max'].append(maxX)
    calculations['max'].append(series.max())
    calculations['min'].append(minY)
    calculations['min'].append(minX)
    calculations['min'].append(series.min())
    calculations['sum'].append(sumY)
    calculations['sum'].append(sumX)
    calculations['sum'].append(series.sum())
    return calculations
