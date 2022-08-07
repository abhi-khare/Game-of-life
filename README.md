# Convery's Game of life



The rules of game are very simple : </br>
* If a cell is alive and surrounded by less than 2 alive cell, it dies due to loneliness.
* If a cell is alive and surrounded by more than 3 alive cell, it dies due to overpopulation.
* If a cell is alive and surrounded by either 2 or 3 alive cell, it continues to live.
* If a cell is dead and surrounded by exactly 3 alive cell, it borns again.



<h1>Runbook</h1> <br />

This implementation uses Pygame to render artifacts on the screen and uses Numpy to store the cell state and processing. All the required packages can be installed using the below command:
```bash
pip install -r requirements.txt
```
Run the program directly and use --help argument for info on various command line argument:
```python
python main.py
```
<h3> On-Screen Controls </h3>

| Input        | Action           | 
| ------------- |:-------------:| 
| Left Click     | set cell on the grid | 
| Key : s      | start simulation    |
| Key : d | pause simulation     |
| Key : r      | reset grid   |
| Key : 0 | preset : Glider     |
| Key : 1      | preset : pentomino    |
