TIL new subtest feature added to pytest
-

[TIL about another TIL](https://til.simonwillison.net/pytest/subtests)

```Python
def test_settings_are_documented(settings_headings, subtests):
    for setting in app.SETTINGS:
        with subtests.test(setting=setting.name):
            assert setting.name in settings_headings
```

It's somewhat interchangeable with parameterized tests, however:
* ["subtests are an alternative to parametrization, useful in situations where the parametrization values are not all known at collection time."](https://docs.pytest.org/en/stable/changelog.html#pytest-9-0-0-2025-11-05)
* less chatty: it's one test rather than reporting each parameterized test individually
