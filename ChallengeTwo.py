with open('input.txt') as f:
    i = f.readlines()

text = [int(i) for i in i]

windows = []
def Part2() -> int:
    ans = 0
    for i, j, k in zip(text, text[1:], text[2:]):
        windows.append(i + j + k)

    for i, j in zip(windows, windows[1:]):
        if j > i:
            ans += 1
    return ans

  Part2()
