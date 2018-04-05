



hoblo = [
	{
		'color': "red",
		'value': "#f00"
	},
	{
		'color': "red",
		'value': "#f0011"
	},
	{
		'color': "green",
		'value': "#0f0"
	},
	{
		'color': "blue",
		'value': "#00f"
	},
	{
		'color': "cyan",
		'value': "#0ff"
	},
	{
		'color': "magenta",
		'value': "#f0f"
	},
	{
		'color': "yellow",
		'value': "#ff0"
	},
	{
		'color': "black",
		'value': "#000"
	}
]
hoblo1 = [
	{
		'color': "red",
		'value': "#f00"
	},
	{
		'color': "grey",
		'value': "#fff"
	},
	{
		'color': "blue",
		'value': "#00f"
	},
	{
		'color': "cyan",
		'value': "#0ff"
	},
	{
		'color': "magenta",
		'value': "#f0f"
	},
	{
		'color': "yellow",
		'value': "#ff0"
	},
	{
		'color': "black",
		'value': "#000"
	}
]



import pandas as pd
#import as ps
import numpy as np


df = pd.DataFrame(hoblo)
df1 = pd.DataFrame(hoblo1)


#print ps.sqldf("select * from df minus select * from df1",locals())

dd = df.to_dict()
d1 = df1.to_dict()



print df
exit(1)

#print df['color']

dfDict = df1['color'].to_dict()

dfDict = [ x for x in dfDict.values()]
#print dfDict

def checkValue(dfDict,x,y,row):
	#dfDict = df1['color'].to_dict()
	if row['color'] in dfDict :
		return "True"
 	else:
		return "False"

df['color1'] = df.apply(lambda row : checkValue(dfDict,'true','false',row),axis=1)
print df


#for x in dfDict:
#	df['color1'] = np.where(df['color'] == x,"True",'False')
#print df
#query = "SELECT * FROM df WHERE (color = 'red' or value LIKE '%000%')"
#print(ps.sqldf(query, locals()))
#print df
#query = query.replace('WHERE','')

#print df.query(query, inplace=False)

#print df









