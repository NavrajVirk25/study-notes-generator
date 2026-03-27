# test_app.py
# Phase 6 — Pytest test cases for Study Notes Generator
# Tests is_valid_topic() directly and generate_study_notes() with a mocked API.

import pytest
from unittest.mock import patch, MagicMock
from gemini_helper import is_valid_topic, generate_study_notes


# ─────────────────────────────────────────────
# GROUP 1: is_valid_topic() — no mocking needed
# ─────────────────────────────────────────────

def test_valid_topic_normal():
    """A normal topic string should return True."""
    assert is_valid_topic("Decision Trees") is True

def test_valid_topic_single_word():
    """A single valid word should return True."""
    assert is_valid_topic("Regression") is True

def test_valid_topic_with_numbers():
    """Topics with numbers mixed in should still be valid."""
    assert is_valid_topic("Python 3 basics") is True

def test_invalid_topic_empty_string():
    """An empty string should return False."""
    assert is_valid_topic("") is False

def test_invalid_topic_spaces_only():
    """Whitespace-only input should return False."""
    assert is_valid_topic("   ") is False

def test_invalid_topic_one_letter():
    """A single letter should return False (fewer than 2 letters)."""
    assert is_valid_topic("A") is False

def test_invalid_topic_symbols_only():
    """Symbols with no letters should return False."""
    assert is_valid_topic("!!!###") is False

def test_invalid_topic_mostly_symbols():
    """Input where over 50% are non-alphanumeric should return False."""
    assert is_valid_topic("a!!!") is False

def test_invalid_topic_repeated_chars():
    """Repeated character strings like 'aaaaaaa' should return False."""
    assert is_valid_topic("aaaaaaa") is False

def test_valid_topic_long_input():
    """A long but valid topic string should return True."""
    long_topic = "Introduction to machine learning and data mining algorithms"
    assert is_valid_topic(long_topic) is True

def test_valid_topic_with_hyphen():
    """Topics with hyphens are common and should be valid."""
    assert is_valid_topic("K-Means Clustering") is True


# ──────────────────────────────────────────────────────────────────
# GROUP 2: generate_study_notes() — mocked Gemini API (no key needed)
# ──────────────────────────────────────────────────────────────────

def test_generate_study_notes_returns_string():
    """generate_study_notes() should return a string when API succeeds."""
    mock_response = MagicMock()
    mock_response.text = "## Overview\nThis is a test.\n## Key Concepts\n- Concept A"

    with patch("gemini_helper.get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = mock_response
        mock_get_client.return_value = mock_client

        result = generate_study_notes("Decision Trees")

    assert isinstance(result, str)
    assert len(result) > 0

def test_generate_study_notes_returns_expected_content():
    """generate_study_notes() should return exactly what the API gives back."""
    expected = "## Overview\nDecision trees split data recursively."

    mock_response = MagicMock()
    mock_response.text = expected

    with patch("gemini_helper.get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = mock_response
        mock_get_client.return_value = mock_client

        result = generate_study_notes("Decision Trees")

    assert result == expected

def test_generate_study_notes_calls_api_once():
    """generate_study_notes() should call the Gemini API exactly once per call."""
    mock_response = MagicMock()
    mock_response.text = "Some notes"

    with patch("gemini_helper.get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = mock_response
        mock_get_client.return_value = mock_client

        generate_study_notes("Linear Regression")

        mock_client.models.generate_content.assert_called_once()