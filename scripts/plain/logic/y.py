import os
import sys



def p():
    current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to 'client' directory
    client_dir = os.path.normpath(os.path.join(current_dir, '..', 'client'))
    print(current_dir)
    print(client_dir)
    print(sys.path())
    return current_dir

if __name__ == "__main__":
    p()