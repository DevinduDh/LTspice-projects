import matplotlib.pyplot as plt

# Initialize lists to store data
slewc = []
trrise = []
trfall = []
rise_delay = []
fall_delay = []

# Read data from the text file
with open('output_values.txt', 'r') as file:
    current_list = None
    for line in file:
        line = line.strip()
        if line == 'slewc':
            current_list = slewc
        elif line == 'trrise':
            current_list = trrise
        elif line == 'trfall':
            current_list = trfall
        elif line == 'rise_delay':
            current_list = rise_delay
        elif line == 'fall_delay':
            current_list = fall_delay
        else:
            if current_list is slewc:  # Check if current list is slewc
                current_list.append(float(line) * 1e12)  # Convert seconds to picoseconds
            else:
                current_list.append(float(line))
# Plot the data
plt.plot(slewc, trrise, label='trrise')
plt.plot(slewc, trfall, label='trfall')
plt.plot(slewc, rise_delay, label='rise_delay')
plt.plot(slewc, fall_delay, label='fall_delay')
plt.xlabel('slewc (ps)')
plt.ylabel('Values')
plt.legend()
plt.show()
