#Functions - Help us model a linear relationship between variables. (y = 2x + 1 OR f(x) = 2x + 1)
import matplotlib.pyplot as plt

def f(x):
    return 5*x + 1

values_of_x = [0,1,2,3,4,5]
values_of_y = []

for x in values_of_x:
    y = f(x)
    values_of_y.append(y)

print(values_of_y)
# fig, ax = plt.subplots()
# plt.plot(values_of_x, y)
# plt.show()