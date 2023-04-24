import sys, os
from pathlib import Path

if (dir := str(Path(os.getcwd()).parent)) not in sys.path:
    sys.path.insert(0, dir)

