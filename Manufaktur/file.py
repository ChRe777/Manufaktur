def file_to_str(path):
    with open(path) as f:
        return f.read()


def str_to_file(str, file):
    with open(file=file, mode="w") as f:
        return f.write(str)
