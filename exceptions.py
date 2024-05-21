"""
All custom exceptions
"""


class PaperSizeException(Exception):
    """
    Exception raised when the paper size is invalid.
    """
    def __init__(self, width: float, height: float):
        super().__init__(f'Invalid dimensions {(width, height)}')
