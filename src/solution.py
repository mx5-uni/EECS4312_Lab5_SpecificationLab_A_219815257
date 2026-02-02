## Student Name: Anna Maximova
## Student ID: 219815257

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict

def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    """
    Suggest possible meeting start times for a given day.

    Args:
        events: List of dicts with keys {"start": "HH:MM", "end": "HH:MM"}
        meeting_duration: Desired meeting length in minutes
        day: Three-letter day abbreviation (e.g., "Mon", "Tue", ... "Fri")

    Returns:
        List of valid start times as "HH:MM" sorted ascending
    """
    # TODO: Implement this function
    #raise NotImplementedError("suggest_slots function has not been implemented yet")


    def to_minutes(t: str) -> int:
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    def to_time(m: int) -> str:
        return f"{m // 60:02d}:{m % 60:02d}"

    # Convert and sort events by start time
    intervals = sorted(
        [(to_minutes(e["start"]), to_minutes(e["end"])) for e in events],
        key=lambda x: x[0]
    )

    available_slots = []
    day_start = 0
    day_end = 24 * 60

    prev_end = day_start

    for start, end in intervals:
        if start - prev_end >= meeting_duration:
            available_slots.append(
                f"{to_time(prev_end)}-{to_time(start)}"
            )
        prev_end = max(prev_end, end)

    # Check after last event
    if day_end - prev_end >= meeting_duration:
        available_slots.append(
            f"{to_time(prev_end)}-{to_time(day_end)}"
        )

    return available_slots