from TP21_Downloading_data import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
plt.rc('font',family='Times New Roman')

for i in range(len(graph_names)):

		df = index_list[i]
		df.drop(['Open', 'High', 'Low', 'Volume', 'Date', 'Percent change'], axis='columns', inplace=True)
		df.rename(columns={'Close': 'Волатильність (стандартне відхилення)'}, inplace=True)

		df = df.pct_change(1)
		std = df.rolling(30).std(ddof=0)

		state = pd.cut(std['Волатильність (стандартне відхилення)'], bins=[-np.inf, std['Волатильність (стандартне відхилення)'].mean(), 1.25*std['Волатильність (стандартне відхилення)'].mean(), \
			1.5*std['Волатильність (стандартне відхилення)'].mean(), np.inf], labels=range(4))
		cmap = plt.get_cmap('RdYlGn_r')

		std.plot(color='black', figsize = (18,4), linewidth=1.5, marker='', legend=False)
		ax = plt.gca()  
		axes = plt.gca()

		if graph_names[i] == "SP500" or graph_names[i] == 'KOSPI':
			axes.set_ylim([0, 0.055])
		elif graph_names[i] == 'SSE Composite Index':
			axes.set_ylim([0, 0.04])
		else:		
			axes.set_ylim([0,0.07])
		
		ax.set_xlim(left=std.index[0], right=std.index[-1])
		ax.set_ylabel('Волатильність (ст. відхилення)', {'fontname':'Times New Roman'})
		ax.set_xlabel('Дата', {'fontname':'Times New Roman'})
		ax.set_title('Динаміка волатильності (30d) ' + graph_names[i], {'fontname' : 'Times New Roman', 'size' : 17})

		for tick in ax.get_xticklabels():
			tick.set_fontname("Times New Roman")
		for tick in ax.get_yticklabels():
			tick.set_fontname("Times New Roman")
		ax.grid(False)
		trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)

		for i, color in enumerate(cmap([0.2, 0.4, 0.6, 0.8])):
		    ax.fill_between(std.index, 0, 1, where=state == i,facecolor=color, transform=trans)

		graph_name = 'vol'+ graph_names[i]
		# plt.savefig(graph_name + '.jpg')
		plt.show()
		plt.close()