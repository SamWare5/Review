import matplotlib.pyplot as plt
squares = [10, 40, 90, 160, 250]
input_values = [10, 20, 30, 40, 40]

plt.plot(squares)
plt.show()


plt.axis([0, 100, 0, 100])
plt.scatter(input_values, squares, linewidth=5, c='red')
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()


