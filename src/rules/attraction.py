import random

from src.grid import Grid
from src.util import rand_between


def generate_color_attraction(grid_size=(12, 12), size_range=(2, 5), colors=("red", "blue")):
    rows, cols = grid_size
    grid_input, grid_output = Grid(rows, cols), Grid(rows, cols)

    w1, h1, w2, h2 = (rand_between(*size_range) for _ in range(4))

    x1 = rand_between(0, cols - w1 - w2 - 1)
    y1 = rand_between(0, rows - h1 - 1)

    x2 = rand_between(x1 + w1 + 1, cols - w2)
    y2 = rand_between(max(0, y1 - h2 + 1), min(rows - h2, y1 + h1 - 1))

    grid_input.fill_rect(col_min=x1, row_min=y1, col_max=x1 + w1 - 1, row_max=y1 + h1 - 1, color=colors[0])
    grid_input.fill_rect(col_min=x2, row_min=y2, col_max=x2 + w2 - 1, row_max=y2 + h2 - 1, color=colors[1])

    grid_output.fill_rect(col_min=x1, row_min=y1, col_max=x1 + w1 - 1, row_max=y1 + h1 - 1, color=colors[0])
    grid_output.fill_rect(col_min=x1 + w1, row_min=y2, col_max=x1 + w1 + w2 - 1, row_max=y2 + h2 - 1, color=colors[1])

    for _ in range(random.randrange(4)):  # 0–3 times
        grid_input.rotate_ccw_90()
        grid_output.rotate_ccw_90()

    params = {
        "event": "attraction",
        "condition": ["color", "movement"],
        "stimulus": "big_blocks",
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2,
        "bigger_block": "red" if (w1*h1 > w2*h2) else "blue"
    }

    return grid_input, grid_output, params


