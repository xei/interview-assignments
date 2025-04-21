from .core import find_best_threshold

if __name__ == "__main__":
    example = {
        0.1: {"tp": 90, "fp": 10, "tn": 80, "fn": 10},
        0.2: {"tp": 85, "fp": 8, "tn": 82, "fn": 15},
        0.3: {"tp": 80, "fp": 5, "tn": 85, "fn": 20},
        0.4: {"tp": 70, "fp": 3, "tn": 87, "fn": 30},
    }
    result = find_best_threshold(example)
    print(f"Best threshold: {result}")