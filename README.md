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

## 3. Menu

### [L1 ~ L10](./L0001~L0010.ipynb)

1. 两数之和 **简单**
2. 两数相加 **中等**
3. 无重复字符的最长子串 **中等**
4. 寻找两个正序数组的中位数 **困难**
5. 最长回文子串 **中等**
6. Z 字形变换 **中等**
7. 整数反转 **简单**
8. 字符串转换整数 (atoi) **中等**
9. 回文数 **简单**
10. 正则表达式匹配 **困难**

### [L11 ~ L20](./L0011~L0020.ipynb)

11. 盛最多水的容器（双指针法） **中等**
12. 整数转罗马数字 **中等**
13. 罗马数字转整数 **简单**
14. 最长公共前缀 **简单**
15. 三数之和 **中等**
16. 最接近的三数之和 **中等**
17. 电话号码的字母组合（回溯法） **中等**

### [L51 ~ L60](./L0051~L0060.ipynb)

59. 螺旋矩阵 II **中等**

### [L91 ~ L100](./L0091~L0100.ipynb)

92. 反转链表 II **中等**

### [L221 ~ L230](./L0221~L0230.ipynb)

224. 基本计算器 **困难**
227. 基本计算器 II **中等**

### [L301 ~ L310](./L0301~L0310.ipynb)

303. 区域和检索 - 数组不可变 **简单**

### [L331 ~ L340](./L0331~L0340.ipynb)

331. 验证二叉树的前序序列化 **中等**

### [L341 ~ L350](./L0341~L0350.ipynb)

341. 扁平化嵌套列表迭代器 **中等**

### [L391 ~ L400](./L0391~L0400.ipynb)

395. 至少有 K 个重复字符的最长子串 **中等**

### [L861 ~ L870](./L0861~L0870.ipynb)

867. 转置矩阵 **简单**

### [L891 ~ L900](./L0891~L0900.ipynb)

896. 单调数列 **简单**

### [L1171 ~ L1180](./L1171~L1180.ipynb)

1178. 猜字谜 **困难**