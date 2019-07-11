https://docs.python.org/zh-cn/3/howto/logging-cookbook.html#logging-cookbook

在多个模块中使用日志
多次调用``logging.getLogger('someLogger')``时会返回对同一个logger对象的引用。 这不仅是在同一个模块中，在其他模块调用也是如此，只要是在同一个Python解释器进程中。 
是应该引用同一个对象，此外，应用程序也可以在一个模块中定义和配置父logger，而在单独的模块中创建（但不配置）子logger，对子logger的所有调用都将传给父logger。
参见 spam_application 和 spam_application.auxiliary 。

日志记录器是普通的Python对象。addHandler() 方法没有限制可以添加的日志处理器数量。
有时候，应用程序需要将严重类的消息记录在一个文本文件，而将错误类或其他等级的消息输出在控制台中。
要进行这样的设定，只需多配置几个日志处理器即可，在应用程序代码中的日志记录调用可以保持不变。
---
在编写和测试应用程序时，创建能过滤不同等级消息的日志处理器是很有用的。
不要去使用 print 去调试，而是使用 logger.debug: 它不像打印语句需要在调试结束后注释或删除掉，你可以把它们保留在源码中并不输出。
当需要再次调试时，只需要改变日志记录器或处理器的过滤等级即可。

如果你想在网络上发送日志，并在接收端处理它们。一个简单的方式是通过附加一个 SocketHandler 的实例在发送端的根日志处理器中
参见 logsocketsend.py 和 logsocketrecv.py 。

一个传递上下文信息和日志事件信息的简单办法是使用类 LoggerAdapter。 
这个类设计的像 Logger，所以可以直接调用 debug()、info()、 warning()、 error()、exception()、 critical() 和 log()。 
这些方法在对应的 Logger 中使用相同的签名，所以可以交替使用两种类型的实例。

使用过滤器传递上下文信息
你也可以使用一个用户定义的类 Filter 在日志输出中添加上下文信息。
Filter 的实例是被允许修改传入的 LogRecords，包括添加其他的属性，然后可以使用合适的格式化字符串输出，或者可以使用一个自定义的类 Formatter。


https://cloud.tencent.com/developer/article/1354396

一个系统只有一个 Logger 对象，并且该对象不能被直接实例化，没错，这里用到了单例模式，获取 Logger 对象的方法为 getLogger。

注意：这里的单例模式并不是说只有一个 Logger 对象，而是指整个系统只有一个根 Logger 对象，
Logger 对象在执行 info()、error() 等方法时实际上调用都是根 Logger 对象对应的 info()、error() 等方法。

我们可以创造多个 Logger 对象，但是真正输出日志的是根 Logger 对象。
每个 Logger 对象都可以设置一个名字，如果设置logger = logging.getLogger(__name__)，__name__ 是 Python 中的一个特殊内置变量，
他代表当前模块的名称（默认为 __main__）。
则 Logger 对象的 name 为建议使用以点号作为分隔符的命名空间等级制度。

默认情况下，logging将日志打印到屏幕，日志级别为 WARNING 。

logger.setLevel(logging.NOTSET)     # harry, logging.NOTSET 经测试，调不调用效果一样，似乎不会被执行。

Python 标准库 logging 用作记录日志，默认分为六种日志级别（括号为级别对应的数值），NOTSET（0）、DEBUG（10）、INFO（20）、WARNING（30）、ERROR（40）、CRITICAL（50）。
我们自定义日志级别时注意不要和默认的日志级别数值相同，logging 执行时输出大于等于设置的日志级别的日志信息，
如设置日志级别是 INFO，则 INFO、WARNING、ERROR、CRITICAL 级别的日志都会输出。

看到这几种 Python 类型，Logger、LogRecord、Filter、Handler、Formatter。
类型说明：
Logger：日志，暴露函数给应用程序，基于日志记录器和过滤器级别决定哪些日志有效。
LogRecord ：日志记录器，将日志传到相应的处理器处理。
Handler ：处理器, 将(日志记录器产生的)日志记录发送至合适的目的地。
Filter ：过滤器, 提供了更好的粒度控制,它可以决定输出哪些日志记录。
Formatter：格式化器, 指明了最终输出中日志记录的布局。



Formatter 对象用来设置具体的输出格式，常用变量格式如下表所示，所有参数见 Python(3.7)官方文档：
---------------------------------------------
变量		格式			变量描述
asctime		%(asctime)s		将日志的时间构造成可读的形式，默认情况下是精确到毫秒，如 2018-10-13 23:24:57,832，可以额外指定 datefmt 参数来指定该变量的格式
name		%(name)			日志对象的名称
filename	%(filename)s	不包含路径的文件名
pathname	%(pathname)s	包含路径的文件名
funcName	%(funcName)s	日志记录所在的函数名
levelname	%(levelname)s	日志的级别名称
message		%(message)s		具体的日志信息
lineno		%(lineno)d		日志记录所在的行号
pathname	%(pathname)s	完整路径
process		%(process)d		当前进程ID
processName	%(processName)s	当前进程名称
thread		%(thread)d		当前线程ID
threadName	%threadName)s	当前线程名称
---------------------------------------------
---------------------------------------------

