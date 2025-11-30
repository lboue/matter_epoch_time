"""Utilities to convert Matter 2000 epoch timestamps to Unix epoch timestamps and
a small runtime demonstration.

This module provides:
- matter_2000_to_unix_epoch: convert seconds since 2000-01-01 UTC to Unix epoch
  seconds
- a simple runtime demonstration that prints current times and conversion
  results
"""

from datetime import datetime, timezone


# Convert Matter 2000 epoch to Unix epoch
def matter_2000_to_unix_epoch(matter_2000_epoch: int) -> int:
    """Convert a Matter 2000 epoch timestamp to a Unix epoch timestamp.

    Parameters
    ----------
    matter_2000_epoch : int
        Seconds since 2000-01-01 00:00:00 UTC (Matter 2000 epoch).

    Returns
    -------
    int
        Corresponding Unix epoch seconds (since 1970-01-01 00:00:00 UTC).
    """
    return matter_2000_epoch + MATTER_2000_TO_UNIX_EPOCH_OFFSET


###################

# Seconds from Matter 2000 epoch to Unix epoch
MATTER_2000_TO_UNIX_EPOCH_OFFSET = 946684800

# Current time in Matter 2000 epoch
current_matter_2000_epoch = (
    int(datetime.now(tz=timezone.utc).timestamp()) - MATTER_2000_TO_UNIX_EPOCH_OFFSET
)
# Current date and time
print("Current date and time (UTC):", datetime.now(tz=timezone.utc))
print(
    "Current time in Matter 2000 epoch (seconds since 2000-01-01 00:00:00 UTC):",
    current_matter_2000_epoch,
)

# Print separator
print("-" * 60)

# Convert back 817847143 (Matter 2000 epoch) to Unix epoch to verify
converted_unix_epoch = matter_2000_to_unix_epoch(current_matter_2000_epoch)
print(
    "Converted back to Unix epoch (seconds since 1970-01-01 00:00:00 UTC):",
    converted_unix_epoch,
)
print(
    "Converted back to date and time (UTC):",
    datetime.fromtimestamp(converted_unix_epoch, tz=timezone.utc),
)
