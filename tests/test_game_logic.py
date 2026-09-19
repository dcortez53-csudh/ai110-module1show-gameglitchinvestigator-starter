from logic_utils import (
    check_guess,
    parse_guess,
    update_score,
    get_range_for_difficulty,
)


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_parse_guess_handles_empty():
    ok, value, err = parse_guess("")
    assert not ok
    assert value is None
    assert err is not None


def test_parse_guess_handles_non_number():
    ok, value, err = parse_guess("abc")
    assert not ok
    assert value is None


def test_parse_guess_accepts_int():
    ok, value, err = parse_guess("42")
    assert ok
    assert value == 42
    assert err is None


def test_range_for_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_range_for_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_update_score_win_decreases_with_attempts():
    first_win = update_score(0, "Win", 1)
    later_win = update_score(0, "Win", 5)
    assert first_win > later_win


def test_update_score_too_low_loses_points():
    assert update_score(50, "Too Low", 1) == 45

def test_parse_guess_handles_decimal():
    # Decimal input like "42.7" should truncate to 42, not crash.
    ok, value, err = parse_guess("42.7")
    assert ok
    assert value == 42


def test_parse_guess_handles_negative():
    # Negative numbers parse as valid ints (below the game range).
    ok, value, err = parse_guess("-5")
    assert ok
    assert value == -5


def test_parse_guess_handles_very_large_number():
    # Python handles arbitrary precision, so a huge int should not overflow.
    ok, value, err = parse_guess("99999999999999999999")
    assert ok
    assert value == 99999999999999999999
