
import time

start_time = time.time()
for a in range(0, 2001):
    for b in range(0, 2001):
        for c in range(0, 2001):
            if a+b+c==1000 and a**2 + b**2 == c**2:
                print("a, b, c:%d, %d, %d" % (a, b, c))
                print("a, b, c:%d, %d, %d" % (a, b, c))

# for a in range(0, n):
#     for b in range(0, n):
#         c = 1000 - a -b
#         if a**2 + b**2 == c**2:
#             print("a, b, c:%d, %d, %d" % (a, b, c))


