Getting Started
---------

Given the following project (directory):

```
├── myfoo
│   ├── webapp
│   ├── webservice
│   └── datatools
```

We have the myfoo/webapp and myfoo/webservice directories.

Say we want to run an operation (create a git tag) on just the web* directories.

## Register & Tag

```
cd myfoo/webapp && pymr-register -t web
cd myfoo/webservice && pymr-register -t web
```

This will create a file ".pymr" in both directories that contains the tag "web".

## Execute a Command

```
pymr-run -t web "git tag newversion"
```

This command will:

1. Recurse through all directories searching for a ".pyrmr" file.
2. Read that file and match the given tag.
3. The given command will be executed on each directory.
