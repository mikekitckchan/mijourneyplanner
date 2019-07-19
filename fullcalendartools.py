import json

def getevent(data):

	temp = data[0]['_calendar']['interactionsStore']['6'][0]['component']['context']['view']['timeGrid']['eventRenderer']['segs']
	#print (temp)

	output=[]
	
	
	for items in temp:
		eventdict ={}
		eventdict['title']=items['eventRange']['def']['title']
		eventdict['start']=items['start']
		eventdict['end']=items['end']
		output.append(eventdict)
		

	return output
			
def makeevent(date, time):
	pass

		
