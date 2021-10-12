import pytest
from fastapi.testclient import TestClient
from app.main import create_app


@pytest.fixture(scope='module')
def test_client() -> TestClient:
    app = create_app()
    testing_client = TestClient(app)
    yield testing_client


@pytest.fixture(scope='module')
def post_endpoint() -> str:
    return '/api/v1/hash/calculate-file-hash'


@pytest.fixture(scope='module')
def get_endpoint_prefix() -> str:
    return f'/api/v1/hash/get-result'


@pytest.fixture(scope='module')
def path_prefix() -> str:
    return '/app/tests/files/'

