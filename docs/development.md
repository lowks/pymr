Developer Setup
==========

Please fork the repository and submit pull requests. Any pull requests without passing tests will be rejected.

[Forking](https://help.github.com/articles/fork-a-repo/)

[Pull-Requests](https://help.github.com/articles/using-pull-requests/)

Bootstrapping PyMR
---------

### Clone the repository & cd into it
```
git clone https://github.com/kpurdon/pymr.git
```
### Install [fabric](http://www.fabfile.org/en/latest/)
```
pip install fabric
```
### Run the bootstrap
```
fab bootstrap
```
### Run the tests
```
fab test
```
### Install in develop mode
```
python setup.py develop
```
