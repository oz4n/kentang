#!/usr/bin/env python

import sys

F = 'smtp-fail.log'

if __name__ == '__main__':
    try:
        t = sys.argv[1]
        h = sys.argv[2]
        p = sys.argv[3]
    except:
        sys.exit(1)
    #
    line = '%s %s %s FAILED\n' %(t, h, p)
    open(F, 'a+').write(line)
