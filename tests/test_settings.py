

def test_set_setting(settings):
    settings.set("test", "test")
    assert settings.get("test") == "test"

