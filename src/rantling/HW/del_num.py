import sys

while True:
    try:
        for line in sys.stdin:
            N = int(line.split()[0])
            N = N if N < 1000 else 999
        
            ls = []
            index = 0
            pos = 0
        
            for i in range(0, N):
                ls.append(i)
            
            while len(ls) > 1:
                pos += 2
                if pos > len(ls)-1:
                    pos = pos % len(ls)
                index = ls[pos]
                del ls[pos]
            print(ls[0])
    except:
        break
            