def generate_size_attraction(grid_size=(12, 12), size_range=(3, 6), colors=("red", "blue")):
    rows, cols = grid_size
    grid_input, grid_output = Grid(rows, cols), Grid(rows, cols)

    w1, h1 = (rand_between(*size_range) for _ in range(2))
    w2 = rand_between(2, w1 - 1)
    h2 = rand_between(2, h1 - 1)

    x1 = rand_between(0, cols - w1 - w2 - 1)
    y1 = rand_between(0, rows - h1 - 1)

    x2 = rand_between(x1 + w1 + 1, cols - w2)
    y2 = rand_between(max(0, y1 - h2 + 1), min(rows - h2, y1 + h1 - 1))

    c_big, c_small = random.getrandbits(1), random.getrandbits(1)

    grid_input.fill_rect(col_min=x1, row_min=y1, col_max=x1 + w1 - 1, row_max=y1 + h1 - 1, color=colors[c_big])
    grid_input.fill_rect(col_min=x2, row_min=y2, col_max=x2 + w2 - 1, row_max=y2 + h2 - 1, color=colors[c_small])

    grid_output.fill_rect(col_min=x1, row_min=y1, col_max=x1 + w1 - 1, row_max=y1 + h1 - 1, color=colors[c_big])
    grid_output.fill_rect(col_min=x1 + w1, row_min=y2, col_max=x1 + w1 + w2 - 1, row_max=y2 + h2 - 1,
                          color=colors[c_small])

    for _ in range(random.randrange(4)):  # 0–3 times
        grid_input.rotate_ccw_90()
        grid_output.rotate_ccw_90()

    params = {
        "event": "attraction",
        "condition": ["shape", "movement"],
        "stimulus": "big_blocks",
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params


def generate_repulsion(grid_size=(12, 12), size_range=(2, 5), colors=("red", "blue")):
    rows, cols = grid_size
    grid_input, grid_output = Grid(rows, cols), Grid(rows, cols)

    w1, h1, w2, h2 = (rand_between(*size_range) for _ in range(4))

    x1 = rand_between(0, cols - w1 - w2 - 1)
    y1 = rand_between(h2, rows - h1 - 1)

    x2 = x1 + w1
    y2 = rand_between(y1 - h2 // 2 + 1, y1 + h2 // 2 - 1)

    grid_input.fill_rect(col_min=x1, row_min=y1, col_max=x1 + w1 - 1, row_max=y1 + h1 - 1, color=colors[0])
    grid_input.fill_rect(col_min=x2, row_min=y2, col_max=x2 + w2 - 1, row_max=y2 + h2 - 1, color=colors[1])

    grid_output.fill_rect(col_min=x1, row_min=y1, col_max=x1 + w1 - 1, row_max=y1 + h1 - 1, color=colors[0])
    grid_output.fill_rect(col_min=cols - w2, row_min=y2, col_max=cols, row_max=y2 + h2 - 1, color=colors[1])

    for _ in range(random.randrange(4)):  # 0–3 times
        grid_input.rotate_ccw_90()
        grid_output.rotate_ccw_90()

    params = {
        "event": "attraction",
        "condition": ["color", "movement"],
        "stimulus": "big_blocks",
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params


def generate_gravity(grid_size=(12, 12), size_range=(2, 6), colors=("red", "blue")):
    rows, cols = grid_size
    grid_input, grid_output = Grid(rows, cols), Grid(rows, cols)

    w1, h1, w2, h2 = (rand_between(*size_range) for _ in range(4))

    x1 = rand_between(0, cols - w1 - w2 - 1)
    y1 = rand_between(1, rows - h1 - 1)

    x2 = rand_between(x1 + w1 + 1, cols - w2)
    y2 = rand_between(1, rows - h2 - 1)

    c_big, c_small = random.getrandbits(1), random.getrandbits(1)

    grid_input.fill_rect(col_min=x1, row_min=y1, col_max=x1 + w1 - 1, row_max=y1 + h1 - 1, color=colors[c_big])
    grid_input.fill_rect(col_min=x2, row_min=y2, col_max=x2 + w2 - 1, row_max=y2 + h2 - 1, color=colors[c_small])

    grid_output.fill_rect(col_min=x1, row_min=0, col_max=x1 + w1 - 1, row_max=0 + h1 - 1, color=colors[c_big])
    grid_output.fill_rect(col_min=x2, row_min=0, col_max=x2 + w2 - 1, row_max=0 + h2 - 1, color=colors[c_small])

    params = {
        "event": "attraction",
        "condition": "movement",
        "stimulus": "big_blocks",
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params


def generate_float(grid_size=(12, 12), size_range=(2, 6), colors=("red", "blue")):
    grid_input, grid_output, params = generate_gravity(grid_size=grid_size, size_range=size_range, colors=colors)
    # funny idea: floating is opposite direction gravity
    grid_input.rotate_180()
    grid_output.rotate_180()

    params = {
        "event": "attraction",
        "condition": "movement",
        "stimulus": "big_blocks",
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params


def generate_dots_gravity(
        grid_size=(12, 12),
        n_objects=(3, 10),
        colors=("red", "blue"),
):
    rows, cols = grid_size
    grid_input = Grid(rows, cols)

    n = rand_between(*n_objects)
    positions = random.sample([(r, c) for r in range(rows) for c in range(cols)], n)

    for r, c in positions:
        grid_input.fill_cell(r, c, random.choice(colors))

    grid_output = apply_gravity(grid_input)

    params = {
        "event": "attraction",
        "condition": "movement",
        "stimulus": "dots",
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": n
    }

    return grid_input, grid_output, params


def apply_gravity(grid: Grid) -> Grid:
    rows, cols = grid.rows, grid.cols
    out = Grid(rows, cols)

    for c in range(cols):
        col = [grid.get(r, c) for r in range(rows) if grid.get(r, c) != "black"]
        r = 0  # bottom is row 0 in coordinate system
        for color in col:  # keep order stable
            out.fill_cell(r, c, color)
            r += 1

    return out
