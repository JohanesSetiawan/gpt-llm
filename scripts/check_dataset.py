import datasets

from pathlib import Path

CWD = Path(__file__).parent

df = datasets.load_from_disk(f"{CWD.parent}/dataset")

print(df[0])
