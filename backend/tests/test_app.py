import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from backend.app import analyze_tone, summarize_tone


def test_analyze_tone_returns_placeholder():
    url = "https://example.com/song"
    result = analyze_tone(url)
    assert result["song_url"] == url
    assert result["tone"] == "placeholder"


def test_summarize_tone_formats_output():
    profile = {"song_url": "https://example.com/song", "tone": "warm"}
    summary = summarize_tone(profile)
    assert summary == "Tone profile for https://example.com/song: warm"
