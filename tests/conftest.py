import pytest

from infrad_ext.settings import TestConfig
from infrad_ext.app import create_app

@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)
