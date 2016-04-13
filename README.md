# projectdb
  This project helps to create a new project in github repository.
  It contains create script, token authenticaiton file and project
  directory.

### Projects Directory
    Projects Directory contains description about a project in yml file.

    `name` - **Required** The name of the repository

    `description` - A short description of the repository
    
    `homepage` - A URL with more information about the repository
    
    `private` - Either true to create a private repository, or false to create a public one.
    	      	Creating private repositories requires a paid GitHub account.
		Default: false


    `has_issues` - Either true to enable issues for this repository, false to disable them.
    		   Default: true
		   
    `has_wiki` - Either true to enable the wiki for this repository, false to disable it.
    	       	 Default: true
		 
    `has_downloads` - Either true to enable downloads for this repository, false to disable them.
    		      Default: true
		      
    `team_id` - The id of the team that will be granted access to this repository.
    	      	This is only valid when creating a repository in an organization.
		
    `auto_init` - Pass true to create an initial commit with empty README.
    		  Default: false
		  
    `gitignore_template` - Desired language or platform [https://github.com/github/gitignore](.gitignore template) to apply.
    			   Use the name of the template without the extension.
			   For example, "Haskell".
			   
    `license_template` - Desired [https://github.com/github/choosealicense.com](LICENSE template) to apply. Use the name of the [https://github.com/github/choosealicense.com/tree/gh-pages/_licenses](template) without
    		       	 the extension. For example, "mit" or "mozilla".


### Run

1. At First, run `oauth.py` to generate tokenfile
```
  $ python oauth.py
  
  Github username: vengatlnx
  Github password: yyyy
  Note: oauth
  New token: 79db7857e9d0c6c199dcf5b5c187a50b81a81143
```

2. Create a new yml file with description in projects dir
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

3. Then run python script `create.py` to create repository
```
 $ python create.py -p "HelloWorld.yml" -o "vengatlnx"
```

### Intergrating with Travis-Ci
    **TDB**
    
