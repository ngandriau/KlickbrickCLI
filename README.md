# Introduction
My progress for manning's live project: [Build an Extensible CLI with Python](https://www.manning.com/liveproject/build-an-extensible-cli-with-python)

## todo
- integrate with github actions
- integrate with travis for cli

# work from terminal
open terminal in <REPO-HOME>
```shell
$ source venvpython3.9/bin/activate
$ source $HOME/.poetry/env
```
=≥ Should be all set with right version of python and poetry accessible

# Execution
```shell
$ poetry run hello --name Nicolas
HELLO  Nicolas
(venvpython3.9) 
```

# local initial setup after git clone
set current python to ^3.9 (use `pyenv` for instance)
create a virtual env
`$ python -m venv venv`
Check that pycharm use the `venv` interpreter
![](.README_images/pycharmConfigVenvInterpreter.png)



# publishing to TestPyPI
publishing done with: `$ poetry publish -r testpypi`
use my credential `ngandriau`
[project url on testPYyPI](https://test.pypi.org/project/klickbrickcli/)
