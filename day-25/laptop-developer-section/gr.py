import matplotlib.pyplot as plt #pyplot-> helps as a toolbox to create grapgh

# ------------------ Data ------------------
x = [1, 2, 3, 4, 5]#x-> horizontal
y = [10, 20, 15, 25, 30]#y-> vertical

names = ['A', 'B', 'C', 'D']
values = [40, 25, 20, 15]

# ------------------ Create Subplots ------------------
plt.figure(figsize=(10, 8))

# -------- 1. Line Plot --------
plt.subplot(2, 2, 1)#subplot(rows , columns , postion)
plt.plot(x, y, marker='o', linestyle='--')
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()

# -------- 2. Bar Chart --------
plt.subplot(2, 2, 2)
plt.bar(names, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# -------- 3. Scatter Plot --------
plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# -------- 4. Pie Chart --------
plt.subplot(2, 2, 4)
plt.pie(values, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart")

# ------------------ Show All ------------------
plt.tight_layout()
plt.show()
