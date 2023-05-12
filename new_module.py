import sys
import shutil
import os

if len(sys.argv) < 3:
	print("USAGE: new _MODULE_NAME_ _NUMBER_EXERECISES_")
	quit()


module_folder = sys.argv[1]
list = [ module_folder ]

if (sys.argv[2]).isdigit():
	r = int(sys.argv[2])
else:
	print("__NUMBER_EXERCISES__ must be a number")
	quit()

for i in range(r):
		ex_dir = module_folder + "/ex0" + str(i)
		list.append(ex_dir)

for item in list:
	try:
		os.mkdir(item)
	except OSError:
		print("File already exists")
		quit()
	if list.index(item) == 0:
		continue
	try:
		shutil.copy("Makefile", item)
	except:
		print("Makefile does not exist")
		quit()
	sub_list = [ item + "/src", item + "/inc" ]
	for subitem in sub_list:
		try:
			os.mkdir(subitem)
		except OSError:
			print("File already exists")
			quit()
