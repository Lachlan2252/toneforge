from backend.app import analyze_tone


def test_analyze_tone_returns_placeholder():
    url = "https://example.com/song"
    result = analyze_tone(url)
    assert result["song_url"] == url
    assert result["tone"] == "placeholder"
