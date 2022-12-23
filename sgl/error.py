def error(message, exception=None, line=None, file_path=None):
    message = f"Error! {message}: {exception}"
    if line is not None:
        message += f" on line {line}"
    if file_path is not None and line is not None:
        file = open(file_path)
        line_string = file.readlines()[line - 1]
        message += f"\n{line} | {line_string}"
    print(message)