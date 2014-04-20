#!/usr/bin/env python
#mtime:2013/12/09
"""
besdirac-dms-dataset-delete
  remove a dataset from DB
  Usage:
    besdirac-dms-dataset-delete <datasetname>
"""

__RCSID__ = "$Id$"
from DIRAC import S_OK, S_ERROR, gLogger, exit
from DIRAC.Core.Base import Script

Script.setUsageMessage(__doc__)
args = Script.getPositionalArgs()

if len(args)!=1:
  Script.showHelp()
datasetName = args[0]

from BESDIRAC.Badger.API.Badger import Badger
badger = Badger()

result = badger.getFilesByDatasetName(datasetName)
if result['OK']:
  fileList = result['Value'] 
  fileCountDict = badger.reCalcCount(fileList,False)
  badger.removeDataset(datasetName)

  for file in fileCountDict:
    if fileCountDict[file] == 0:
      result = badger.removeFile(file)
      if not result['OK']:
        print "Failed remove file %s"%file


exit(0)