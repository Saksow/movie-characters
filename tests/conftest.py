import pytest

from app.app import create_app


@pytest.fixture(scope='function')  # Using scope 'function' to ensure tests are independent
def client():
    app = create_app('app.config.Testing')
    client = app.test_client()
    context = app.app_context()

    context.push()
    yield client
    context.pop()
