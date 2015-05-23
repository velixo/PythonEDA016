import sys
topdir = 'PythonEDA016'
s = sys.path[0]
sys.path.insert(0, s[:s.index(topdir) + len(topdir)])


def print_path():
	path = sys.path
	print("")
	for line in path:
		print(line)