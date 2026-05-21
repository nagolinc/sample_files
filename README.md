# sample_files

Small helper functions for sampling text, weighted JSON keys, and generated words.

## Installation

Install directly from GitHub:

```powershell
python -m pip install git+https://github.com/nagolinc/sample_files.git
```

For local development, clone the repository and install it in editable mode:

```powershell
git clone git@github.com:nagolinc/sample_files.git
cd sample_files
python -m pip install -e .
```

## Usage

```python
from sample_files import sample_files, random_word, extract_tag, get_filename

print(random_word())

text = "before <name>Ada</name> after"
print(extract_tag(text, "name"))

print(get_filename("A sample image prompt", extension="png"))
```

Sample lines from text files:

```python
from sample_files import sample_files

result = sample_files(["names.txt", "places.txt"], k=2, seed=123)
print(result)
```

For `.json` files, values are treated as weights and keys are sampled:

```json
{
  "apple": 10,
  "banana": 3,
  "cherry": 1
}
```

```python
print(sample_files(["weighted_words.json"], k=5))
```

Use `"RANDOM"` to generate a random pronounceable word:

```python
print(sample_files(["RANDOM", "RANDOM", "RANDOM"]))
```

Sample from a list while avoiding immediate repeats:

```python
from sample_files import h_sample

history = {}
items = ["alpha", "bravo", "charlie"]

print(h_sample(items, history))
print(h_sample(items, history))
```

`h_sample` usually favors recent items near the end of the list, sometimes chooses uniformly, and stores the last result in `history["prev"]`.

## Requirements

Python 3.6 or newer.
