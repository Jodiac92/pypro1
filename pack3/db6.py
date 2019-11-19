# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import MySQLdb
import ast

with open('mariadb.txt', mode='r') as f:
    aa = f.read()
    config = ast.literal_eval(aa)
#print(config)

datas = []
rec_r = 0

class MyForm ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"레코드 이동", pos = wx.DefaultPosition, size = wx.Size( 414,124 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"코드 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer7.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtCode = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer7.Add( self.txtCode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText7 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"상품명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer7.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtSang = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.txtSang, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer7 )
        self.m_panel5.Layout()
        bSizer7.Fit( self.m_panel5 )
        bSizer6.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel6, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel6, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel6, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel6, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer8 )
        self.m_panel6.Layout()
        bSizer8.Fit( self.m_panel6 )
        bSizer6.Add( self.m_panel6, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer6 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
        self.btn1.Bind( wx.EVT_BUTTON, self.OnButton )
        self.btn2.Bind( wx.EVT_BUTTON, self.OnButton )
        self.btn3.Bind( wx.EVT_BUTTON, self.OnButton )
        self.btn4.Bind( wx.EVT_BUTTON, self.OnButton )
        
        self.DbShow()
    def __del__( self ):
        pass
    
    def DbShow(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select  * from sangdata"
            cursor.execute(sql)
            
            global datas
            datas = cursor.fetchall()
            
            #print(datas)
            #print(datas[0]) # (1, '장갑', 3, 10000)
            #print(datas[0][0]) # 1
            self.ShowData(rec_r)
        except Exception as e:
            print('err :',e)
        finally:
            cursor.close()
            conn.close()
            
    def ShowData(self, r):
        self.txtCode.SetLabel(str(datas[r][0]))
        self.txtSang.SetLabel(datas[r][1])
    # Virtual event handlers, overide them in your derived class
    def OnButton( self, event ):
        id = event.GetEventObject().id
        global rec_r
        
        if id == 1:
            rec_r = 0
        elif id == 2:
            rec_r -= 1
            if rec_r < 0: 
                rec_r = 0
                return
        elif id == 3:
            rec_r += 1
            if rec_r > len(datas) - 1 :
                rec_r = len(datas) - 1
                return
        elif id == 4:
            rec_r = len(datas) - 1
        
        self.ShowData(rec_r)
        

if __name__ == '__main__':
    app = wx.App()
    MyForm(None).Show()
    app.MainLoop()