import requests

def get_repos():
    '''Call the api for python repositories with +10000 stars.'''
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    return r

def get_response_dict(response):
    '''Return a JSON file based on the api response.'''
    return response.json()

def show_info(response):
    '''Show if the api brought every result and display the amount.'''
    print(f"Total repositories: {response['total_count']}")
    print(f"Complete results: {not response['incomplete_results']}")

def get_items(response):
    '''Return the repositories data.'''
    return response['items']

def show_info_repos(repo_dicts):
    '''Show details about each repository.'''
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")