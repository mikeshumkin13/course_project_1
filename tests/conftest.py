import sys
import os

# Добавляем путь к src/ в PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, '../src'))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)