from collections import defaultdict
from goody import irange


def unique(iterator,times=1):
    track = defaultdict(int)
    for i in iterator:
        track[i] += 1
        if track[i] <= times:
            yield i


if __name__ == '__main__':
    iterable = 'abbcccddddeeeeefffff'
    for t in irange(1,6):
        print('unique with times =',t,end=': ')
        for i in unique(iterable,times=t):
            print(i,end='')
        print()    
