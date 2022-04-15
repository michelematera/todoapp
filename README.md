# Todo App

## Install global Dependencies (only _macOS_)
`$ pipenv install`

### Install Brew (https://brew.sh):
`$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

### Install pyenv:
`$ brew install pyenv`

### Install pyenv in Todo App root directory:
Run and Manage differents version of Python, refer to .python-version
`$ pyenv install`

### Install pipenv:
`$ brew install pipenv`
`$ pipenv install`

### Execute pipenv shell
Execute `pipenv shell` command on todo repository entering, put in .bash_profile this:

```bash
# Python
export PYENV_ROOT="$HOME/.pyenv"
export PIPENV_DONT_LOAD_ENV="1"
export PATH="$PYENV_ROOT/bin:$PATH"
function cd {
  builtin cd "$@"
  if [ ! -n "${PIPENV_ACTIVE+1}" ] && [ -f "Pipfile" ] ; then
    pipenv shell
  fi
}
eval "$(pyenv init -)"
```

If your prompt is not getting to you right information of current directory, put in .bash_profile this:

```bash
# Prompt
export PS1='[\u@\h \W]\$ '
```

### Start Docker Services
`$ docker-compose up -d --build --remove-orphans`
