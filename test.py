
from collectionpy.math.statistic import SimpleLinearRegression

slr = SimpleLinearRegression(
    x = [1, 2, 3, 4, 5],
    y = [3, 6, 10, 15, 20]
)

print(slr.expression())

x = 6
y = slr.calcular(x)

print('x=', x, '=', y)

