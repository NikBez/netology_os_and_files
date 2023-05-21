from pathlib import Path
import os


def merge_files(path):
    files = []
    for file in os.scandir(path):
        lines = 0
        text = ''
        if not Path(file).suffix == '.txt':
            continue
        with open(file.path, 'r') as text_file:
            for line in text_file:
                lines += 1
                text += line
            filename = Path(file).name
            files.append((filename, lines, text))

    files = sorted(files, key=lambda x: x[1])

    with open('result.txt', 'w') as result:
        for temp_file in files:
            filename, lines, text = temp_file
            result.write(f'{filename}\n{lines}\n{text}\n')


if __name__ == "__main__":
    merge_dir = Path('task_3')
    merge_files(merge_dir)
