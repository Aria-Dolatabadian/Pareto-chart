import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
#create DataFrame
df = pd.DataFrame({'count': [97, 140, 58, 6, 17, 32]})
df.index = ['B', 'A', 'C', 'F', 'E', 'D']
#sort DataFrame by count descending
df = df.sort_values(by='count', ascending=False)
#add column to display cumulative percentage
df['cumperc'] = df['count'].cumsum()/df['count'].sum()*100
#define aesthetics for plot
color1 = 'steelblue'
color2 = 'red'
line_size = 4
#create basic bar plot
fig, ax = plt.subplots()
ax.bar(df.index, df['count'], color=color1)
#add cumulative percentage line to plot
ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())
#specify axis colors
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)
#display Pareto chart
plt.show()
