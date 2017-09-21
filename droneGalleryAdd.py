#Allow user to manually add a new drone image's information

import os, sys, json
from Tkinter import *



root = Tk()
addLabel = Label( root, text="ADD", font=(None, 25))
editLabel = Label( root, text="EDIT", font=(None, 25))
layerNameText = Label( root, text="Layer Name ")
layerNameEntry = Entry(root, bd =5)
descriptionText = Label( root, text="Description")
descriptionEntry = Text(root, bd = 15, height = 5) #Entry(root, bd =5, height = 20)
dateText = Label( root, text="Date")
dateEntry = Entry(root, bd =5)
xCoorText = Label( root, text="X-Coor")
xCoorEntry = Entry(root, bd =5)
yCoorText = Label( root, text="Y-Coor")
yCoorEntry = Entry(root, bd =5)

def clear_textbox(): #see if it can clear more than one entry...
	layerNameEntry.delete(0, END)
    # descriptionEntry.delete("1.0", END)
    # dateEntry.delete(0, END)
    # xCoorEntry.delete(0, END)
    # yCoorEntry.delete(0, END)

def deleteLastLine():
	readFile = open("droneGalleryJSON.json")
	lines = readFile.readlines()
	readFile.close()

	w = open("droneGalleryJSON.json",'w')

	w.writelines([item for item in lines[:-2]])
	w.writelines("]")
	w.close()

def displayLine(changeLayer): #edit line - when JSON dumps, it changes the order...
	data = []
	if os.path.exists('droneGalleryJSON.json'):
	    with open('droneGalleryJSON.json', 'r+') as f:
	    	playlist = json.load(f)
	    	for i in range(len(playlist)):
	        	if (playlist[i]["layer"] == changeLayer):
	        		layerNameEntry.insert(0, playlist[i]["layer"])
					# descriptionEntry.insert("1.0", playlist[i]["description"])
					# dateEntry.insert(0, playlist[i]["date"])
					# xCoorEntry.insert(0, playlist[i]["xcoor"])
					# yCoorEntry.insert(0, playlist[i]["ycoor"])

	        		playlist[i]["description"] = "PLEASE WORK"
	        	data.append(playlist[i])

		f.seek(0)
		f.writelines("[\n")
		f.writelines(["%s\n" % json.dumps(i) for i in data[0:1]])
		f.writelines([",%s\n" % json.dumps(i) for i in data[1:]])
		f.writelines(",\n]")
		f.truncate()

	# data = []
	# with open('droneGalleryJSON.json') as f:
	# 	for line in f:
	# 		print line
	# 		data.append(line)

	# data = []
	# with open('droneGalleryJSON.json', 'r+') as f:
	#     for line in f:
	#         data_line = json.loads(line)
	#         print line
	#         # if data_line[0] == 'test':
	#         #     data_line[1] = 'new value'
	#         # data.append(data_line)
	#     f.seek(0)
	#     f.writelines(["%s\n" % json.dumps(i) for i in data])
	    # f.truncate()





def addLine():
#layerNameEntry.get(), descriptionEntry.get(), dateEntry.get(), xCoorEntry.get(), yCoorEntry.get()
	# numAdds = int(raw_input("Number of entried to add? "))
	# for i in range(numAdds):
	layerName = layerNameEntry.get()
	description = descriptionEntry.get("1.0",'end-1c')
	date = dateEntry.get()
	xcoor = xCoorEntry.get()
	ycoor = yCoorEntry.get()

	readFile = open("droneGalleryJSON.json")
	lines = readFile.readlines()
	readFile.close()

	w = open("droneGalleryJSON.json",'w')

	w.writelines([item for item in lines[:-1]])
	w.writelines(',{"layer": "' + layerName +'", "description": "'+description+'", "date": "' +date+ '", "xcoor": "'+ xcoor+'", "ycoor": "' + ycoor + '"}')
	print ('ADDED: \nLayer Name:' + layerName +'\nDescription": '+description+'\nDate: ' +date+ '\nX-Coor: "'+ xcoor+'\nY-Coor: ' + ycoor +'\n')
	w.writelines("\n]")
	w.close()
	
submitAddButton = Button(root, text ="SUBMIT", command = addLine)
submitEdit = Button(root, text ="SUBMIT", command = displayLine)
closeButton = Button(root, text = "CLOSE", command=root.destroy)
clearButton = Button(root, text='CLEAR ALL', command=clear_textbox) #se if there can be mutliple commands?

def main():
	add = raw_input("Add Entry [y/n]? ")

	if (add == "Y" or add == "y"):

		addLabel.pack()
		layerNameText.pack()
		layerNameEntry.pack()
		descriptionText.pack()
		descriptionEntry.pack()
		dateText.pack()
		dateEntry.pack()
		xCoorText.pack()
		xCoorEntry.pack()
		yCoorText.pack()
		yCoorEntry.pack()
		submitAddButton.pack(side =BOTTOM)
		closeButton.pack(side =BOTTOM)
		clearButton.pack(side =BOTTOM)
		root.mainloop() 

	deleteLast  =raw_input("Delete last line [y/n]? ")
	if (deleteLast == "Y" or deleteLast == "y"):
		deleteLastLine()
	edit = raw_input("Edit line [y/n]? ")
	if (edit == "Y" or edit == "y"):
		changeLayer = raw_input("Layer name to change? ")
		displayLine(changeLayer)
		editLabel.pack()
		layerNameText.pack()
		layerNameEntry.pack()
		descriptionText.pack()
		descriptionEntry.pack()
		dateText.pack()
		dateEntry.pack()
		xCoorText.pack()
		xCoorEntry.pack()
		yCoorText.pack()
		yCoorEntry.pack()
		submitEdit.pack(side =BOTTOM)
		closeButton.pack(side =BOTTOM)
		clearButton.pack(side =BOTTOM)
		root.mainloop() 
		

main()

# {
# 	"layer": "northbeach",
# 	"description": "from our recent trip to Georgia.",
# 	"date": "3/12/17",
# 	"xcoor": "31.684522",
# 	"ycoor": "-81.132717"
# }