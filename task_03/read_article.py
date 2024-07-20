
def read_article(path: str) -> str:
    content = ""
    with open(path, 'r', encoding='utf-8') as f:
        list_content = f.readlines()
    return content.join(list_content)

