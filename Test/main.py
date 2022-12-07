import os

cnt, start = [10000000] * 2
buckets = {}
while cnt:
    c = os.urandom(1)
    buckets.setdefault(c, 0)
    buckets[c] += 1
    cnt -= 1

ideal = 1 / 256.0
if len(buckets) != 256: print('{} missing keys'.format(256 - len(buckets)))
for k, v in sorted(buckets.items()):
    actual = float(buckets[k]) / start
    print('byte   acutal    diff')
    print('{:8} {:10.4%} {:10.4%}'.format(repr(k), actual, actual - ideal))
