TIL : How to ensure correct logs are emitted using Pytest
--

This is a useful technique to ensure accurate logging messages are generated. This is obviously extremely valuable for long-term maintenance and debugging uses.


```Python

with caplog.at_level("INFO", logger="consumers"):
        do_a_thing()

for rec in caplog.records:
    assert "message consumed" in rec.getMessage()
```