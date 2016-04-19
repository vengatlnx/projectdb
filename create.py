"""Script create project in github repository

Usage:
    create.py (-o <owner>) (-p <project>)

Options:
    -h --help               show help
    -o --owner OWNER        project owner
    -p --project PROJECT    name of the project
"""

import requests
import json
import yaml
from docopt import docopt
import os

URL = "https://api.github.com"
token = os.getenv('GH_TOKEN', None)

class ProjectBuilder:
    def __init__(self, proj, owner):
        self.session = requests.Session()
        self.proj = proj
        self.owner = owner

    def _get_repos(self):
        url = URL + "/users/"+ self.owner +"/repos"
        repos = json.loads(self.session.get(url).text)
        repo_list = []
        for repo in repos:
            repo_list.append(repo["full_name"].encode("utf-8"))

        return repo_list

    def _check_repo_exist(self):
        if (self.proj not in self._get_repos()):
            return True
        
    def create_repo(self):
        if (self._check_repo_exist()):
            try:
                with open(self.proj, "r") as data_file:
                    data = yaml.safe_load(data_file)
                    url = URL + "/user/repos"
                    res = self.session.post(url, data=json.dumps(data), headers={'Authorization':'token %s' % token})
                    if res.status_code == 201 :
                        print "Repository Created Successfully"
                    else:
                        print "Failed to create repository"
            except IOError:
                 print "Nothing to create"    
        else:
            print "Repository already exist"


def main(proj, owner):
    pb = ProjectBuilder(proj, owner)
    pb.create_repo()
    
if __name__ == "__main__":
    args = docopt(__doc__)
    main(proj=args['--project'], owner=args['--owner'])
