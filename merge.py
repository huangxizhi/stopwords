import os


def merge(files_dir):
    files = os.listdir(files_dir)

    tokens = set()
    for file in files:
        filepath = os.path.join(files_dir, file)
        with open(filepath) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                tokens.add(line)

    tokens = list(tokens)
    tokens.sort()
    return tokens


def main():
    files_dir = 'reference'
    output_file = 'stopwords.txt'
    tokens = merge(files_dir)

    tokens = [t+"\n" for t in tokens]
    with open(output_file, 'w') as f:
        f.writelines(tokens)


def load_stopwords(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        return lines


if __name__ == '__main__':
    main()
