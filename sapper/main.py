from random import randint


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False) -> None:
        self.around_mines: int = around_mines
        self.mine: bool = mine
        self.fl_open: bool = False


class GamePole:
    def __init__(self, field_size: int, mines: int) -> None:
        if mines > field_size * field_size:
            raise ValueError(
                "Number of mines should be less or "
                "equal to the total number of cells."
            )
        self.field_size: int = field_size
        self.mines: int = mines
        self.pole: list[list[Cell]] = [
            [Cell(0, False) for _ in range(field_size)] for _ in range(field_size)
        ]
        self.mine_positions: set[tuple[int, int]] = set()
        self._place_mines()
        self._count_mines_around()

    def _place_mines(self):
        placed = 0

        while placed < self.mines:
            mine_x = randint(0, self.field_size - 1)
            mine_y = randint(0, self.field_size - 1)
            if (mine_x, mine_y) not in self.mine_positions:
                self.mine_positions.add((mine_x, mine_y))
                self.pole[mine_x][mine_y].mine = True
                placed += 1

    def _count_mines_around(self):
        for mine_x, mine_y in self.mine_positions:
            for neighbor_x in range(
                max(0, mine_x - 1), min(self.field_size, mine_x + 2)
            ):
                for neighbor_y in range(
                    max(0, mine_y - 1), min(self.field_size, mine_y + 2)
                ):
                    if not self.pole[neighbor_x][neighbor_y].mine:
                        self.pole[neighbor_x][neighbor_y].around_mines += 1

    def _is_valid_position(self, x, y):
        return 0 <= x < self.field_size and 0 <= y < self.field_size

    def show(self):
        for cell_x in range(self.field_size):
            row = []
            for cell_y in range(self.field_size):
                if not self.pole[cell_x][cell_y].fl_open:
                    row.append("#")
                elif self.pole[cell_x][cell_y].mine:
                    row.append("*")
                else:
                    row.append(str(self.pole[cell_x][cell_y].around_mines))
            print(" ".join(row))

    def open_cell(self, cell_x: int, cell_y: int):
        if not self._is_valid_position(cell_x, cell_y):
            raise ValueError("Cell position is out of bounds.")

        if self.pole[cell_x][cell_y].fl_open:
            return "Cell already open"

        self.pole[cell_x][cell_y].fl_open = True
        if self.pole[cell_x][cell_y].mine:
            return "Game over"

        if self.pole[cell_x][cell_y].around_mines == 0:
            for neighbor_x in range(
                max(0, cell_x - 1), min(self.field_size, cell_x + 2)
            ):
                for neighbor_y in range(
                    max(0, cell_y - 1), min(self.field_size, cell_y + 2)
                ):
                    if not self.pole[neighbor_x][neighbor_y].fl_open:
                        self.open_cell(neighbor_x, neighbor_y)

        return "Continue"


# pole = GamePole(10, 12)


# pole.open_cell(3, 5)
# pole.open_cell(0, 0)
# pole.show()
