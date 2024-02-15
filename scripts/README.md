In this folder we have two scripts and one declaration script.

```tree
├── README.md
├── build.sh
├── projects.sh
└── test.sh
```


## Requirements

These scripts use bash v4+ element like dictionary.
So please if you are using Mac, you will need to install bash with homebrew.

And follow these steps:

```bash
$ bash --version
> 3.5*

$ brew install bash

# check location 
$ brew ls bash
> /opt/homebrew/Cellar/bash/5.2.26/bin/bash

$ sudo vim /etc/shells

add -> /opt/homebrew/bin/bash

# check new bash version
$  bash --version
> GNU bash, version 5.2.26(1)
```

You will need to declare in [projects.sh](./projects.sh) the dictionary of project name and project path?
For instance `"taggenerator"` is the project name and its path is `"core/taggenerator"` it will be declared as `["taggenerator"]="core/taggenerator"`.