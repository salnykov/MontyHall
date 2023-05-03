# Simulating the Monty Hall Problem

This code simulates the **Monty Hall problem**, a probability puzzle named after the host of the game show *"Let's Make a Deal"*, Monty Hall. The problem consists of three doors, behind one of which is a valuable prize, while behind the other two doors, there are less valuable prizes, such as goats.

The player chooses one of the doors. Then, the host, who knows what is behind each door, opens one of the other two doors to reveal a goat. The player is then given the choice to stick with their original choice or switch to the other unopened door. The question is, is it better to stick with the original choice or switch?

## How to Use the Code
To run the code, follow these steps:

1. Install the required dependencies: **random** and **matplotlib**. You can install them using **pip**:
```
pip install random matplotlib
```

2. Clone or download the code to your local machine.

3. Run the monty_hall.py file using a Python interpreter:
```
python monty_hall.py
```
The code will run 5000 simulations for both the "no change" and "change" strategies, each with 100 iterations, and display the results in two histograms using the matplotlib library.

## File Structure
The project includes one file:

**monty_hall.py**: contains the Python code to simulate the Monty Hall problem and generate the histograms.

## Contributing
Contributions to the code are welcome. If you find a bug or have a feature request, please open an issue on the GitHub repository. If you want to contribute code, please fork the repository and submit a pull request.

## License
This code is released under the MIT License. See LICENSE for more information.
