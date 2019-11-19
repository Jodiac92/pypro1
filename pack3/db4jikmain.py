import wx
from pack3 import db4jik

if __name__ == '__main__':
    app = wx.App()
    frame = db4jik.MyFrame2(None)
    frame.Show()
    app.MainLoop()