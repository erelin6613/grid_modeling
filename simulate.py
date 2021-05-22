import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from models import Grid


def mean_daily_consumption(df, 
	cons_col='load_per_consumer'):

	df.time = df.time.apply(lambda x: str(x).split(' ')[0])
	grouped = df.groupby('time')
	recs = []
	for g in grouped:
		if len(g[1])<24:
			continue
		recs.append(g[1][cons_col].sum())

	return np.array(recs), np.mean(recs)

def run_simulation():
	g = Grid(1e3, 100)
	loads = g.simulate(num_hours=24*7)
	loads['diff'] = loads.apply(
		lambda x: x['gen']-x['load'], axis=1)
	loads['en_suplus'] = loads.loc[loads['diff']>0, 'diff']
	loads['en_outage'] = loads.loc[loads['diff']<=0, 'diff']
	plt.setp(plt.gca().get_xticklabels(),
		rotation=75, ha='right')
	plt.plot(loads['load'], label='{} households load'.format(
		g.num_consumers), color='green')
	plt.plot(loads['gen'],
		label='{} solar arrays power generation'.format(
		len(g.generators)), color='orange')
	plt.stem(loads['en_suplus'].index,
		loads['en_suplus'].values, basefmt=' ', markerfmt='b')
	plt.stem(loads['en_outage'].index,
		loads['en_outage'].values, basefmt=' ', markerfmt='b')
	plt.xticks(
		[x for x in loads.index if int(x.split(' ')[-1])%12==0])
	plt.legend()
	plt.tight_layout()

	print(loads['load'].mean()/100)
	for col in loads.columns:
		loads[f'{col}_per_consumer'] = loads[col]/100
	loads.to_csv('loads.csv')
	plt.show()

if __name__ == '__main__':
	run_simulation()
	#df = pd.read_csv('loads.csv')
	#cons_history, mean_cons = mean_daily_consumption(df)

	#print(mean_cons)
