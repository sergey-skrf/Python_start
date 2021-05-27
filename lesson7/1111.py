mc1 = [[31, 22], [37, 43], [51, 1]]
mc2 = [[69, 78], [63, 57], [49, 99]]

i = 0
while i < len(mc1):
    n = 0
    while n < len(mc1[i]):
        mc1[i][n] = mc1[i][n] + mc2[i][n]
        n += 1
    n = 0
    i += 1
print(mc1)
