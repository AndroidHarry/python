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

https://cloud.tencent.com/developer/article/1354396

默认情况下，logging将日志打印到屏幕，日志级别为 WARNING 。

logger.setLevel(logging.NOTSET)     # harry, logging.NOTSET 经测试，调不调用效果一样，似乎不会被执行。

Python 标准库 logging 用作记录日志，默认分为六种日志级别（括号为级别对应的数值），NOTSET（0）、DEBUG（10）、INFO（20）、WARNING（30）、ERROR（40）、CRITICAL（50）。
我们自定义日志级别时注意不要和默认的日志级别数值相同，logging 执行时输出大于等于设置的日志级别的日志信息，
如设置日志级别是 INFO，则 INFO、WARNING、ERROR、CRITICAL 级别的日志都会输出。
