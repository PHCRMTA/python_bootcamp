def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}

    for course, day in pairs:
        result.setdefault(day, []).append(course)

    for day in result:
        result[day].sort()

    return result


