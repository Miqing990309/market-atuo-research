import os

directory = "output"

def main():
    # current dir
    current_path = os.getcwd()
    # parent_dir = os.path.abspath(os.path.join(current_path, os.pardir))
    # Path
    path = os.path.join(current_path, directory)
    if not os.path.exists(path):
        os.mkdir(path)

if __name__ == '__main__':
    main()

