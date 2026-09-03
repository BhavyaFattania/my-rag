from dataclasses import dataclass
from typing import Optional

@dataclass(freeze=True)
class directory_path:
    path: str

@dataclass(freeze=True)
class LiteParseConfig:
    ocr_enabled: bool = True
    ocr_language: str = "eng"
    ocr_server_url: Optional[str] = None
    tessdata_path: Optional[str] = None

    max_pages: int = 1000
    target_pages: Optional[str] = None

    dpi: int = 150

    output_format: str = "markdown"

    image_mode: str = "placeholder"
    extract_images: bool = False
    image_output_dir: Optional[str] = None

    extract_links: bool = True

    continue_on_page_error: bool = False