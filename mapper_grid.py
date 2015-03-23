#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import math
from datetime import datetime

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split('\t')

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    #nxn grid
    n = 1000
    #buckets is a dictionary where each entry is a bucket determined by y*n+x
    buckets = {}
    #max/min lat/longs
    latm = 40.477399
    latmm = 40.917577
    lngm = -74.25909
    lngmm = -73.700272

    for words in data:
        try:
            
            lat = float(words[0])
            lng = float(words[1])
            
            #to go by hour or n by weekday just change the formula for hr, no need to change anything else
            try:
                hr = datetime.strptime(words[2].split(' ')[1], '%H:%M:%S').time().hour
                # hr = datetime.strptime(words[2].split(' ')[0], '%Y-%m-%d').date().weekday() #this is by day of the week
            except IndexError:
                continue
            
            # increase the count for the appropriate bin
            if lng == lngmm:
                xidx = n-1
            else:
                xidx = int(math.floor(((lng-lngm)/(lngmm-lngm))*n))
            if lat == latmm:
                yidx = n-1
            else:
                yidx = int(math.floor(((lat-latm)/(latmm-latm))*n))

            #don't record any observations that fall outside the bounds
            if (0 <= xidx <= n-1) and (0 <= yidx <= n-1):
                b = (yidx*n)+xidx
                if hr in buckets:
                    if b in buckets[hr]:
                        buckets[hr][b] += 1
                    else:
                        buckets[hr][b] = 1
                else:
                    buckets[hr] = {}
                    buckets[hr][b] = 1

        except ValueError:
            continue

    #output each bin and its count
    for hr in sorted(buckets):
        for b in sorted(buckets[hr]):
            print str(hr) + '|' + str((b,buckets[hr][b]))


if __name__ == "__main__":
    main()