# Amy

一个帮助你在本地格式化Amy Surge订阅的命令工具。

## 安装

1. 克隆此项目
    ```sh
    pip3 install Qpro -U
    # clone this project
    git clone <your url> amy
    cd amy
    ```
2. 打开`__init__.py`，在相应位置填写你的订阅链接(注意是Surge的)、你的腾讯云对象存储域名以及你希望保存的路径
3. 注册此项目为全局命令
    ```sh
    # 注册此项目为全局命令
    Qpro register-global
    ```

## 使用

获取帮助: `amy --help`

### 子命令

| 命令  | 样例                           | 描述        |
| -------- | ------------------------------ | ------------------ |
| update | `amy update [--name <名称>]` | 更新并上传你的订阅信息到腾讯云对象存储\[设置文件名] |

### 调用注册的子命令 (开发者选项)

```python
app.real_call('<function name>', *args, **kwargs)
```

## 如何注册全局命令

1. 设置环境变量 `QproGlobalDir`, 比如 `$HOME/.local/QproGlobalDir`
2. 注册此项目为全局命令: `Qpro register-global`
3. 生成Fig补全插件: `Qpro gen-fig-script`
4. 生成zsh补全插件: `Qpro gen-zsh-comp`
