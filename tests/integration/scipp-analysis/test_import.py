def test_import_easydiffraction():
    import easydiffraction

    assert easydiffraction is not None


def test_dummy_function():
    from easydiffraction.dummy import dummy_function

    result = dummy_function()

    assert result == 'Hello from easydiffraction'
    assert isinstance(result, str)
