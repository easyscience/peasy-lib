import pytest


@pytest.mark.fast
def test_import_easydiffraction():
    import easydiffraction

    assert easydiffraction is not None
