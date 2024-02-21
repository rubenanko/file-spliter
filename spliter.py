from os.path import isfile
from os import listdir,system
import tkinter as tk
from tkinter import ttk
import time


EXTENTION_LIST = ["mp4","mp3","png","jpg","gif","exe"]

def splitFile(filename : str,outputnames : str, chunk : int)->bool:
	system("mkdir " + outputnames.split("/")[0])
	chunk = chunk * 1000000
	if isfile(filename):
		with open(filename,"rb") as f:
			bytes_chunk = f.read(chunk)
			fid = 0
			while bytes_chunk != b"":
				with open(outputnames + str(fid),"wb+") as outputf:
					outputf.write(bytes_chunk)
				fid += 1
				bytes_chunk = f.read(chunk)
		return True
	else:	return False

def gatherFile(filenames : str, outputname : str)->None:
	fid = 0
	with open(outputname,"ab+") as output:
		while isfile(filenames + str(fid)):
			with open(filenames + str(fid),"rb") as f:
				output.write(f.read())
			fid += 1
			
def main():
	window = tk.Tk()
	window.title("file spliter")
	window.geometry("230x230")
	window.resizable(False, False)
	
	directory_list = listdir()
	file_list = []
	folder_list = []
	
	for element in directory_list:
		if isfile(element):	file_list.append(element)
		else:	folder_list.append(element)
		
	splitFileLabel = tk.Label(window,text="split file")
	splitFileLabel.pack()
	
	combofile = ttk.Combobox(window,state="readonly",values=file_list)
	combofile.pack()
	
	splitFileLabel2 = tk.Label(window,text="chunk size (Mo)")
	splitFileLabel2.pack()	

	chunkSizeEntry = tk.Entry(window)
	chunkSizeEntry.pack()
	
	split_button = tk.Button(window, text ="split", command=lambda: splitFile(combofile.get(),"output" + str(time.time()) + "/chunk",int(chunkSizeEntry.get())))
	split_button.pack()
		
	gatherFileLabel = tk.Label(window,text="gather files")
	gatherFileLabel.pack()
	
	combofolder = ttk.Combobox(window,state="readonly",values=folder_list)
	combofolder.pack()
	
	gatherFileLabel2 = tk.Label(window,text="file extention")
	gatherFileLabel2.pack()	
	
	comboextention = ttk.Combobox(window,values=EXTENTION_LIST)
	comboextention.pack()
	
	gather_button = tk.Button(window, text ="gather", command=lambda: gatherFile(combofolder.get() + "/chunk",combofolder.get() + "/output." + comboextention.get()))
	gather_button.pack()
	
	window.mainloop()

if __name__ == '__main__':
	main()
