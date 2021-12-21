with open('input.txt') as f:
    i = f.readlines()

i = [int(i) for i in i]

answer = []

for j, k in enumerate(i):
    try:
        if i[j+1] > k:
            answer.append(i[j+1])
    except IndexError:
        pass

len(answer)
