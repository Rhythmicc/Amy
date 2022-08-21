import requests
from QuickProject.Commander import Commander
from QuickProject import QproDefaultConsole, QproInfoString
from QuickStart_Rhy import headers
from . import *

app = Commander()


@app.command()
def update():
    with QproDefaultConsole.status('正在获取订阅信息') as st:
        r = requests.get(url, headers=headers)
        st.update('创建临时文件')
        with open('temp.conf', 'w') as f:
            f.write(r.content.decode('utf-8').strip())
        st.update('获取订阅信息')
        with open('temp.conf', 'r') as f:
            lines = f.readlines()
    
    lines = [line.strip() for line in lines]
    proxy_list = []
    index = lines.index('[Proxy]') + 1
    while not lines[index].startswith('['):
        if lines[index].startswith('Bandwidth') or lines[index].startswith('Expire Date'):
            index += 1
            continue
        proxy_list.append(lines[index].strip())
        index += 1

    with open(f'temp.conf', 'w') as f:
        infos = {
            'proxies': '\n'.join(proxy_list),
            'proxies_one_line': ','.join([i.split('=')[0].strip() for i in proxy_list if i]),
            'proxies_one_line_jp': ','.join([i.split('=')[0].strip() for i in proxy_list if '日本' in i]),
            'proxies_one_line_us': ','.join([i.split('=')[0].strip() for i in proxy_list if '美国' in i])
        }
        f.write(conf_template.format(**infos))
    
    with QproDefaultConsole.status('正在上传'):
        from QuickStart_Rhy.API.TencentCloud import TxCOS
        TxCOS().upload(f'temp.conf', key=key)
    from QuickStart_Rhy import remove
    remove('temp.conf')

    QproDefaultConsole.print(QproInfoString, f'订阅更新成功, 链接: {txcos_domain}/{key}')


def main():
    """
    注册为全局命令时, 默认采用main函数作为命令入口, 请勿将此函数用作它途.
    When registering as a global command, default to main function as the command entry, do not use it as another way.
    """
    app()


if __name__ == '__main__':
    main()
