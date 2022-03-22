arr="""215
193 124
117 237 442
218 935 347 235
320 804 522 417 345
229 601 723 835 133 124
248 202 277 433 207 263 257
359 464 504 528 516 716 871 182
461 441 426 656 863 560 380 171 923
381 348 573 533 447 632 387 176 975 449
223 711 445 645 245 543 931 532 937 541 444
330 131 333 928 377 733 017 778 839 168 197 197
131 171 522 137 217 224 291 413 528 520 227 229 928
223 626 034 683 839 053 627 310 713 999 629 817 410 121
924 622 911 233 325 139 721 218 253 223 107 233 230 124 233"""

arr1="""1
8 4
2 6 9
8 5 9 3"""
tri = [ [*map(int,line.split())] for line in arr1.split("\n") ]
maxValue = max(map(max,tri))
isPrime = [0,0]+[1]*(maxValue-1) # Sieve of Eratosthenes
p,inc = 2,1
while p*p<=maxValue:
    if isPrime[p]:
        isPrime[p*p::p] = [0]*len(range(p*p,len(isPrime),p))
    p,inc = p+inc,2
tri = [ [None if isPrime[n] else n for n in row] for row in tri ]
path = tri[-1]
for row in tri[-2::-1]:
    path = [None if n is None or (a, b) == (None, None) else n + max(a or 0, b or 0)
            for n, a, b in zip(row, path, path[1:])]
print(path[0])