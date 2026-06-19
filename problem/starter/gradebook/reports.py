"""gradebook.reports — build a printable report from grade records."""

from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def _format_score(score: float) -> str:
    text = f"{score:.2f}"
    if text.endswith(".00"):
        return text[:-3] + ".0"
    if text.endswith("0"):
        return text[:-1]
    return text


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    averages = average_per_student(records)
    subjects = sorted(subjects_offered(records))
    top_name, top_avg = top_scorer(records)
    passed = passing_students(records)

    name_width = max((len(name) for name in averages), default=0)

    lines = [
        "=== Gradebook Report ===",
        f"Total records: {len(records)}",
        f"Subjects offered: {', '.join(subjects)}",
        "",
        "Averages:",
    ]

    for name in sorted(averages):
        lines.append(f"  {name.ljust(name_width)} : {_format_score(averages[name])}")

    lines.extend([
        "",
        f"Top scorer: {top_name} ({_format_score(top_avg)})",
        f"Passing students (>= 60.0): {', '.join(passed)}",
    ])

    return "\n".join(lines)
