"""Convenient entry point for running the game from an IDE.

Run this file with: python main.py
"""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from car_simulation.app import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
