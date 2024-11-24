def solve():
    w, h = map(int, input().split())
    grid = [input().strip() for _ in range(h)]

    def find_square():
        for r1 in range(h - 4):
            for c1 in range(w - 4):
                if grid[r1][c1] == '1':
                    if any(grid[r1 + i][c1] == '0' for i in range(1, 5)) or any(grid[r1][c1 + i] == "0" for i in range(1, 5)):
                        continue
                    # Check increasing square sizes starting from (r1, c1)
                    max_size = min(h - r1, w - c1)
                    for size in range(5, max_size + 1):
                        r2 = r1 + size - 1
                        c2 = c1 + size - 1

                        # Check borders of the square
                        is_square = True
                        for r in range(r1, r2 + 1):
                            if grid[r][c1] != '1' or grid[r][c2] != '1':
                                is_square = False
                                break
                        if is_square:
                            for c in range(c1, c2 + 1):
                                if grid[r1][c] != '1' or grid[r2][c] != '1':
                                    is_square = False
                                    break

                        if is_square:
                            return r1, c1, r2, c2
        return None

    square = find_square()

    if square is None:
        print("Printing error")
        return

    r1, c1, r2, c2 = square

    def is_marked():
        size = r2 - r1 + 1
        for i in range(size):
            if grid[r1 + i][c1 + i] == '0' or grid[r2 - i][c1 + i] == '0':
                return False
        return True

    if is_marked():
        print("Marked")
    else:
        print("Not marked")


solve()
