# GitConnect

GitConnect is a Python library that provides an interface for interacting with the GitHub API. It allows you to easily search for repositories by user and keyword, get details about a specific repository, and more.

## Installation
To install GitConnect, simply run:
    
        pip install gitconnect

## Usage
First, you'll need a personal access token for the GitHub API. You can create one by following these steps:
1. Go to https://github.com/settings/tokens and click "Generate new token".
2. Give your token a name and select the scopes that it needs.
3. Click "Generate token" and copy the token value.

Next, create a GitWrapper object with your access token: