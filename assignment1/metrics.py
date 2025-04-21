def compute_recall(tp: int, fn: int) -> float:
    denom = tp + fn
    return tp / denom if denom else 0.0

def compute_precision(tp: int, fp: int) -> float:
    denom = tp + fp
    return tp / denom if denom else 0.0

def compute_f1(precision: float, recall: float) -> float:
    denom = precision + recall
    return 2 * precision * recall / denom if denom else 0.0