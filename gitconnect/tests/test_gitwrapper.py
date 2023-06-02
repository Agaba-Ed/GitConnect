import os
import pytest
from gitconnect.GitWrapper import GitWrapper



@pytest.fixture
def git_wrapper():
    access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
    return GitWrapper(access_token)


def test_get_user(git_wrapper):
    username = 'octocat'
    user_data = git_wrapper.get_user(username)
    assert user_data['login'] == username


def test_get_repo(git_wrapper):
    owner = 'octocat'
    repo_name = 'Hello-World'
    repo_data = git_wrapper.get_repo(owner, repo_name)
    assert repo_data['name'] == repo_name


def test_search_repos(git_wrapper):
    query = 'python'
    results = git_wrapper.search_repos(query)
    assert len(results) > 0


def test_search_user_repos(git_wrapper):
    username = 'octocat'
    query = 'language:py'
    results = git_wrapper.search_user_repos(username, query)
    assert len(results) > 0


def test_get_commits(git_wrapper):
    owner = 'pytest-dev'
    repo_name = 'pytest'
    branch = 'main'
    commits = git_wrapper.get_commits(owner, repo_name, branch)
    assert len(commits) > 0


def test_get_commit_files(git_wrapper):
    owner = 'pytest-dev'
    repo_name = 'pytest'
    sha = '07eeeb8dfc82de289565a57880ca08b0eac4462d'
    files = git_wrapper.get_commit_files(owner, repo_name, sha)
    assert len(files) > 0


def test_get_commit_file_content(git_wrapper):
    owner = 'pytest-dev'
    repo_name = 'pytest'
    sha = '07eeeb8dfc82de289565a57880ca08b0eac4462d'
    file_path = 'blob/main/setup.py'
    content = git_wrapper.get_commit_file_content(owner, repo_name, sha, file_path)
    assert content.startswith('"""pytest plugins.') 


def test_get_source_files(git_wrapper):
    owner = 'pytest-dev'
    repo_name = 'pytest'
    file_extensions = ['.py']
    source_files = git_wrapper.get_source_files(owner, repo_name, file_extensions)
    assert len(source_files) > 0
