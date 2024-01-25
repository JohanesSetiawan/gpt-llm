from datasets import load_dataset
from pathlib import Path

CWD = Path(__file__).parent

dataset = load_dataset("bookcorpus", split="train",
                       cache_dir=f"{CWD.parent}/cache")

dataset.save_to_disk(f"{CWD.parent}/dataset")
