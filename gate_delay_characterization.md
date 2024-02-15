# LTspice-projects
![Screenshot 2024-02-03 233827](https://github.com/DevinduDh/LTspice-projects/assets/76746921/6350ba8d-d0ab-436c-855f-a9477e3a8c2b)

## Schematic
![schematic](https://github.com/DevinduDh/LTspice-projects/assets/76746921/4ac23f47-d9b2-4f43-bcad-cda26d2e31f0)

## Sizing of Inverter
![image](https://github.com/DevinduDh/LTspice-projects/assets/76746921/cf4ec450-a655-4346-8fab-f02c9c45011d)

For the inverter both NMOS and PMOS length was kept at 45nm, NMOS width kept at 0.2µm and PMOS width was varied. Then transition rise and transition fall at DUT output was taken. From the graph where transition rise and transition fall equals corresponds to 0.296µm.
Length = 45nm
PMOS width = 0.296 µm
NMOS width = 0.2 µm
Multiplier = 4

## Calculating rising, falling propagation delay, output rise and fall time of the device under test (DUT)
![Screenshot 2024-01-30 104825](https://github.com/DevinduDh/LTspice-projects/assets/76746921/63505c33-52ad-417a-ada8-0beb59eed409)
![Screenshot 2024-01-30 105741](https://github.com/DevinduDh/LTspice-projects/assets/76746921/a0be0661-877e-4bf6-9804-8215652daefa)
## Sweeping the input slew at node “a” and measure input slew at node “c”.
Input slew at A is varied by varying the rise time and fall time of the pulse signal
Slew A vaues          |  Slew C vaues          
:-------------------------:|:-------------------------:
![](https://github.com/DevinduDh/LTspice-projects/assets/76746921/99c5f794-d6f4-4411-9aa0-1ddfe0c0a583)  |  ![Screenshot 2024-01-30 180040](https://github.com/DevinduDh/LTspice-projects/assets/76746921/8cf7f54a-d1d7-4a50-9bf1-41e6d6316748)


![Screenshot 2024-01-30 110120](https://github.com/DevinduDh/LTspice-projects/assets/76746921/0ee3b557-18d2-4162-8c9b-4ae81886a424)

## The input slew at node “c” are {20, 30, 40, 50, 100, 200, 250}ps. Plot the input slew at node “c” versus rising, falling propagation delay, output rise and fall time of DUT. 
Input slew at node C was varied by a capacitor at node C.
![Screenshot 2024-01-30 180336](https://github.com/DevinduDh/LTspice-projects/assets/76746921/a44e153a-78fb-4267-aa53-87903f7c7cae)
![Screenshot 2024-01-30 180840](https://github.com/DevinduDh/LTspice-projects/assets/76746921/1f730c0a-a65c-409a-bc46-b1aba3c08d84)
![Screenshot 2024-01-30 180717](https://github.com/DevinduDh/LTspice-projects/assets/76746921/19e5a566-ae5e-4d2d-8a16-c98093157110)

## Sweep the output load of DUT. The out load can be of 1 to 6 inverter loads in the step of 1 inverter. Plot the output load versus rising, falling propagation delay, output rise and fall time of DUT.
The output load of DUT is varied by changing size of inverter.
Varying PMOS size            |  Varying NMOS size      
:-------------------------:|:-------------------------:
![](https://github.com/DevinduDh/LTspice-projects/assets/76746921/530bbcd6-3aa0-4b47-9876-837cf63ef8ce)  |  ![](https://github.com/DevinduDh/LTspice-projects/assets/76746921/0fdbfab2-80e8-4daa-9336-04ee14957281)

![Screenshot 2024-01-30 181636](https://github.com/DevinduDh/LTspice-projects/assets/76746921/8ecc8473-b903-43bb-9730-1ae9237e142a)
![Screenshot 2024-01-30 181932](https://github.com/DevinduDh/LTspice-projects/assets/76746921/c8dbe49b-74aa-4732-beaf-09f49256e79a)

Python Script to plot graphs for propagation delays fall and rise, transition rise, transition fall directly from the netlist file.
```
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
```









