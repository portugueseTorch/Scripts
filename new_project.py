import sys
import os
from colorama import Fore

if len(sys.argv) < 3:
	print("USAGE: proj _PROJECT_NAME_ _LANG_")
	quit(1)

proj_name = sys.argv[1]
lang = sys.argv[2]

if proj_name[0] >= '0' and proj_name[0] <='9':
	print(Fore.RED + "ERROR: Project name cannot start with a number" + Fore.RESET)
	quit(1)

if lang != "c" and lang != "cpp":
	print(Fore.RED + "ERROR: Only c and cpp projects supported" + Fore.RESET)
	quit(1)

if os.path.exists(proj_name):
	print(proj_name + "directory already exits on your local machine\nPlease select a different name for the project")
	quit(1)

def create_main():
	term = ".h" if lang == "c" else ".hpp"
	main = open("src/main." + lang, "a")
	main.write("\n#include \"../inc/" + proj_name.lower() + term + "\"\n")
	main.write("\nint main() {\n\t\n\treturn 0;\n}\n\n")
	main.close()

def create_header():
    term = "h" if lang == "c" else "hpp"
    header = open("inc/" + proj_name.lower() + "." + term, "a")
    header.write("\n#ifndef " + proj_name.upper() + "_" + term.upper() + "\n")
    header.write("# define " + proj_name.upper() + "_" + term.upper() + "\n\n")
    header.write("\n#endif\n")
    header.close()

try:
	# Create project directory
	os.mkdir(proj_name)
	os.chdir(proj_name)

	# Initializing github repo
	print(Fore.BLUE + "[Initializing git repo...]" + Fore.RESET)
	os.system('git init')

	# Creating src, inc, lib, and .gitignore files
	dirs = [ "src", "inc", "lib" ]
	for item in dirs:
		os.mkdir(item)
	gitignore = open(".gitignore", "a")
	gitignore.write("subject.pdf\n")
	gitignore.close()
	print(Fore.BLUE + "[Creating folder structure...]" + Fore.RESET)

	# Creating a header file and a main
	create_main()
	create_header()

	# Adding files and pushing
	os.system('git add .')
	os.system('git commit -m \"Initial Commit\"')
	os.system('gh repo create ' + proj_name + ' --public --source=. --remote=upstream --push')
	print(Fore.GREEN + "\n" + proj_name + " repository created.\nGo get some, tiger.\n" + Fore.RESET)
except:
	print(Fore.RED + "ERROR: unable to create repo" + Fore.RESET)
	quit(1)
