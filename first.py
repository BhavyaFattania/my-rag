from liteparse import LiteParse

parser = LiteParse()
result = parser.parse("document.pdf")

# Full document text
print(type(result))

# # Per-page data
# for page in result.pages:
#     print(f"Page {page.page_num}: {len(page.text_items)} text items")
