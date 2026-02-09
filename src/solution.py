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
        h, m = map(int, t.split(":"))
        return h * 60 + m

    def to_time_str(minutes: int) -> str:
        return f"{minutes // 60:02d}:{minutes % 60:02d}"

    WORK_START = 9 * 60        # 09:00
    WORK_END = 17 * 60         # 17:00
    LUNCH_START = 12 * 60      # 12:00
    LUNCH_END = 13 * 60        # 13:00
    BUFFER = 15               # 15-minute buffer after events

    busy_intervals = []
    for event in events:
        start = to_minutes(event["start"])
        end = to_minutes(event["end"]) + BUFFER

        if end <= WORK_START or start >= WORK_END:
            continue

        busy_intervals.append((start, end))

    slots = []
    t = WORK_START

    while t + meeting_duration <= WORK_END:
        meeting_end = t + meeting_duration

        # No starts during lunch
        if LUNCH_START <= t < LUNCH_END:
            t += 15
            continue

        # Check overlap with buffered events
        for busy_start, busy_end in busy_intervals:
            if not (meeting_end <= busy_start or t >= busy_end):
                break
        else:
            slots.append(to_time_str(t))

        t += 15

    return slots


    
    """ FIRST IMPLEMENTATION
    def to_minutes(t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    def to_time_str(minutes: int) -> str:
        return f"{minutes // 60:02d}:{minutes % 60:02d}"

    # Working hours and lunch break (in minutes)
    WORK_START = 9 * 60       # 09:00
    WORK_END = 17 * 60        # 17:00
    LUNCH_START = 12 * 60     # 12:00
    LUNCH_END = 13 * 60       # 13:00

    # Normalize and filter events to working hours
    busy_intervals = []
    for event in events:
        start = to_minutes(event["start"])
        end = to_minutes(event["end"])

        # Ignore events completely outside working hours
        if end <= WORK_START or start >= WORK_END:
            continue

        busy_intervals.append((start, end))

    slots = []

    # Generate candidate start times in 15-minute increments
    t = WORK_START
    while t + meeting_duration <= WORK_END:
        meeting_end = t + meeting_duration

        # Block lunch start times
        if LUNCH_START <= t < LUNCH_END:
            t += 15
            continue

        # Check overlap with any event
        overlaps = False
        for busy_start, busy_end in busy_intervals:
            if not (meeting_end <= busy_start or t >= busy_end):
                overlaps = True
                break

        if not overlaps:
            slots.append(to_time_str(t))

        t += 15

    return slots"""