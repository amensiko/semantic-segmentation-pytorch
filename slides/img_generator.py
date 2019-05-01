import os

def write_local_img(str_dir):
	directory = os.fsencode(str_dir)

	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".png"): 
			print("<div class=\"item\"> <img src=\"" + str_dir + filename + "\"> </div>")


def write_link_img(link_strings_file):
	with open(link_strings_file) as f:
		for s in f:
			link = s[s.find("(")+1:s.find(")")]  #just read the link inside the parentheses
			print("<div class=\"item\"> <img src=\"" + link + "\"> </div>")



str_dir = "/Users/anastasia/Desktop/GWU/research/human_trafficking/semantic-segmentation-pytorch/hotel_results/"
link_strings_file = "links"

write_link_img(link_strings_file)