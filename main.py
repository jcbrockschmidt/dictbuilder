#!/usr/bin/env python3

"""TODO:
 * more flexible sorting options
 * use -o to specify output file
"""

import json, sys

if len(sys.argv) > 1:
    inFn = sys.argv[1]

with open(inFn, 'r') as f:
    try:
        defs = json.load(f)
    except ValueError as e:
        sys.exit('ValueError in {}: {}'.format(inFn, e))

sort = sorted(defs, key=str.lower)

print('# My Dictionary')
print('\n## Definitions')
curLetter = None
for k in sort:
    l = k[0].upper()
    if curLetter != l:
        curLetter = l
        print('\n### {}'.format(curLetter))
    word = k[0].upper() + k[1:]
    print('* *{}* - {}'.format(word, defs[k]))
