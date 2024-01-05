def find_path(matrix):
    n = len(matrix)

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and matrix[x][y] == "🔵"

    def dfs(x, y):
        if not is_valid(x, y):
            return False

        matrix[x][y] = "🟢"  # Mark the current cell as part of the path

        if (x, y) == (n - 1, n - 1):  # Reached the destination
            return True

        # Explore all possible directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y) and matrix[new_x][new_y] != "🟢":
                if dfs(new_x, new_y):
                    return True

        matrix[x][y] = "🔵"  # Unmark the current cell if no valid path found
        return False

    # Start DFS from the source (0, 0)
    if dfs(0, 0):
        return matrix
    else:
        return None

