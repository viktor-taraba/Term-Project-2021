import matplotlib.pyplot as plt
from TP21_Downloading_data import *

graph_names = ['^GSPC', '000001.SS', '^N100', '^HSI', '^KS11', '^N225']

def draw_graph(data, name):

	font = {'fontname' : 'Times New Roman', 
			'size' : 20}

	plt.figure(figsize=(20,10))
	plt.plot(data["Date"], data["Percent change"], color='orangered', linewidth=0.4)

	plt.tight_layout()
	plt.gcf().subplots_adjust(top=0.9, bottom=0.13, left=0.08)

	plt.ylabel('\nЗначення індексу', **font)
	plt.xlabel('Дата', **font)
	plt.title('Динаміка індексу '+ name, {'fontname' : 'Times New Roman', 'size' : 30})

	ax = plt.axes()
	ax.spines["right"].set_visible(False)
	ax.spines["top"].set_visible(False)

	for tick in ax.get_xticklabels():
		tick.set_fontname("Times New Roman")
	for tick in ax.get_yticklabels():
		tick.set_fontname("Times New Roman")
	ax.tick_params(axis='both', which='major', labelsize=20)

	plt.savefig(name + "_change" + ".jpg")
	plt.close()

for i in range(len(index_list)):
	draw_graph(index_list[i], graph_names[i])