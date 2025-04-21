from .metrics import compute_recall, compute_precision, compute_f1
from .logger import logger


def find_best_threshold(
        metrics_by_threshold: dict[float, dict[str, int]]
) -> float | None:
    best_threshold = None
    best_score = -1.0

    for threshold, metrics in sorted(metrics_by_threshold.items()):
        tp, fp, fn = (metrics.get("tp", 0),
                      metrics.get("fp", 0),
                      metrics.get("fn", 0))
        recall = compute_recall(tp, fn)
        if recall >= 0.9:
            precision = compute_precision(tp, fp)
            f1 = compute_f1(precision, recall)
            logger.debug(f"Threshold {threshold}: Precision={precision:.2f}, Recall={recall:.2f}, F1={f1:.2f}")
            if f1 > best_score:
                best_score = f1
                best_threshold = threshold

    return best_threshold