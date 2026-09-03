from pathlib import Path

from liteparse import LiteParse

from parser import Parser
from document import Document
from config import LiteParseConfig


class LiteParseAdapter(Parser):
    def __init__(self, config: LiteParseConfig):
        self.config = config
        self.parser = LiteParse(
            **self.config.to_dict()
        )

    def parse_document(self, files: list[Path]) -> list[Document]:
        documents = []

        for file in files:
            result = self.parser.parse(file)

            document = Document(
                content=result.text,
                source=str(file),
                metadata={}
            )

            documents.append(document)

        return documents