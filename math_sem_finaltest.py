#task 
#Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. 
#Даны значения роста в трех группах случайно выбранных спортсменов: 
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. 
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

#Нулевая гипотеза - средний рост взрослого спортсмена не зависит от вида спорта, которым он занимается
#Альтернативная гипотеза - средний рост взрослого спортсмена зависит от спорта, которым он занимается 

import numpy as np
import pandas as pd
from scipy import stats
footballers =np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockeyplayers =np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters =np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

#проверяем на нормальность через шапиро
print(stats.shapiro(footballers))
print(stats.shapiro(hockeyplayers))
print(stats.shapiro(weightlifters))
#Результаты 
# ShapiroResult(statistic=0.9775082468986511, pvalue=0.9495404362678528)
# ShapiroResult(statistic=0.9579196572303772, pvalue=0.7763139009475708)
# ShapiroResult(statistic=0.9386808276176453, pvalue=0.5051165223121643)

#проводим тест бартлетта 
print(stats.bartlett(footballers, hockeyplayers, weightlifters))
#Результаты 
# BartlettResult(statistic=0.4640521043406442, pvalue=0.7929254656083131)

#выполняем post hoc test
print(stats.tukey_hsd(footballers, hockeyplayers, weightlifters))
#Результаты 
# Tukey's HSD Pairwise Group Comparisons (95.0% Confidence Interval)
# Comparison  Statistic  p-value  Lower CI  Upper CI
# (0 - 1)      0.458     0.979    -5.357     6.273
# (0 - 2)      6.398     0.022     0.837    11.958
# (1 - 0)     -0.458     0.979    -6.273     5.357
# (1 - 2)      5.939     0.028     0.561    11.318
# (2 - 0)     -6.398     0.022   -11.958    -0.837
# (2 - 1)     -5.939     0.028   -11.318    -0.561

#используем метод однофакторного дисперсионного анализа 
print(stats.f_oneway(footballers, hockeyplayers, weightlifters))
#Результаты 
# F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698694)

# p-value = 0.01048 - на уровне альфа = 0.05 - отвергаем нулевую гипотезу, 
# а на уровне значимости альфа = 0.01 - нулевую гипотезу не отвергаем.
