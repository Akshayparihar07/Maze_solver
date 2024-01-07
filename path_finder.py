def find_path(matrix, r, c):
    def is_valid(matrix, r, c):
        def is_valid(matrix, r, c):
            n = len(matrix)
            if 0 <= r < n and 0 <= c < n and matrix[r][c] == ' 🔵 |':
                return True
            return False


    def backtrack(matrix, r, c):
        n = len(matrix)
        if r == n-1 and c == n-1:
            return matrix

        # Down -> (r+1, c)
        if is_valid(matrix, r+1, c):
            matrix[r+1][c] = ' 🟢 |'
            if backtrack(matrix, r+1, c):
                return matrix

        # Left -> (r, c-1)
        elif is_valid(matrix, r, c-1):
            matrix[r][c-1] = ' 🟢 |'
            if backtrack(matrix, r, c-1):
                return matrix

        # Right -> (r, c+1)
        elif is_valid(matrix, r, c+1):
            matrix[r][c+1] = ' 🟢 |'
            if backtrack(matrix, r, c+1):
                return matrix

        # Up -> (r-1, c)
        elif is_valid(matrix, r-1, c):
            matrix[r-1][c] = ' 🟢 |'
            if backtrack(matrix, r-1, c):
                return matrix

    return backtrack(matrix, r, c)
