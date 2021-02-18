# Funny work on leetcode.com

## 1. Setup

### 1.1 Install pyenv

- On macOS

```bash
$ brew install pyenv
$ brew install pyenv-virtualenv
```

- On Linux

````bash
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
````

### 1.2 Setup pyenv

- On macOS, edit `~/.bash_profile` file or `~/.zshrc` file;
- On Linux, edit `~.bashrc` file;
- Add the following content:

  ```bash
  export PATH="~/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  ```

### 1.3 Install python

- Check if `python 3.7.4` installed;

  ```bash
  $ pyenv versions
  ```

- Install `python 3.7.4`

  ```bash
  $ pyenv install 3.7.4
  ```

  > 注意：如果因下载过慢而无法安装成功，可通过提示的下载路径，通过其它下载工具下载安装压缩包，放入`~/.pyenv/cache`目录下，例如：`~/.pyenv/cache/Python-3.7.4.tar.xz`

- 使用`python 3.7.4`

  ```bash
  $ pyenv local 3.7.4
  ```

### 1.4 Create and active virtualenv

```bash
$ python -m venv .venv --prompt='study-python'
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

### 1.5 Enable "Jupyterlab Code Formatter" extension

```bash
$ jupyter labextension install @ryantam626/jupyterlab_code_formatter
$ jupyter serverextension enable --py jupyterlab_code_formatter
```

> [Jupyterlab Code Formatter Homepage](https://jupyterlab-code-formatter.readthedocs.io/)

### 1.6 Start "jupyterlab" and setup

- Start "jupyterlab server"

  ```bash
  $ jupyter lab
  ```

  After command run successful, then the url with token should be printed, open the url with browser

- Click menu `Settings`>`Advanced Settings Editor`>`Jupyterlab Code Formatter`，add content：

  ```json
  {
      "autopep8": {
          "max_line_length": 120,
          "ignore": [
              "E226",
              "E302",
              "E41"
          ]
      },
      "preferences": {
          "default_formatter": {
              "python": "autopep8",
              "r": "formatR"
          }
      }
  }
  ```

- Click menu `Settings`>`Advanced Settings Editor`>`Keyboard Shortcuts`，add content：

  ```bash
  {
      "shortcuts": [
          {
              "command": "jupyterlab_code_formatter:autopep8",
              "keys": [
                  "Ctrl K",
                  "Ctrl M"
              ],
              "selector": ".jp-Notebook.jp-mod-editMode"
          }
      ]
  }
  ```

## 2. Something else

### 2.1 About "virtualenv" and "virtualenvwrapper"

- Install

  ```bash
  $ pip install virtualenv
  $ pip install virtualenvwrapper
  ```

  Or on linux

  ```bash
  $ sudo apt install virtualenv
  $ sudo apt install virtualenvwrapper
  ```

- Edit "shell profile" file (`~/.bash_profile` or `~/.bashrc`), add content:

  ```bash
  export WORKON_HOME=~/.venv
  VIRTUALENVWRAPPER_PYTHON='/usr/local/bin/python3'
  source /usr/local/bin/virtualenvwrapper.sh
  ```

  Or lazy load

  ```bash
  export WORKON_HOME=~/.venv
  VIRTUALENVWRAPPER_PYTHON='/usr/local/bin/python3'
  export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
  source /usr/local/bin/virtualenvwrapper_lazy.sh
  ```

- Create environment by `virtualenv` command

  ```bash
  $ virtualenv -p `which python3` --no-site-packages .venv
  $ source .venv/bin/activate
  ```

- Create environment by `virtualenvwrapper` command

  ```bash
  $ mkvirtualenv --python=python3 study
  $ workon study
  ```

- Leave environment

  ```bash
  $ deactivate
  ```
