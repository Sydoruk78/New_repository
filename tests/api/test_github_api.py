import pytest
from  modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 50
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiirepo_not_exists')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('d')
    assert r['total_count'] != 0


@pytest.mark.api
def test_org_can_be_found(github_api):
    r = github_api.get_organisation('errfree')
    assert r['login'] == 'errfree'


@pytest.mark.api
def test_org_cannot_be_found(github_api):
    r = github_api.get_organisation('kostyantyn')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_count_of_followers(github_api):
    r = github_api.get_organisation('errfree')
    assert r['followers'] == 3


@pytest.mark.api
def test_type_of_org(github_api):
    r = github_api.get_organisation('errfree')
    assert r['type'] == 'Organization'


