#!/usr/bin/python

import hotshot.stats
import sys

stats = hotshot.stats.load(sys.argv[1])
stats.sort_stats("cumulative").print_stats(40)
#print "--- callers -----"
#stats.sort_stats("cumulative").print_callers(15)
#print "--- callees -----"
#stats.sort_stats("cumulative").print_callees(15)
