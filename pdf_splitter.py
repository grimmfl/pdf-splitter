"""
module containing PdfSplitter class
"""
import sys

from pypdf import PdfReader, PageObject, PaperSize, PdfWriter
from pypdf.generic import RectangleObject

from exceptions import PaperSizeException


class PdfSplitter:
    """
    PdfSplitter splits all DIN A3 pages of a pdf into DIN A3 pages.
    :param filepath: path to pdf file
    :param result_suffix: suffix of the resulting pdf file
    """
    def __init__(self, filepath: str, result_suffix: str = "_splitted"):
        self._reader = PdfReader(filepath)
        self._writer = PdfWriter()
        self._path = filepath
        self._result_suffix = result_suffix

    def split(self):
        """
        Splits all DIN A3 pages into DIN A3 pages.
        """
        for page in self._reader.pages:
            if not self._should_split(page):
                self._writer.add_page(page)
                continue

            self._write_single_pages(page)

        with open(f"{self._path[:-4]}{self._result_suffix}.pdf", "wb") as file:
            self._writer.write(file)

    def _write_single_pages(self, page: PageObject):
        original_right = page.mediabox.right

        # TODO use DIN A4 dimensions here
        page.mediabox.right /= 2
        self._writer.add_page(page)

        page.mediabox.right = original_right
        page.mediabox.left = original_right / 2
        self._writer.add_page(page)

    @staticmethod
    def _should_split(page: PageObject):
        box: RectangleObject = page.mediabox
        width, height = box.width, box.height

        if (width, height) == PaperSize.A4 or (height, width) == PaperSize.A4:
            return False

        if (width, height) == PaperSize.A3 or (height, width) == PaperSize.A3:
            return True

        raise PaperSizeException(width, height)


if __name__ == '__main__':
    path = sys.argv[1]
    splitter = PdfSplitter(path)
    splitter.split()
