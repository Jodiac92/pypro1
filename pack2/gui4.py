# -*- coding: utf-8 -*- 

import wx
import wx.xrc

class MyCalc ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"간단 계산기", pos = wx.DefaultPosition, size = wx.Size( 240,270 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"숫자 1 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.txtNum1 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.txtNum1, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer6 )
        self.m_panel4.Layout()
        bSizer6.Fit( self.m_panel4 )
        bSizer5.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"숫자  2 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.txtNum2 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.txtNum2, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer7 )
        self.m_panel5.Layout()
        bSizer7.Fit( self.m_panel5 )
        bSizer5.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        rdoOpChoices = [ u"+", u"-", u"*", u"/" ]
        self.rdoOp = wx.RadioBox( self.m_panel6, wx.ID_ANY, u"연산자 선택", wx.DefaultPosition, wx.DefaultSize, rdoOpChoices, 1, wx.RA_SPECIFY_ROWS )
        self.rdoOp.SetSelection( 0 )
        bSizer8.Add( self.rdoOp, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel6.SetSizer( bSizer8 )
        self.m_panel6.Layout()
        bSizer8.Fit( self.m_panel6 )
        bSizer5.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"연산 결과 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer9.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.staResult = wx.StaticText( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )
        bSizer9.Add( self.staResult, 0, wx.ALL, 5 )
        
        
        self.m_panel7.SetSizer( bSizer9 )
        self.m_panel7.Layout()
        bSizer9.Fit( self.m_panel7 )
        bSizer5.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btnCalc = wx.Button( self.m_panel8, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        bSizer10.Add( self.btnCalc, 0, wx.ALL, 5 )
        
        self.btnClear = wx.Button( self.m_panel8, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        bSizer10.Add( self.btnClear, 0, wx.ALL, 5 )
        
        self.btnExit = wx.Button( self.m_panel8, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        bSizer10.Add( self.btnExit, 0, wx.ALL, 5 )
        
        
        self.m_panel8.SetSizer( bSizer10 )
        self.m_panel8.Layout()
        bSizer10.Fit( self.m_panel8 )
        bSizer5.Add( self.m_panel8, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnCalc.id = 1
        self.btnClear.id = 2
        self.btnExit.id = 3
        self.btnCalc.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnClear.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnExit.Bind( wx.EVT_BUTTON, self.OnProcess )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnProcess( self, event ):
        #event.Skip()
        sel_id = event.GetEventObject().id
        #print(sel_id)
        if sel_id == 1:
            #print(self.rdoOp.GetStringSelection())
            op = self.rdoOp.GetStringSelection()
            num1 = self.txtNum1.GetValue()
            num2 = self.txtNum2.GetValue()
            
            if num1 == '' or num2 == '':
                wx.MessageDialog(self, '값을 입력하시오', '에러', wx.OK).ShowModal()
                return
            
            try:
                mes = eval(num1 + op + num2)
            except Exception as e :
                wx.MessageDialog(self, '연산오류 : ' + str(e), '에러', wx.OK).ShowModal()
                return
            self.staResult.SetLabel(str(mes))
            
        elif sel_id == 2:
            self.txtNum1.SetLabel('')
            self.txtNum2.SetLabel('')
            self.staResult.SetLabel('')
            self.rdoOp.SetSelection(0)
            self.txtNum1.SetFocus()
            
        elif sel_id == 3:
            dlg = wx.MessageDialog(self, '정말 종료할까요?','알림', wx.YES_NO)
            imsi = dlg.ShowModal()
            if imsi == wx.ID_YES:
                dlg.Destroy() #MessageDialog 닫기
                self.Close() # Frame 닫기
                
if __name__ == '__main__':
    app = wx.App()
    MyCalc(None).Show()
    app.MainLoop()