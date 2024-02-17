import os

from twisted.python.logfile import LogFile
from twisted.application import service
from twisted.python.log import ILogObserver, FileLogObserver

from buildbot.master import BuildMaster


basedir = os.path.abspath(os.path.dirname(__file__))
rotateLength = 10000000
maxRotatedFiles = 10
configfile = 'master.cfg'

# Default umask for server
umask = None

# note: this line is matched against to check that this is a buildmaster
# directory; do not edit it.
application = service.Application('buildmaster')
logfile = LogFile.fromFullPath(
    os.path.join(basedir, "twistd.log"),
    rotateLength=rotateLength,
    maxRotatedFiles=maxRotatedFiles
)
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

m = BuildMaster(basedir, configfile, umask)
m.setServiceParent(application)
m.log_rotation.rotateLength = rotateLength
m.log_rotation.maxRotatedFiles = maxRotatedFiles