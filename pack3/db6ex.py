# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import MySQLdb
import ast

with open('mariadb.txt', mode='r') as f:
    a = f.read()
    config = ast.literal_eval(a)
    
datas = []
rec = 0

class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"고객 관리", pos = wx.DefaultPosition, size = wx.Size( 500,324 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"직원번호 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.sta1 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
        self.sta1.Wrap( -1 )
        bSizer5.Add( self.sta1, 0, wx.ALL, 5 )
        
        self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"이름 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.sta2 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.sta2.Wrap( -1 )
        bSizer5.Add( self.sta2, 0, wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"부서명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer5.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.sta3 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
        self.sta3.Wrap( -1 )
        bSizer5.Add( self.sta3, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"직급 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer5.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self.sta4 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.sta4.Wrap( -1 )
        bSizer5.Add( self.sta4, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer5 )
        self.m_panel3.Layout()
        bSizer5.Fit( self.m_panel3 )
        bSizer4.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel4, wx.ID_ANY, u"처음", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel4, wx.ID_ANY, u"이전", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel4, wx.ID_ANY, u"다음", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel4, wx.ID_ANY, u"끝", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer6 )
        self.m_panel4.Layout()
        bSizer6.Fit( self.m_panel4 )
        bSizer4.Add( self.m_panel4, 0, wx.EXPAND|wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstGogek = wx.ListCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer7.Add( self.lstGogek, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel5.SetSizer( bSizer7 )
        self.m_panel5.Layout()
        bSizer7.Fit( self.m_panel5 )
        bSizer4.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.sta5 = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.sta5.Wrap( -1 )
        bSizer8.Add( self.sta5, 0, wx.ALL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer8 )
        self.m_panel6.Layout()
        bSizer8.Fit( self.m_panel6 )
        bSizer4.Add( self.m_panel6, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.lstGogek.InsertColumn(0, '고객번호', width = 100)
        self.lstGogek.InsertColumn(1, '고객명', width = 120)
        self.lstGogek.InsertColumn(2, '고객전화', width = 150)
        self.lstGogek.InsertColumn(3, '성별', width = 100)
        
        self.SetSizer( bSizer4 )
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
    
    
    # Virtual event handlers, overide them in your derived class
    def OnButton( self, event ):
        id = event.GetEventObject().id
        global rec
        if id == 1:
            rec = 0
        elif id == 2:
            rec -= 1
            if rec < 0:
                rec = 0
                return
        elif id == 3:
            rec += 1
            if rec > len(datas) - 1:
                rec = len(datas) - 1
                return
        elif id == 4:
            rec = len(datas) - 1
            
        self.ShowData(rec)
        
    def DbShow(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = """
            select  jikwon_no, jikwon_name, buser_name, jikwon_jik 
            from jikwon j, buser b
            where buser_num=buser_no
            """
            cursor.execute(sql)
            
            global datas
            datas = cursor.fetchall()
            
            self.ShowData(rec)
        except Exception as e:
            print('DbShow err :',e)
        finally:
            cursor.close()
            conn.close()
    
    def ShowData(self, num):
        self.sta1.SetLabel(str(datas[num][0]))
        self.sta2.SetLabel(str(datas[num][1]))
        self.sta3.SetLabel(str(datas[num][2]))
        self.sta4.SetLabel(str(datas[num][3]))
        self.lstGogek.DeleteAllItems()
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = """
            select gogek_no, gogek_name,  gogek_tel, gogek_jumin
            from gogek
            where gogek_damsano = '{0}'
            """.format(datas[num][0])
            
            cursor.execute(sql)
            
            for r in cursor:
                i = self.lstGogek.InsertItem(1000, 0)
                self.lstGogek.SetItem(i, 0, str(r[0]))
                self.lstGogek.SetItem(i, 1, r[1])
                self.lstGogek.SetItem(i, 2, r[2])
                jumin = r[3].split('-')
                if int(jumin[1][0]) % 2 == 1:
                    self.lstGogek.SetItem(i, 3, '남')
                else:
                    self.lstGogek.SetItem(i, 3, '여')
                
                
            self.sta5.SetLabelText('고객수 : ' + str(self.lstGogek.GetItemCount()))
        except Exception as e:
            print('ShowData err :',e)
        finally:
            cursor.close()
            conn.close()
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()

