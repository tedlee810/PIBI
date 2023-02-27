import numpy as np
import pandas as pd

# source: https://codepen.io/FelixRilling/pen/rNmZMP

# cols are offensive (attacking)
# rows are defensive (receiving)
type_chart = np.array([['','bug','dark','dragon','electric','fairy','fighting','fire','flying','ghost','grass','ground','ice','normal','poison','psychic','rock','steel','water'],
                       ['bug',1,1,1,1,1,0.5,2,2,1,0.5,0.5,1,1,1,1,2,1,1],
                       ['dark',2,0.5,1,1,2,2,1,1,0.5,1,1,1,1,1,0,1,1,1],
                       ['dragon',1,1,2,0.5,2,1,0.5,1,1,0.5,1,2,1,1,1,1,1,0.5],
                       ['electric',1,1,1,0.5,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1],
                       ['fairy',0.5,0.5,0,1,1,0.5,1,1,1,1,1,1,1,2,1,1,2,1],
                       ['fighting',0.5,0.5,1,1,2,1,1,2,1,1,1,1,1,1,2,0.5,1,1],
                       ['fire',0.5,1,1,1,0.5,1,0.5,1,1,0.5,2,0.5,1,1,1,2,1,1],
                       ['flying',0.5,1,1,2,1,0.5,1,1,1,0.5,0,2,1,1,1,2,1,1],
                       ['ghost',0.5,2,1,1,1,0,1,1,2,1,1,1,0,0.5,1,1,1,1],
                       ['grass',2,1,1,0.5,1,1,2,2,1,0.5,0.5,2,1,2,1,1,1,0.5],
                       ['ground',1,1,1,0,1,1,1,1,1,2,1,2,1,0.5,1,0.5,1,2],
                       ['ice',1,1,1,1,1,2,2,1,1,1,1,0.5,1,1,1,2,2,1],
                       ['normal',1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,1],
                       ['poison',0.5,1,1,1,0.5,0.5,1,1,1,0.5,2,1,1,0.5,2,1,1,1],
                       ['psychic',2,2,1,1,1,0.5,1,1,2,1,1,1,1,1,0.5,1,1,1],
                       ['rock',1,1,1,1,1,2,0.5,0.5,1,2,2,1,0.5,0.5,1,1,2,2],
                       ['steel',0.5,1,0.5,1,0.5,2,2,0.5,1,0.5,2,0.5,0.5,0,0.5,0.5,0.5,1],
                       ['water',1,1,1,2,1,1,0.5,1,1,2,1,0.5,1,1,1,1,0.5,0.5]
                       ])

type_chart = pd.DataFrame(data=type_chart[1:,1:],
                     index=type_chart[1:,0],
                     columns=type_chart[0,1:])

# transpose source type chart to make calculating types more intuitive (e.g., type_chart.loc['offensive','defensive'])
type_chart = type_chart.T

# print(type_chart)

# test statement
# print('rock against steel is: ' + type_chart.loc['rock','steel'])