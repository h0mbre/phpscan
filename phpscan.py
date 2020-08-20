import glob
import argparse
import os

### arg parsing ###
parser = argparse.ArgumentParser()

parser.add_argument("-d", "--directory", default=os.getcwd(),
	type=str,
	help="directory to search for php files from, default=cwd")

parser.add_argument("-r", "--recursive",
	help="recurisvely search from the searchdir",
	action="store_true")

parser.add_argument("-v", "--verbose",
	help="display actual function call syntax",
	action="store_true")

args = parser.parse_args()
search_dir = args.directory
###################

### scary php functions ###
bad_func = ["system(", "shell_exec(", "exec(", "passthru(", "popen(",
	"proc_open(", "pcntl_exec(", "eval(", "assert("]
###########################


def search_files(search_dir):
	# search through our current directory for php files and return list
	if args.recursive:
		files = glob.glob(search_dir + '/**/*.php', recursive=True)
	# search through our current dir recusrively for php files
	else:
		files = glob.glob(search_dir + '/*.php', recursive=False)

	print("> found {} php files".format(str(len(files))))
	return files

def parse_files(files):
	findings = {}
	final_findings = {}
	for x in files:
		file = open(x, 'r')
		lst = []
		findings["{}".format(file.name)] = lst
		lines = file.readlines()
		for y in lines:
			for z in bad_func:
				if z in y:
					lst.append(
						"\033[36;1m{}\033[0m -- line {}: {}".format(z.replace("(", ""),
						"\033[33;1m{}\033[0m".format(lines.index(y) + 1),
						z + y.split(z)[1]).rstrip())
	
	for key, value in findings.items():
		key = os.path.relpath(key, os.getcwd())
		if value != []:
			new_value = []
			for x in value:
				if x not in new_value:
					new_value.append(x)
			final_findings[key] = new_value
			

	return final_findings

def present_findings(final_findings):
	for key, value in final_findings.items():
		print("> \033[35;1m{}\033[0m".format(key))
		for x in value:
			if args.verbose:
				print("   {}".format(x))
			else:
				print("   {}".format(x.split(":")[0]))

php_files = search_files(search_dir)
final_findings = parse_files(php_files)
present_findings(final_findings)
