from itertools import chain, starmap


def neighbours(x: int, y: int) -> tuple:
    ''' generate the coordinate neighbours of x and y including itself'''
    yield x, y
    yield x+1, y
    yield x-1, y
    yield x, y+1
    yield x, y-1
    yield x+1, y+1
    yield x-1, y-1
    yield x-1, y+1
    yield x+1, y-1


def update(board: set[tuple]) -> set[tuple]:
    ''' Updates a set of points based on the rules of Conway's Game of Life'''
    full_board = set(chain(*starmap(neighbours, board)))
    new_board = set()

    for point in full_board:
        tot_neighbours = sum((n in board for n in neighbours(*point)))
        if tot_neighbours == 3 or (tot_neighbours == 2 and point in board):
            new_board.add(point)

    del full_board, board

    return new_board


if __name__ == '__main__':
    for _ in range(1000):
        points = {(-1, 1), (2, 6), (-1, -1), (1, 1), (0, 0)}
        points = update(points)
        if not points:
            print("Complete")
            break
        print(points)
