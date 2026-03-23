import random
from src.grid import Grid


def generate_occlusion_reversal(grid_size=(12, 12), size_range=(2, 5), colors=("red", "blue")):
    rows, cols = grid_size
    grid_input = Grid(rows, cols)
    grid_output = Grid(rows, cols)

    w, h = random.randint(*size_range), random.randint(*size_range)

    # Random position for back block (x and y of bottom left corner of the back block)
    x1 = random.randint(min(size_range), cols - w - min(size_range))
    y1 = random.randint(min(size_range), rows - h - min(size_range))
    back_block = {"col_min": x1, "row_min": y1, "col_max": x1 + w, "row_max": y1 + h, "color": colors[0]}

    min_x2 = x1 + 1
    max_x2 = x1 + w - 1
    min_y2 = y1 + 1
    max_y2 = y1 + h - 1

    x2 = random.randint(min_x2, max_x2)
    y2 = random.randint(min_y2, max_y2)

    front_block = {"col_min": x2, "row_min": y2, "col_max": x2 + w, "row_max": y2 + h, "color": colors[1]}

    # Input: back first, front second
    grid_input.fill_rect(**back_block)
    grid_input.fill_rect(**front_block)

    # Output: front first, back second (reversed)
    grid_output.fill_rect(**front_block)
    grid_output.fill_rect(**back_block)

    for _ in range(random.randrange(4)):
        grid_input.rotate_ccw_90()
        grid_output.rotate_ccw_90()

    params = {
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params
