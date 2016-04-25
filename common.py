import re
import os

def prepare_relative_path(path):
    abs_path_pattern = "^(\w:)?/.+"
    p = re.compile(abs_path_pattern)
    result_path = path
    if not p.search(path):
        result_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
    return result_path