import sys
import os

num_classes = len(sys.argv) - 1

if num_classes < 1:
    print("USAGE: class _CLASS1_ ...")
    quit()

def write_hpp_file(file, i):
    file_name = sys.argv[i]

    file.write("\n#ifndef " + file_name.upper() + "_HPP\n# define " + file_name.upper() + "_HPP\n")
    file.write("\nclass " + file_name + "\n{\n\tpublic:\n\t\t" + file_name + "();\n\t\t~" + file_name + "();\n\tprivate:\n\t\t\n};\n")
    file.write("\n#endif\n")
    file.close()

def hpp_files(i):
    file_name = sys.argv[i]

    # Check if the file already exists
    if os.path.exists("inc/" + file_name + ".hpp"):
        print(file_name + ".hpp already exists")
        return
    
	# Try to open thefile in append mode
    try:
        file = open("inc/" + file_name + ".hpp", "a")
    except:
        print("Error creating " + file_name + ".hpp file")
        quit()
    write_hpp_file(file, i)

def write_cpp_file(file, i):
    file_name = sys.argv[i]

    file.write("\n#include \"../inc/" + file_name + ".hpp\"\n")
    file.write("\n" + file_name + "::" + file_name + "() {\n\t\n}\n\n" + file_name + "::~" + file_name + "() {\n\t\n}\n")
    file.close()

def cpp_files(i):
    file_name = sys.argv[i]

    # Check if the file already exists
    if os.path.exists("src/" + file_name + ".cpp"):
        print(file_name + ".cpp already exists")
	return
    
	# Try to open thefile in append mode
    try:
        file = open("src/" + file_name + ".cpp", "a")
    except:
        print("Error creating " + file_name + ".cpp file")
        quit()
    write_cpp_file(file, i)

for i in range(num_classes):
    hpp_files(i + 1)
    cpp_files(i + 1)
