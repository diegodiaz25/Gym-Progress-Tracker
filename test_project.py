import project
from datetime import datetime

def test_add_gym_log():
    logs = []
    logs = project.add_gym_log(logs, "Bench Press", 60, 3, 10, 50.0, 75.0)
    assert len(logs) == 1
    entry = logs[0]
    assert entry["exercise"] == "Bench Press"
    assert entry["time_spent"] == 60
    assert entry["sets"] == 3
    assert entry["reps"] == 10
    assert entry["weight_lifted"] == 50.0
    assert entry["body_weight"] == 75.0
    try:
        datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        assert False, "Timestamp format is incorrect."
    assert entry["volume"] == 3 * 10 * 50.0

def test_calculate_total_volume():
    logs = [
        {"exercise": "Squats", "time_spent": 45, "sets": 3, "reps": 10, "weight_lifted": 60.0, "body_weight": 72.0, "timestamp": "2023-01-01 10:00:00", "volume": 1800.0},
        {"exercise": "Deadlift", "time_spent": 50, "sets": 2, "reps": 8, "weight_lifted": 80.0, "body_weight": 72.0, "timestamp": "2023-01-02 11:00:00", "volume": 1280.0}
    ]
    total = project.calculate_total_volume(logs)
    assert total == 1800.0 + 1280.0

def test_get_progress_summary():
    logs = [
        {"exercise": "Arms", "time_spent": 30, "sets": 3, "reps": 10, "weight_lifted": 40.0, "body_weight": 70.0, "timestamp": "2023-01-01 10:00:00", "volume": 1200.0}
    ]
    summary = project.get_progress_summary(logs)
    assert "1" in summary
    assert "1200.0" in summary
    assert "70.0" in summary