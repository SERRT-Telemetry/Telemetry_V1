from pathlib import Path

path = Path(__file__).with_name('ExampleData.txt')

file = path.open('r')

lines = file.readlines()

data=[]

for e in lines:
    print(e)
    for i in range(0, len(e)-1):
        if(i < 4):
            i = 3
            continue
        if(i == len(e)-2):
            break
        data.append(e[i])


result = []
i = 0

while i in range(0, len(data)-1):
    result.append(data[i]+data[i+1])
    i += 2

print(result)

file.close()