# histogram.py
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d

print(histogram("sdfs"))
print(histogram(['aaa', 'bbb', 'aaa', 'bbb', 'c']))
