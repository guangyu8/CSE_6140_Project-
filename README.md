# CSE_6140_Project
Exploring algorithms that aim to solve the **Traveling Salesman Problem** and implemented an exact branch-and-bound algorithm, several heuristic algorithms that approximate the optimal result such as $\textsc{MST-APPROX}$ and $\textsc{FARTHEST-INSERTION}$, and local-search algorithms such as $\textsc{2-EXCHANGE}$. We designed experiments to compare the results from different approaches, and we identified classes of graphs for which certain methods outperform others. The coding was implemented in $\textbf{python}$.
## Repository Structure
```bash
DATA
└── Approx_out
└── BnB_out
└── LS1_out
└── LS2_out
branch_n_bound_depth.py
branch_n_bound_LB_rate.py
branch_n_bound.py
MSTApprox.py
simann.py
tsp_main.py
two_opt.py
```
- DATA: Folder with the data instances and solution file; contains each algorithm's outputs in respective folders
- branch_n_bound_depth.py: Depth-first approach
- branch_n_bound_LB_rate.py: Priority based approach
- branch_n_bound.py: Best-first approach
- MSTApprox.py: Minimum spanning tree approximation
- simann.py: Simulated Annealing local search algorithm
- tsp_main.py: executible
- two_opt.py: 2-opt local search algorithm

## Running
### Examples
```
python tsp_main.py -alg BnB -inst DATA/Atlanta.tsp -time 500
python tsp_main.py -alg LS1 -inst DATA/Roanoke.tsp -time 100 -seed 0
```
- `alg`: "BnB", "Approx", "LS1", "LS2"
- `inst`: instance from DATA folder
- `time`:  time cutoff
- `seed`: random seed (necessary for local search algorithms)
