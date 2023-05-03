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
    query = 'python'
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
    sha = '225d245a36b33f51f9b4497f8d06438a7f1ef91a'
    files = git_wrapper.get_commit_files(owner, repo_name, sha)
    assert len(files) > 0


def test_get_commit_file_content(git_wrapper):
    owner = 'pytest-dev'
    repo_name = 'pytest'
    sha = '225d245a36b33f51f9b4497f8d06438a7f1ef91a'
    file_path = 'pytest/plugins/__init__.py'
    content = git_wrapper.get_commit_file_content(owner, repo_name, sha, file_path)
    assert content.startswith('"""pytest plugins.') 
