from typing import Optional, Tuple

from tetris.constants import BOARD_HEIGHT, BOARD_WIDTH, BoardState, Cell
from tetris.piece import Piece


class OPiece(Piece):
    piece_type = "O"

    def __init__(self) -> None:
        super().__init__()

        self.x = 4  # O piece x coordinate is the bottom left square
        self.y = 2

    def spawn_piece(self) -> list[Cell]:
        return [
            (self.y, self.x),
            (self.y - 1, self.x),
            (self.y - 1, self.x + 1),
            (self.y, self.x + 1),
        ]

    def move_left(
        self, board: BoardState
    ) -> Tuple[Optional[list[Cell]], Optional[list[Cell]]]:
        old, new = None, None

        if (
            self.x > 0
            and not board[self.y][self.x - 1]
            and not board[self.y - 1][self.x - 1]
        ):
            self.x -= 1
            old = [(self.y, self.x + 2), (self.y - 1, self.x + 2)]
            new = [(self.y, self.x), (self.y - 1, self.x)]

        return old, new

    def move_right(
        self, board: BoardState
    ) -> Tuple[Optional[list[Cell]], Optional[list[Cell]]]:
        old, new = None, None

        if (
            self.x < BOARD_WIDTH - 2
            and not board[self.y][self.x + 2]
            and not board[self.y - 1][self.x + 2]
        ):
            self.x += 1
            old = [(self.y, self.x - 1), (self.y - 1, self.x - 1)]
            new = [(self.y, self.x + 1), (self.y - 1, self.x + 1)]

        return old, new

    def rotate_clockwise(
        self, board: BoardState
    ) -> Tuple[Optional[list[Cell]], Optional[list[Cell]]]:
        return None, None

    def rotate_anticlockwise(
        self, board: BoardState
    ) -> Tuple[Optional[list[Cell]], Optional[list[Cell]]]:
        return None, None

    def has_landed(self, board: BoardState) -> bool:
        return bool(
            self.y == BOARD_HEIGHT - 1
            or board[self.y + 1][self.x]
            or board[self.y + 1][self.x + 1]
        )

    def fall(self) -> Tuple[list[Cell], list[Cell]]:
        self.y += 1
        old = [(self.y - 2, self.x), (self.y - 2, self.x + 1)]
        new = [(self.y, self.x), (self.y, self.x + 1)]

        return old, new
