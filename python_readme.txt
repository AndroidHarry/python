
========================================================================================
教程

https://docs.python.org/3.8/tutorial/index.html
https://docs.python.org/3/tutorial/

Python 入门指南
https://www.runoob.com/manual/pythontutorial3/docs/html/

Python yield 使用浅析
https://www.runoob.com/w3cnote/python-yield-used-analysis.html

========================================================================================

G:\Harry\python\exercises


========================================================================================
pip
python -m pip install --upgrade pip

pip list


========================================================================================

Django之session详解
https://www.cnblogs.com/daviddd/p/12053482.html


django中的request对象详解
https://www.cnblogs.com/shangping/p/11602885.html


调试时按 F5 不起作用, 在 .vscode 目录下建个 settings.json 文件, 加入语句 
"python.pythonPath": "F:\\Python36\\python.exe"
就可以了。


========================================================================================
虚拟环境 (venv)

https://docs.python.org/zh-cn/3/library/venv.html
通过执行 venv 指令来创建一个 虚拟环境:
python3 -m venv /path/to/new/virtual/environment

Create and activate the virtual environment
py -3 -m venv .venv
.venv\scripts\activate
Once you are finished, type 'deactivate' in the terminal window to deactivate the virtual environment.

========================================================================================

python autocomplete
https://blog.csdn.net/weixin_40922744/article/details/103216982
1. 下载 Visual Studio IntelliCode 插件
2. 安装 微软Python语言服务
harry 实测对直接可推导的类型有效，对间接类型无效
User/settings.json 改为如下
    "python.linting.enabled": true,
    //"python.jediEnabled": true,
    "python.languageServer": "Jedi"
有效
Jedi 比 微软的 Pylance 好用
以上都不如 kite 好用


========================================================================================

VSCode调试Python时终端输出中文乱码解决方法

打开launch.json

在 configurations [{}] 中增加如下代码 

"env":{
    "PYTHONIOENCODING":"gbk"
}



