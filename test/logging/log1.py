import logging
import logging.handlers


############################################################################
## test1
'''
# 默认情况下，logging将日志打印到屏幕，日志级别为 WARNING 。
logger = logging.getLogger("logger")
logger.info('It is a custom info msg.')     # no output
logger.warn('It is a custom warning msg.')  # output
'''
############################################################################
## test2
'''
import auxiliary_module

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
auxiliary_module.some_function()
logger.info('done with auxiliary_module.some_function()')
'''
############################################################################
## test3

# 在多个线程中记录日志并不需要特殊处理，以下示例展示了如何在主线程（起始线程）和其他线程中记录:
'''
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from myfunc')
        time.sleep(0.5)

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()

if __name__ == '__main__':
    main()
'''
############################################################################
## test4

## 假设有这样一种情况，你需要将日志按不同的格式和不同的情况存储在控制台和文件中。
## 比如说想把日志等级为DEBUG或更高的消息记录于文件中，而把那些等级为INFO或更高的消息输出在控制台。
## 而且记录在文件中的消息格式需要包含时间戳，打印在控制台的不需要。
## 以下示例展示了如何做到:
'''
# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='myapp.log',  # '/temp/myapp.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')
'''
############################################################################
## test5

#  QueueListener，它被设计用来作为 QueueHandler 的对应。 
#  QueueListener 非常简单：向其传入一个队列和一些处理句柄，它会启动一个内部线程来监听从 QueueHandlers (或任何其他可用的 LogRecords 源) 发送过来的 LogRecords 队列。 
#  LogRecords 会从队列中被移除，并被传递给句柄进行处理。
#  使用一个单独的类 QueueListener 优点是可以使用同一个实例去服务于多个``QueueHandlers``。
#  这样会更节省资源，否则每个处理程序都占用一个线程没有任何益处。

# 在 3.5 版更改: 在Python 3.5之前，QueueListener 总是把从队列中接收的每个消息都传给它初始化的日志处理程序。
# (这是因为它会假设过滤级别总是在队列的另一侧去设置的。) 
# 从Python 3.5开始，可以通过在监听器构造函数中添加一个参数``respect_handler_level=True``改变这种情况。
# 当这样设置时，监听器会比较每条消息的等级和日志处理器中设置的等级，只把需要传递的消息传给对应的日志处理器。

import queue
from logging.handlers import QueueListener
from logging.handlers import QueueHandler

que = queue.Queue(-1)  # no limit on size
queue_handler = QueueHandler(que)
handler = logging.StreamHandler()
fh = logging.FileHandler('que2file.log')
fh.setLevel(logging.DEBUG)
listener = QueueListener(que, handler, fh)
root = logging.getLogger()
root.addHandler(queue_handler)
formatter = logging.Formatter('%(threadName)s: %(message)s')
handler.setFormatter(formatter)
listener.start()
# The log output will display the thread which generated
# the event (the main thread) rather than the internal
# thread which monitors the internal queue. This is what
# you want to happen.
root.warning('Look out!')
listener.stop()
root.warning('Look out2!')

############################################################################


'''
logger = logging.getLogger('log1')
logger.setLevel(logging.NOTSET)

# logger.addHandler(logging.NullHandler())

cmdHandler = logging.StreamHandler()
cmdHandler.setLevel(logging.NOTSET)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

cmdHandler.setFormatter(formatter)

logger.addHandler(cmdHandler)

logger.debug('it is debug.')

print('a')
'''


'''
logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
a = 5
b = 0
try:
    c = a / b
except Exception as e:
    # 下面三种方式三选一，推荐使用第一种
    logging.exception("Exception occurred")
    logging.error("Exception occurred", exc_info=True)
    logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)
'''

