from statistics import mean
pisemky = [
    [1, 3, 2, 1],
    [3, 1, 1, 2],
    [4, 2, 2, 2],
    [1, 1, 1, 1],
    [1, 2, 2, 1],
    [1, 4, 1, 3]
]

pisemka = [znamka[0] for znamka in pisemky]
print(round(mean(pisemka), 2))