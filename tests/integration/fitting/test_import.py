import pytest


@pytest.mark.fast
def test_import_easypeasy():
    import easypeasy

    assert easypeasy is not None
