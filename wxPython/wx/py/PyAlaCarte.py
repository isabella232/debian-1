
"""Renamer stub: provides a way to drop the wx prefix from wxPython objects."""

__cvsid__ = "$Id: PyAlaCarte.py,v 1.1.2.2 2003/06/11 23:54:28 RD Exp $"
__revision__ = "$Revision: 1.1.2.2 $"[11:-2]

from wx import _rename
from wxPython.py import PyAlaCarte
_rename(globals(), PyAlaCarte.__dict__, modulename='py.PyAlaCarte')
del PyAlaCarte
del _rename
