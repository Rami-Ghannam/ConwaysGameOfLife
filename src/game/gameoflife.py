from collections import Counter
from enum import Enum

class Cell(Enum):
  Dead = 0
  Alive = 1

def get_bounds(points):
    if len(points) < 2: return points * 2
    if len(points) is 2: return sorted( sorted( points, key=lambda pnt: pnt[1]), key=lambda pnt: pnt[0])   
    return [ (f(pnt[0] for pnt in points), f(pnt[1] for pnt in points)) for f in [min, max] ]
  
def get_next_state(current_state, number_of_live_neighbors):
  return Cell.Alive if number_of_live_neighbors is 3 \
    or number_of_live_neighbors is 2 and current_state is Cell.Alive \
    else Cell.Dead

def generate_signals(cell):
  return [ (cell[0] + i, cell[1] + j) for i in range(-1, 2) \
    for j in range(-1, 2) if (i, j) != (0, 0) ]

def generate_signals_for_positions(seed_cells):
  return [ neighbor for cell in seed_cells \
    for neighbor in generate_signals(cell) ]

def count_signals(signals):
  return Counter(signals)

def next_generation(seed_cells):
  signals = generate_signals_for_positions(seed_cells)
  location_signals_count = count_signals(signals)

  dead_or_alive = lambda cell, count: get_next_state(Cell.Alive, count) \
    if cell in seed_cells else get_next_state(Cell.Dead, count)
  
  return [ cell for cell, count in location_signals_count.items() \
    if dead_or_alive(cell, count) is Cell.Alive ]
  