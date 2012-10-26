#!/usr/bin/env python

import sys

F = 'https-ok.log'

if __name__ == '__main__':
    try:
        t = sys.argv[1]
        h = sys.argv[2]
    except:
        sys.exit(1)
    #
    line = '%s %s OK\n' %(t, h)
    open(F, 'a+').write(line)
