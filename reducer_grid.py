#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='|'):
    for line in file:
        yield line.rstrip().split(separator)

def main(separator='|'):
    buckets = {}
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    for line in data:
        bins = eval(line[1])[0]
        count = eval(line[1])[1]
        hr = int(line[0])

        if hr in buckets:
            if bins in buckets[hr]:
                buckets[hr][bins] += count
            else:
                buckets[hr][bins] = count
        else:
            buckets[hr] = {}
            buckets[hr][bins] = count

    for hr in sorted(buckets):
        for b in sorted(buckets[hr]):
            print str(hr) + '|' + str((b,buckets[hr][b]))


if __name__ == "__main__":
    main()