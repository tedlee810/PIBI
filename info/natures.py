import numpy as np
import pandas as pd

nature_chart = np.array([['','attack','defense','special-attack','special-defense','speed'],
                         ['hardy',1,1,1,1,1],
                         ['lonely',1.1,0.9,1,1,1],
                         ['brave',1.1,1,1,1,0.9],
                         ['adamant',1.1,1,0.9,1,1],
                         ['naughty',1.1,1,1,0.9,1],
                         ['bold',0.9,1.1,1,1,1],
                         ['docile',1,1,1,1,1],
                         ['relaxed',1,1.1,1,1,0.9],
                         ['impish',1,1.1,0.9,1,1],
                         ['lax',1,1.1,1,0.9,1],
                         ['timid',0.9,1,1,1,1.1],
                         ['hasty',1,0.9,1,1,1.1],
                         ['serious',1,1,1,1,1],
                         ['jolly',1,1,0.9,1,1.1],
                         ['naive',1,1,1,0.9,1.1],
                         ['modest',0.9,1,1.1,1,1],
                         ['mild',1,0.9,1.1,1,1],
                         ['quiet',1,1,1.1,1,0.9],
                         ['bashful',1,1,1,1,1,],
                         ['rash',1,1,1.1,0.9,1],
                         ['calm',0.9,1,1.1,1,1],
                         ['gentle',1,0.9,1,1.1,1],
                         ['sassy',1,1,1,1.1,0.9],
                         ['careful',1,1,0.9,1.1,1],
                         ['quirky',1,1,1,1,1]
                         ])

nature_chart = pd.DataFrame(data=nature_chart[1:,1:],
                            index=nature_chart[1:,0],
                            columns=nature_chart[0,1:])

# print(nature_chart)
# print(nature_chart.loc['jolly','speed'])