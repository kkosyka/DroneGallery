#Allow user to manually add a new drone image's information

import os, sys, json
from Tkinter import *

file = "droneGalleryJSON1.json"

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

def clear(): #see if it can clear more than one entry...
	layerNameEntry.delete(0, END)
	clear1()
	clear2()
	clear3()
	clear4()
def clear1():
    descriptionEntry.delete("1.0", END)
def clear2():
	dateEntry.delete(0, END)
def clear3():
    xCoorEntry.delete(0, END)
def clear4():
    yCoorEntry.delete(0, END)

def deleteLastLine():
	readFile = open(file)
	lines = readFile.readlines()
	readFile.close()
	w = open(file,'w')
	w.writelines([item for item in lines[:-2]])
	w.writelines("]")
	w.close()

def display(description, date, xcoor,ycoor):
	descriptionEntry.insert("1.0", description)
	dateEntry.insert(0, date)
	xCoorEntry.insert(0, xcoor)
	yCoorEntry.insert(0, ycoor)


def displayLine(changeLayer): #edit line - when JSON dumps, it changes the order...
	data = []
	if os.path.exists(file):
	    with open(file, 'r+') as f:
	    	playlist = json.load(f)
	    	for i in range(len(playlist)):
	        	if (playlist[i]["layer"] == changeLayer):
	        		layerNameEntry.insert(1, playlist[i]["layer"])
	        		display(playlist[i]["description"], playlist[i]["date"], playlist[i]["xcoor"], playlist[i]["ycoor"])
		# 			# descriptionEntry.insert("1.0", playlist[i]["description"])
		# 			# dateEntry.insert(0, playlist[i]["date"])
		# 			# xCoorEntry.insert(0, playlist[i]["xcoor"])
		# 			# yCoorEntry.insert(0, playlist[i]["ycoor"])
		# 			# playlist[i]["layer"] = "PLEASE WORK"
	 #        		playlist[i]["description"] = "PLEASE WORK"
	 #        		playlist[i]["date"] = "PLEASE WORK"
	 #        		playlist[i]["xcoor"] = "PLEASE WORK"
	 #        		playlist[i]["ycoor"] = "PLEASE WORK"
	 #        	data.append(playlist[i])

		# f.seek(0)
		# f.writelines("[\n")
		# f.writelines(["%s\n" % json.dumps(i) for i in data[0:1]])
		# f.writelines([",%s\n" % json.dumps(i) for i in data[1:]])
		# f.writelines(",\n]")
		# f.truncate()

def modifyLine():
	data = []
	newLayerName = layerNameEntry.get()
	newDesc = descriptionEntry.get("1.0",'end-1c')
	newDate = dateEntry.get()
	newXCoor = xCoorEntry.get()
	newYCoor = yCoorEntry.get()
	print ("Modified to: \n" +  newLayerName + " \n" + newDesc + " \n" + newDate + " \n" + newXCoor + "\n" + newYCoor)
	if os.path.exists(file):
	    with open(file, 'r+') as f:
	    	playlist = json.load(f)
	    	for i in range(len(playlist)):
	    		layerName = layerNameEntry.get()
	        	if (playlist[i]["layer"] == layerName):
					playlist[i]["description"] = newDesc
					playlist[i]["date"] = newDate
					playlist[i]["xcoor"] = newXCoor
					playlist[i]["ycoor"] = newYCoor
					data.append(playlist)

			f.seek(0)
			out = [json.dumps(i, indent=0, sort_keys = True, separators=(',', ':')) for i in data]
			f.writelines(out)
			f.truncate()

def addLine():
	layerName = layerNameEntry.get()
	description = descriptionEntry.get("1.0",'end-1c')
	date = dateEntry.get()
	xcoor = xCoorEntry.get()
	ycoor = yCoorEntry.get()

	readFile = open(file)
	lines = readFile.readlines()
	readFile.close()
	w = open(file,'w')
	# lastLine = (item for item in lines[-8:-1])
	#w.writelines([item for item in lines[:-8]])
	w.writelines([item for item in lines[:-1]])
	# w.writelines([item for item in lastLine] + ",")
	# w.writelines(',{"layer": "' + layerName +'", "description": "'+ description +'", "date": "' + date + '", "xcoor": "'+ xcoor +'", "ycoor": "' + ycoor + '"}')
	w.writelines('{\n"date": "' + date + '", \n"description": "' +description + '", \n"layer": "' + layerName+ '", \n"xcoor": "' + xcoor + '", \n"ycoor": "' + ycoor + '"\n}')
	print ('ADDED: \nLayer Name:' + layerName +'\nDescription : '+ description +'\nDate: ' + date + '\nX-Coor: '+ xcoor +'\nY-Coor: ' + ycoor +'\n')
	w.writelines("\n]")
	w.close()
	clear()
	
submitAddButton = Button(root, text = "SUBMIT", command = addLine)
submitEdit = Button(root, text = "SUBMIT", command = modifyLine)
closeButton = Button(root, text = "CLOSE", command = root.destroy)

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
		submitAddButton.pack(side = BOTTOM)
		closeButton.pack(side = BOTTOM)
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
		submitEdit.pack(side = BOTTOM)
		closeButton.pack(side = BOTTOM)
		root.mainloop() 
		
main()

# {
# 	"layer": "northbeach",
# 	"description": "from our recent trip to Georgia.",
# 	"date": "3/12/17",
# 	"xcoor": "31.684522",
# 	"ycoor": "-81.132717"
# }