# coding:utf-8
import sys
import time

jtamie = ["1101011", "1011101", "1110111"]
count = 1
for num in jtamie:
    for x in range(6, -1, -1):
        if x % 3 == 0 and count < 2:
            if num[x] == "1":
                sys.stdout.write(" ——")
            else:
                sys.stdout.write("  ")
            sys.stdout.write("\n")
            time.sleep(0.3)
            sys.stdout.flush()
        else:
            if num[x] == "1":
                if count < 2:
                    sys.stdout.write("|  ")
                else:
                    if num[x+1] == "1":
                        sys.stdout.write("|  ")
                    else:
                        sys.stdout.write(" |  ")
            else:
                sys.stdout.write("  ")

            if count < 2:
                count += 1
            else:
                sys.stdout.write("\n")
                time.sleep(0.3)
                sys.stdout.flush()
                count -= 1
