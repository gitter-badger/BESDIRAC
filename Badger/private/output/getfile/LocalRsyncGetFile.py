from BESDIRAC.Badger.private.output.getfile.GetFile     import GetFile
from BESDIRAC.Badger.private.output.getfile.LocalMount  import LocalMount
from BESDIRAC.Badger.private.output.getfile.Rsync       import Rsync

class LocalRsyncGetFile(LocalMount, Rsync, GetFile):
  def __init__(self):
    super(LocalRsyncGetFile, self).__init__()
