# projectdb [![Build Status](https://travis-ci.org/vengatlnx/projectdb.svg?branch=master)](https://travis-ci.org/vengatlnx/projectdb)
  This project helps to create a new project in github repository.
  It contains create script, token authenticaiton file and project
  directory.

### Projects Directory

Projects Directory contains description about a project in yml file.

**name** - **Required** The name of the repository

**description** - A short description of the repository
    
**homepage** - A URL with more information about the repository
    
**private** - Either true to create a private repository, or false to create a public one.
    	      Creating private repositories requires a paid GitHub account.
	      Default: false

**has_issues** - Either true to enable issues for this repository, false to disable them.
    		 Default: true
		   
**has_wiki** - Either true to enable the wiki for this repository, false to disable it.
    	       Default: true
		 
**has_downloads** - Either true to enable downloads for this repository, false to disable them.
    		    Default: true
		      
**team_id** - The id of the team that will be granted access to this repository.
    	      This is only valid when creating a repository in an organization.
		
**auto_init** - Pass true to create an initial commit with empty README.
    		Default: false
		  
**gitignore_template** - Desired language or platform [.gitignore template](https://github.com/github/gitignore) to apply.
    			 Use the name of the template without the extension.
			 For example, "Haskell".
			   
**license_template** - Desired [LICENSE template](https://github.com/github/choosealicense.com) to apply.
                       Use the name of the [template](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses) without the extension.
		       For example, "mit" or "mozilla".


### Intergrating with Travis-Ci

* At First, run `oauth.py` to generate tokenfile
```
  $ python oauth.py
  
  Github username: vengatlnx
  Github password: yyyy
  Note: oauth
  New token: 79db7857e9d0c6c199dcf5b5c187a50b81a81143
```

* Generate and add secure key `GH_TOKEN` in `.travis.yml`
```
  $ travis encrypt 79db7857e9d0c6c199dcf5b5c187a50b81a81143 --add
  
  secure: "aUbqaq9Torej7WYmPWAHw7spE0SaNMENPkk8cPE2dDlZbACoc1LowGi6bhkiIR0+u2eqEQf7/KnmjjlG04ZqI4AY0Gi2L1z6YW4MYd0BltFKdfygCJ1g3Ea9mFso9R4eXePKQjPPXbQNgzm2k4pN6uoh+W/z/qPdm7Dzto6h5Gb7IBBD8s/0O1NXysunUagN6qakXDxOm6uMI14x1hT49O1veMkK16o8+JZBXXzYW9r+6YA+M4BTfnnJiBbNO4YYUE1XyKoLx3Hual3uyQRmqpgGal0y3LmbMoGDyPgO9ZzJI80effie4iq+GvxWNfgIXRj6Kb7QolsmS1PlOzJNYHbmtsC2nPc9+FAdMwzwkDleITEBlCG+Y/CNjG2EcFsefjfqn8JJI/50Lo32ipqxzTWxuZJ7IJoCULxGDfMLg4cp4fpBt8gqZhrSybW3ZJGlUp847fzspWqBiEYPTgNDrlXAmhPVLvj7Lc9lHg="
```

### Run

* Create a new yml file with description in projects dir
```
$ cd projects
$ touch HelloWorld.yml
```

Example (HelloWorld.yml):
```
name : HelloWorld
description : This is your first repository
auto-init : true
gitignore_template : Python
license_template : mit
```

* Then commit and push to create new project repo