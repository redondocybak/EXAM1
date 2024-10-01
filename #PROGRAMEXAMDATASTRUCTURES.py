#PROGRAMEXAMDATASTRUCTURES

for i in range(1, 51):
        if i % 5 == 0:
            print(f"{i}: HiFive")
        elif i % 2 == 0:
            print(f"{i}: HiTwo")
        elif i % 3 == 0 or i % 7 == 0:
            print(f"{i}: HiThreeOrSeven")
        else:
            print(i)

