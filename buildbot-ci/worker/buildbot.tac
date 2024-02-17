
import os

from twisted.application import service
from twisted.python.logfile import LogFile
from twisted.python.log import ILogObserver, FileLogObserver

from buildbot_worker.bot import Worker


basedir = os.path.abspath(os.path.dirname(__file__))
rotateLength = 10000000
maxRotatedFiles = 10

application = service.Application('buildbot-worker')
application.setComponent(ILogObserver, FileLogObserver(
    LogFile.fromFullPath(
        os.path.join(basedir, "twistd.log"),
        rotateLength=rotateLength,
        maxRotatedFiles=maxRotatedFiles
    )
).emit)


## ===> Worker configuration
buildmaster_host = 'localhost'
workername = 'worker'
passwd = 'worker123'
port = 9989

connection_string = None
keepalive = 600
umask = None
maxdelay = 300
numcpus = None
allow_shutdown = None
maxretries = None
use_tls = 0
delete_leftover_dirs = 0
proxy_connection_string = None
protocol = 'pb'

s = Worker(buildmaster_host, port, workername, passwd, basedir,
           keepalive, umask=umask, maxdelay=maxdelay,
           numcpus=numcpus, allow_shutdown=allow_shutdown,
           maxRetries=maxretries, protocol=protocol, useTls=use_tls,
           delete_leftover_dirs=delete_leftover_dirs,
           connection_string=connection_string,
           proxy_connection_string=proxy_connection_string)
s.setServiceParent(application)
