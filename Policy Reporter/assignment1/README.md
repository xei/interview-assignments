# Assignment 1

## Overview
This project selects the best `confidence threshold` for a binary classification model that achieves a recall ≥ 0.9. Among valid candidates, we needed to optimize a metric.

`Recall` alone might not be the best option because it was already considered in filtering, and overemphasizing it ignores false positives. While `Precision` could be a valid alternative, we decided to use the `F1 score` to harmonically balance both recall and precision for a more reliable selection.

## Input Data Structure
The input to the function is represented as a `dict[float, dict[str, int]]`. This format is chosen for being readable, explicit, JSON-friendly, easy to validate, and avoiding the need to align multiple lists by index.

```python
metrics_by_threshold = {
    0.1: {"tp": 90, "fp": 10, "tn": 80, "fn": 10},
    0.2: {"tp": 85, "fp": 8, "tn": 82, "fn": 15},
    0.3: {"tp": 80, "fp": 5, "tn": 85, "fn": 20},
    0.4: {"tp": 70, "fp": 3, "tn": 87, "fn": 30},
}
```

## Project Structure
```bash
├── __init__.py
├── core.py               # Main logic
├── metrics.py            # Metric calculations (recall, precision, F1)
├── exceptions.py         # Exceptions
├── logger.py             # Logging setup
├── main.py               # Example usage (CLI or script-style)
├── test_core.py          # Unit tests for core logic
└── README.md             # Documentation
```

## Run the Script
```bash
python -m assignment1.main
```

## Run Tests
```bash
python -m unittest assignment1.test_core
```