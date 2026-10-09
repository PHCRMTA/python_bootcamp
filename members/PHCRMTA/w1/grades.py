def summary(scores):
    if len(scores) == 0:
        raise ValueError("The scores list is empty.")

    min_val = scores[0]
    max_val = scores[0]
    sum = 0

    for score in scores:
        if score < min_val:
            min_val = score
        if score > max_val:
            max_val = score
        sum += score

    n = len(scores)
    mean_val = sum / n

    sorted_scores = sorted(scores)

    if n % 2 != 0:
        median_val = sorted_scores[n // 2]
    else:
        mid1 = (n // 2) - 1
        mid2 = n // 2
        median_val = (sorted_scores[mid1] + sorted_scores[mid2]) / 2

    return {
        "min": min_val,
        "max": max_val,
        "mean": round(mean_val, 2),
        "median": round(median_val, 2)
    }
