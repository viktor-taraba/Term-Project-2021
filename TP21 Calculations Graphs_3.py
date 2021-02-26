from TP21_Downloading_data import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
plt.rc('font',family='Times New Roman')

for i in range(len(index_list)):
	start = index_list[i]["Close"][0]
	end = index_list[i]["Close"][len(index_list[i]["Close"])-1]
	print(graph_names[i] + ". Початкове значення: " + str(start) + \
		". Кінцеве значення: " + str(end) + \
		". Зміна (у %): " + str(round((end/start-1)*100,2)) + ". \n")

df_0 = index_list[0]
df_0.drop(['Open', 'High', 'Low', 'Volume', 'Date', 'Percent change'], axis='columns', inplace=True)
df_graph = pd.DataFrame(data = df_0)

for i in range(1,len(names_list)):
	df_0 = index_list[i]
	df_0.drop(['Open', 'High', 'Low', 'Volume', 'Date', 'Percent change'], axis='columns', inplace=True)
	df_graph[graph_names[i]] = df_0

df_graph = df_graph.dropna()
df_graph = df_graph.rename(columns={'Close': 'SP500'})
df_graph = df_graph.apply(lambda x: x/x[0])

df_graph.plot(figsize=(11,6), linewidth=0.9).axhline(0.8, lw=0.8, color='black')
ax = plt.gca()
ax.set_ylabel('Зміна значення (відносно початкового значення)')
ax.set_xlabel('Дата')
ax.set_title('Зміна значення фондових індексів (2000-2021 рр.)\n')
ax.set_ylim([0,4])
plt.yticks(np.arange(0, 4, step=0.5))

plt.savefig("index_dyn.jpg")
plt.close()