import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane = pd.read_excel('D:\\Users\piokoz\projekty\python\Zestaw14_WD_EGZ1_2022\kina14.xlsx')
#wartosc = dane['Wartosc']
#woj = dane['Nazwa']
#plt.pie(wartosc, labels=woj, autopct='%.2f')
#plt.show()

df = pd.DataFrame([['A', 10, 20, 10, 30], ['B', 20, 25, 15, 25], ['C', 12, 15, 19, 6],
                   ['D', 10, 29, 13, 19]],
                  columns=['Team', 'Round 1', 'Round 2', 'Round 3', 'Round 4'])
# view data
print(df)
labels = ['St M', 'St K', 'Nst M', 'Nst K']
# plot grouped bar chart
df.plot(x='Team',
        kind='bar',
        stacked=False,
        title='Grouped Bar Graph with dataframe')
plt.show()