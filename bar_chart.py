import matplotlib.pyplot as plt

##########################################################
# Create only ona chart

def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i]+0.005, y[i], ha='center')  # Aligning text at center

### lists must be the same size
categories = ['test', 'control'] 
values = [1, 2]
colors = ['red', 'blue']

plt.bar(categories, values, color=colors)

add_labels(categories, values)

plt.show()

##########################################################
# Create many charts

fig, axes = plt.subplots(2, 2, figsize=(10, 5))

# First dataset with labels
bar1 = axes[0, 0].bar(categories, values, color=colors)
axes[0, 0].set_title("Set 1")
axes[0, 0].set_ylabel("Values")
axes[0, 0].bar_label(bar1)


# Second dataset
axes[0, 1].bar(categories, values, color=colors)
axes[0, 1].set_title("Set 2")
axes[0, 1].set_ylabel("Values")


# Third dataset
axes[1, 0].bar(categories, values, color=colors)
axes[1, 0].set_title("Set 3")
axes[1, 0].set_ylabel("Values")


# Forth dataset
axes[1, 1].bar(categories, values, color=colors)
axes[1, 1].set_title("Set 4")
axes[1, 1].set_ylabel("Values")

plt.tight_layout()
plt.show()
