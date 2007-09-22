
"""Renamer stub: provides a way to drop the wx prefix from wxPython objects."""

__cvsid__ = "$Id: pypalette.py,v 1.1.2.2 2003/06/11 23:54:32 RD Exp $"
__revision__ = "$Revision: 1.1.2.2 $"[11:-2]

from wx import _rename
from wxPython.lib.colourchooser import pypalette
_rename(globals(), pypalette.__dict__, modulename='lib.colourchooser.pypalette')
del pypalette
del _rename
