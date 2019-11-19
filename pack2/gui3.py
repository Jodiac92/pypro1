# -*- coding: utf-8 -*- 

import wx
import wx.xrc

class TestForm ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"연습", pos = wx.DefaultPosition, size = wx.Size( 300,196 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer7.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.txtName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer7 )
        self.m_panel4.Layout()
        bSizer7.Fit( self.m_panel4 )
        bSizer3.Add( self.m_panel4, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"나이 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer8.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtAge = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txtAge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.btnOk = wx.Button( self.m_panel5, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.btnOk, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer8 )
        self.m_panel5.Layout()
        bSizer8.Fit( self.m_panel5 )
        bSizer3.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText8 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"결과", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer9.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.staResult = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )
        
        bSizer9.Add( self.staResult, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel6.SetSizer( bSizer9 )
        self.m_panel6.Layout()
        bSizer9.Fit( self.m_panel6 )
        bSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.OnShowData )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnShowData( self, event ):
        #event.Skip()
        name = self.txtName.GetValue()
        if name == '':
            wx.MessageBox('이름 입력','알림',wx.OK)
            return
        
        age = self.txtAge.GetValue()
        
        self.staResult.SetLabel(name + ' ' + age)
if __name__ == '__main__':
    app = wx.App()
    TestForm(None).Show()
    app.MainLoop()