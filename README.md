# Antenna Placement Problem using Genetic Algorithm
This repository contains a Python implementation of a genetic algorithm to solve the antenna placement problem for Moroccan cities. The goal of the algorithm is to find a suboptimal locations to place antennas in order to cover all cities and minimize the number of antennas used, using a fixed coverage range of 270 km.
The problem is modeled as a set covering problem with Moroccan cities as the target coverage area. The genetic algorithm is implemented with three main scripts:

genetic.py: Implements the genetic algorithm


data.py: Transforms Moroccan city coordinates for use in the algorithm.


plot.py: Visualizes the results and input data on a Moroccan map

# Getting Started
To run the algorithm, you will need to have Python 3 installed on your computer. The following steps will guide you through the process:

Clone the repository to your local machine.


Install the required dependencies by running :``` pip install -r requirements.txt ``` in your terminal.


Run python  ```genetic.py ``` to execute the genetic algorithm, generate and  store the results in an Excel table called solution.


Run ```python plot.py``` to visualize the results on a map of Morocco.
# Algorithm
The antenna placement problem was modeled as a set covering problem and solved using a genetic algorithm implemented in Python. To handle the problem's constraints, a repairing strategy was used. The repairing strategy consists of modifying the infeasible solutions to meet the constraints by adding or removing elements until a feasible solution is found. This approach was chosen as it allows the algorithm to handle the constraints efficiently and effectively.

# Screenshots
![Cities](https://github.com/EL-GAAMAZE/Antenna-Placement-Problem/blob/main/cities.png)


Figure 1: Map of Moroccan cities.

![Potential Sites](https://github.com/EL-GAAMAZE/Antenna-Placement-Problem/blob/main/potential_sites.png)


Figure 2: Map of potential antenna sites.

![Solution](https://github.com/EL-GAAMAZE/Antenna-Placement-Problem/blob/main/solution.png)


Figure 3: Map of the suboptimal antenna placement solution.



# Execution Time

Please note that the genetic algorithm implemented in this project may take a few seconds to run due to the large data size being used. However, compared to exact methods, this is still a relatively fast solution for the antenna placement problem modeled as a set covering problem. The algorithm is optimized for speed while still providing high-quality solutions. 

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/EL-GAAMAZE/Antenna-Placement-Problem/blob/main/LICENSE) file for details.
