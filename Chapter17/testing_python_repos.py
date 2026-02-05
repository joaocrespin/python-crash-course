import pytest
from python_repos import get_repos, get_response_dict, get_items

@pytest.fixture
def response():
    r = get_repos()
    return r

def test_status_code(response):
    assert response.status_code == 200

def test_response_dict(response):
    response_dict = get_response_dict(response)

    total_dicts = response_dict['total_count']

    assert total_dicts > 240

def test_dicts(response):
    response_dict = get_response_dict(response)
    repo_dicts = get_items(response_dict)

    assert len(repo_dicts) == 30

    for repo_dict in repo_dicts:
        assert repo_dict['stargazers_count'] > 10_000