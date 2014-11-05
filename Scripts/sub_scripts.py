import sys

def dedupe_file(input_file,out_file):
    print 'deduping...'
    data = [row for row in input_file]
    header = data.pop(0)
    out_file.write(header)
    deduped = list(set(data))
    for e in sorted(deduped):
    	if e != '\n':
    		out_file.write(e)


#def strip_suffix(name):  #strip suffix to create output file name w/'.csv'
#    return name[:-4]
#
#file_ext = '.ff'
#
#fname = 'test.txt'
#with open(fname, 'r') as input_file, open(strip_suffix(fname) + file_ext, 'w') as out_file:
#                dedupe_file(input_file, out_file)