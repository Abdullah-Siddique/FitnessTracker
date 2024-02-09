# test_project.py
import pytest
from project import *

# Test cases for track_workouts function
def test_track_workouts():
    # Test case 1: Valid input
    track_workouts("Running", 30, "High")
    assert len(workouts_data) == 1

    # Test case 2: Invalid input
    track_workouts("Yoga", 60, "Low")
    assert len(workouts_data) == 2

# Test cases for log_meals function
def test_log_meals():
    # Test case 1: Valid input
    log_meals("Salad", 1, "Low calories")
    assert len(meals_data) == 1

    # Test case 2: Invalid input
    log_meals("Pizza", 3, "High calories")
    assert len(meals_data) == 2

# Test cases for monitor_water_intake function
def test_monitor_water_intake():
    # Test case 1: Valid input
    monitor_water_intake(500)
    assert len(water_intake_data) == 1

    # Test case 2: Invalid input
    monitor_water_intake(1000)
    assert len(water_intake_data) == 2

# Test cases for track_sleep_patterns function
def test_track_sleep_patterns():
    # Test case 1: Valid input
    track_sleep_patterns(7.5, 8)
    assert len(sleep_data) == 1

    # Test case 2: Invalid input
    track_sleep_patterns(6, 6)
    assert len(sleep_data) == 2

# Test cases for generate_dashboard function
def test_generate_dashboard():
    # Test case 1: No data
    generate_dashboard()

    # Test case 2: With data
    track_workouts("Running", 30, "High")
    log_meals("Salad", 1, "Low calories")
    monitor_water_intake(500)
    track_sleep_patterns(7.5, 8)
    generate_dashboard()

# Test cases for set_goals function
def test_set_goals():
    # Test cases for set_goals function
    pass

# Test cases for send_reminders function
def test_send_reminders():
    # Test cases for send_reminders function
    pass

