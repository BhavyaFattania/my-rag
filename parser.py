from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Parser(ABC):
    """
    Abstraction for any document parsing backend.

    Examples:
    - LiteParse
    - LlamaParse
    - PyMuPDF
    - Unstructured
    """

    @abstractmethod
    def parse_document(self, files: list[Path]) -> list[Document]:
        pass


