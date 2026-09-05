from pathlib import Path
from typing import Any

from parser import Parser


class DocumentParser:
    """
    Orchestrates document ingestion for the RAG pipeline.

    Responsibilities:
    - Discover documents from a directory
    - Group documents by file type
    - Delegate parsing to a Parser implementation
    - Return the parsed documents
    """

    def __init__(self, directory: str | Path, parser: Parser):
        self.directory = Path(directory)
        self.parser = parser

    def discover_documents(self) -> list[Path]:
        if not self.directory.exists():
            raise FileNotFoundError(f"Directory does not exist: {self.directory}")

        if not self.directory.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {self.directory}")

        return sorted(
            path
            for path in self.directory.rglob("*")
            if path.is_file()
        )

    def group_documents_by_type(
        self,
        documents: list[Path],
    ) -> dict[str, list[Path]]:
        pass

    def parse_documents(
        self,
        documents: list[Path],
    ) -> list[Any]:
        pass

    def parse(self) -> list[Any]:
        pass