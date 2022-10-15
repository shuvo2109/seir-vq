# seir-vq
Python code and Excel file for the SEIR-VQ Model. The python code and excel file draws the graph of the SEIR-VQ model presented in [this paper](https://drive.google.com/file/d/1FkL5T_2S8f0VZjoAXryJ-zmQ7jkBF0Ka/view?usp=sharing).

## Files Included
- `python_plot.py` contains the Python code used for the plotting of the graph
- `excel_plot.xlsx` contains the Excel file for the plotting of the graph

## `python_plot.py`
### Required Version
This program requires `Python 3` or above. It was originally written using `Python 3.10`.

### Required Libraries and Modules
This program uses the `matplotlib` module for plotting the graph.

## `excel_plot.xlsx`
### Required Version
This file runs of Microsoft Excel 2013 and beyond. It was originally developed in Microsoft Excel 2016.

### How to Use
- Open the file and change the values of the parameters in cells from `B2` to `B10`.
- Enter the initial values of the compartments in the cells from `E2` to `J2`

The following quantities / plots are automatically updated / drawn based on the input values:
- The values of S(t), E(t), I(t), R(t), V(t) and Q(t) for t>0
- The values of E+I+Q (infected compartments) for t>0
- The values of the proportion of each compartments in endemic equilibrium (at t=400)
- Basic Reproduction Number R0
- The values of I_max and (E+I+Q)_max
- The plot of Epidemic Dynamics against time for 0<t<400

## Contact Information
For any queries or confusion, contact: rahman.fahimur21@gmail.com
