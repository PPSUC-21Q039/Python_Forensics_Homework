# Python 大作业 检材常用信息搜集 Readme



**仓库地址**：https://github.com/PPSUC-21Q039/Python_Forensics_Homework

**组员**：

1. 21数据警务技术一区队 孟昊阳 202121710017 

2. 21数据警务技术一区队 胡文强 202121710039 huwenqiang.hwq@protonmail.com

**Python 程序设计方向**：检材常用信息搜集

---

## 程序构思：

首先 `import` 通用库 `os` 库，使用 `os.name` 进行平台判断，若为 `nt`，则调用 Windows 自动取证的 Class，如果为 `posix`，则调用 Linux 自动取证的 Class.

```
if __name__ == '__main__':
    OS_TYPE = os.name
    if  OS_TYPE== 'nt':
        Windows_Forensics.start_forensics()
    elif OS_TYPE == 'posix':
	    Linux_Forensics.start_forensics()
	else:
	    ...
```

对于各个平台，所取的信息基本相似，但对 Windows 平台，应尽可能加入更多常用软件的取证，对于 Linux 平台，应加入更多对于配置文件的取证，如：

- 系统类型及具体版本（发行版、内核版本、大版本及内部版号）

- 基本账户信息：
  - 账户名称
  - 账户属性
  - 账户密码
  - 账户登录情况
  - 账户私有文件及配置
  - 
  
- 系统配置信息：
  - 系统磁盘信息
  - 系统安装日期
  - 系统启动 Log
  - 系统服务配置
  - 
  
- 检材文件标注：
  - 常用文件遍历、筛选
  - 常见 Office 文档图片提取（可以复用当时挑战杯写的代码）
  - 
  
- 常用软件取证：
  - ssh 配置、证书和连接列表
  
  - shell 软件配置及记录分析：
    - bash
    - zsh
    - sh 
    - csh
    
  - 运维方面：
    - docker
    - nginx
    - php
    - git
    
  - 加密软件：
    - truecrypt (veracrypt) 提取
    - Bitlocker 提取
    
  - 翻墙软件：
    - shadowsocks (shadowsocksR, clash等) 客户端配置提取
    - 服务端提取
    
  - 应用程序提取：
    - 浏览器：
      - Firefox 系列
      - Chromium 系列
      - IE 取证
      
    - IM：
      - Wechat （文件分析及使用外部程序）账户信息及聊天记录导出
      - QQ 信息提取
      - Telegram 搜寻
      - Skype 分析
      - 
      
    - 文档软件分析：
      - Vim
      - Notepad ++
      - 
      
      
  
###  Windows 平台取证



###  Linux 平台取证

对于 Linux 平台，主要使用以下操作：

- `platform.uname()` 
