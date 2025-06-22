import os
import sys

def find_tf_directories(root_dir):
    """
    Walks the directory tree starting at `root_dir` and returns a list of directories
    that contain at least one .tf or .tf.json file.
    """
    tf_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.tf') or file.endswith('.tf.json'):
                tf_dirs.append(dirpath)
                break  # Stop checking files in this directory once a match is found
    return tf_dirs

def main():
    # Use current directory as default or allow passing a different directory as an argument.
    root_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    directories = find_tf_directories(root_dir)
    if directories:
        print("Directories containing .tf/.tf.json files:")
        for directory in directories:
            print(f" - {directory}")
    else:
        print("No directories with .tf or .tf.json files were found.")

if __name__ == "__main__":
    main()
