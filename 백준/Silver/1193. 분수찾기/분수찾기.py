x = int(input())

line = 1

while( x > line):
    x -= line
    line += 1
if line % 2 ==0:
    up = x
    down = line- x + 1
if line % 2 !=0:
    down = x
    up = line- x + 1
print(f"{up}/{down}")