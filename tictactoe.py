from pydoc import plain


class TicTacToe:

    def __init__(self) -> None:
        self.nb_plays = 0
        self.plays = [(0, 0) for _ in range(9)]
