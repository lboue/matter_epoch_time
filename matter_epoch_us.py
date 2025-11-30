from datetime import datetime, timezone

matter_epoch_us = int(
    (
        datetime(2025, 1, 1, tzinfo=timezone.utc)
        - datetime(2000, 1, 1, tzinfo=timezone.utc)
    ).total_seconds()
    * 1_000_000
)
print(matter_epoch_us)  # 789004800000000


def matter_2000_to_unix_epoch(matter_2000_epoch: int) -> int:
    """Convert Matter 2000 epoch to Unix epoch.

    Args:
        matter_2000_epoch (int): Time in Matter 2000 epoch (seconds since 2000-01-01 00:00:00 UTC).

    Returns:
        int: Time in Unix epoch (seconds since 1970-01-01 00:00:00 UTC).
    """
    MATTER_2000_TO_UNIX_EPOCH_OFFSET = 946684800
    return matter_2000_epoch + MATTER_2000_TO_UNIX_EPOCH_OFFSET


# Example usage
matter_2000_time = 789004800  # Example Matter 2000 epoch time
unix_time = matter_2000_to_unix_epoch(matter_2000_time)
print(unix_time)  # 1735689600
# Convert back to verify
converted_back = unix_time - 946684800
print(converted_back)  # 789004800
# Verify the conversion
assert converted_back == matter_2000_time
print("Conversion verified successfully.")
print("-" * 60)
# Additional verification with current time
current_unix_time = int(datetime.now(tz=timezone.utc).timestamp())

current_matter_2000_time = current_unix_time - 946684800
converted_unix_time = matter_2000_to_unix_epoch(current_matter_2000_time)
print("Current Unix time:", current_unix_time)
print("Current Matter 2000 time:", current_matter_2000_time)
print("Converted back Unix time:", converted_unix_time)
assert converted_unix_time == current_unix_time
print("Current time conversion verified successfully.")
print("-" * 60)
# Test with a specific date
test_date = datetime(2023, 6, 1, 12, 0, 0, tzinfo=timezone.utc)
test_unix_epoch = int(test_date.timestamp())
test_matter_2000_epoch = test_unix_epoch - 946684800
converted_test_unix_epoch = matter_2000_to_unix_epoch(test_matter_2000_epoch)
print("Test date (UTC):", test_date)
print("Test Unix epoch time:", test_unix_epoch)
print("Test Matter 2000 epoch time:", test_matter_2000_epoch)
print("Converted back Unix epoch time:", converted_test_unix_epoch)
assert converted_test_unix_epoch == test_unix_epoch
