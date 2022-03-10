import sys

my_file = open(sys.argv[1]+"/index.h", "w")
my_file.write("bool bollian = false;")
my_file.close()
