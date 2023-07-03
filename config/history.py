def update(filename: str, line: str) -> None:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = ""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(line + '\n')
            if lines:
                file.writelines(lines)
    except FileNotFoundError:
        update(filename, line)


def get_last(filename: str) -> str:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readline().strip()
    except FileNotFoundError:
        return ""
