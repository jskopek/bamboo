#!/usr/bin/python

import StringIO
import hotshot.stats
import sys
import re

new_stdout = StringIO.StringIO()
sys.stdout = new_stdout

stats = hotshot.stats.load(sys.argv[1])
stats.sort_stats("cumulative").print_stats(40)

sys.stdout = sys.__stdout__

print "OUTPUT:"
printed = new_stdout.getvalue()
print printed

for line in printed.split("\n"):
    m = re.match("\s+(\d+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([^:]+):(\d+)\(([^)]+)\)$", line)
    if m:
        print "LINE: %s"%line
        ncalls, tottime, percall_other, cumtime, percall, filename, linenum, method = m.groups(0)
        print ncalls
        print tottime
        print percall
        print cumtime
        print filename
        print linenum
        print method

#print "--- callers -----"
#stats.sort_stats("cumulative").print_callers(15)
#print "--- callees -----"
#stats.sort_stats("cumulative").print_callees(15)
