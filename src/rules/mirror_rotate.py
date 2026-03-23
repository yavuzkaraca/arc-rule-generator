from src.rules.occlusion import generate_occlusion_reversal


def generate_occlusion_mirror_x(grid_size=(12, 12), size_range=(2, 5), colors=("red", "blue")):
    grid_input, _, _ = generate_occlusion_reversal(
        grid_size=grid_size, size_range=size_range, colors=colors
    )

    grid_output = grid_input.copy()
    _transform_occupied_box(grid_output, lambda f: f.mirror_x())

    params = {
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params


def generate_occlusion_mirror_y(grid_size=(12, 12), size_range=(2, 5), colors=("red", "blue")):
    grid_input, _, _ = generate_occlusion_reversal(
        grid_size=grid_size, size_range=size_range, colors=colors
    )

    grid_output = grid_input.copy()
    _transform_occupied_box(grid_output, lambda f: f.mirror_y())

    params = {
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params


def generate_occlusion_rotate_90(grid_size=(12, 12), size_range=(2, 5), colors=("red", "blue")):
    grid_input, _, _ = generate_occlusion_reversal(
        grid_size=grid_size, size_range=size_range, colors=colors
    )

    grid_output = grid_input.copy()
    _transform_occupied_square_box(grid_output, lambda f: f.rotate_ccw_90())

    params = {
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params


def generate_occlusion_rotate_180(grid_size=(12, 12), size_range=(2, 5), colors=("red", "blue")):
    grid_input, _, _ = generate_occlusion_reversal(
        grid_size=grid_size, size_range=size_range, colors=colors
    )

    grid_output = grid_input.copy()
    _transform_occupied_box(grid_output, lambda f: f.rotate_180())

    params = {
        "grid_size": grid_size,
        "colors": colors,
        "n_objects": 2
    }

    return grid_input, grid_output, params


def _transform_occupied_box(grid, transform_fn):
    row_min, row_max, col_min, col_max = grid.get_occupied_bounding_box()
    box = grid.extract_box(row_min, row_max, col_min, col_max)
    transform_fn(box)
    grid.paste_at(box, row_min, col_min)


def _transform_occupied_square_box(grid, transform_fn):
    # Needed for rotate 90 because otherwise the dimensions do not fit
    row_min, row_max, col_min, col_max = grid.get_occupied_bounding_box()
    row_min, row_max, col_min, col_max = _make_square_box(
        row_min, row_max, col_min, col_max, grid.rows, grid.cols
    )
    box = grid.extract_box(row_min, row_max, col_min, col_max)
    transform_fn(box)
    grid.paste_at(box, row_min, col_min)


def _make_square_box(row_min, row_max, col_min, col_max, max_rows, max_cols):
    h = row_max - row_min + 1
    w = col_max - col_min + 1
    side = max(h, w)

    row_max = min(row_min + side - 1, max_rows - 1)
    col_max = min(col_min + side - 1, max_cols - 1)

    row_min = row_max - side + 1
    col_min = col_max - side + 1

    return row_min, row_max, col_min, col_max
