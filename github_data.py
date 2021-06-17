from github import Github

TOKEN = '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'

g = Github(TOKEN)

def get_repo_data():
    for repo in g.get_user().get_repos():
        if not(repo.private):
            return repo
            #print(repo.full_name)
            #print("   " + repo.description)
            #print(repo.url)
