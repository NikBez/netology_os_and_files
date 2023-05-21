from pathlib import Path
import os


def merge_files(path):
    files = []
    for file in os.scandir(path):
        if not Path(file).suffix == '.txt':
            continue
        with open(file.path, 'r') as text_file:
            lines = text_file.readlines()
            text = ''.join(lines)
            lines_count = len(lines)
            filename = Path(file).name

            files.append((filename, lines_count, text))
    files = sorted(files, key=lambda x: x[1])

    with open('result.txt', 'w') as result:
        for temp_file in files:
            filename, lines, text = temp_file
            result.write(f'{filename}\n{lines_count}\n{text}\n')


if __name__ == "__main__":
    base_path = os.getcwd()
    merge_dir = Path(base_path)/'task_3'
    merge_files(merge_dir)
