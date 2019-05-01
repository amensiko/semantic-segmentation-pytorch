import os

str_dir = "/Users/anastasia/Desktop/GWU/research/human_trafficking/semantic-segmentation-pytorch/hotel_results/"
directory = os.fsencode(str_dir)

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".png"): 
		print("<div class=\"item\"> <img src=\"" + str_dir + filename + "\"> </div>")