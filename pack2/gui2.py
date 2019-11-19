# 레이아웃 매니저 : sizer

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title = title, size = (300, 250))
        
        panel1 = wx.Panel(self, -1, style = wx.SUNKEN_BORDER)
        panel2 = wx.Panel(self, -1, style = wx.SUNKEN_BORDER)
        
        panel1.SetBackgroundColour('BLUE')
        panel2.SetBackgroundColour('RED')
        
        box = wx.BoxSizer(wx.VERTICAL) # HORIZONTAL : 가로 # VERTICAL : 세로
        box.Add(panel1, 1, wx.EXPAND)
        box.Add(panel2, 1, wx.EXPAND)
        
        self.SetSizer(box)
        self.Center()
        self.Show(show=True)

if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title = '레이아웃')
    app.MainLoop()