def test_registry_basic():
    from derex.runner.plugins import Registry

    registry = Registry()
    registry.add("last", "I should be last", "_end")
    registry.add("first", "I should be first", "_begin")
    registry.add(
        "in-between-1", "I should be the first in between first and last", ">first"
    )
    registry.add(
        "in-between-2", "I should be the second in between first and last", "<last"
    )

    assert registry["last"] == "I should be last"
    assert registry[-1] == "I should be last"
    assert registry["first"] == "I should be first"
    assert registry[0] == "I should be first"

    # Now move the last to the beginning, just to prove we can
    registry.add("last", "I should be last", "_begin")
    assert registry[0] == "I should be last"
