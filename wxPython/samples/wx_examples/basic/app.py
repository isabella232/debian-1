#!/usr/bin/env python

"""Basic application class."""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"
__cvsid__ = "$Id: app.py,v 1.1.2.1 2003/04/18 21:15:33 RD Exp $"
__revision__ = "$Revision: 1.1.2.1 $"[11:-2]

import wx

from frame import Frame

class App(wx.App):
    """Application class."""

    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()
