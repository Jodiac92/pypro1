# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'kic1234',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"고객관리", pos = wx.DefaultPosition, size = wx.Size( 458,323 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직원번호", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtJik_no = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtJik_no, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직원명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtJik_name = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtJik_name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.btnJik_Ok = wx.Button( self.m_panel1, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnJik_Ok, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.stalogin = wx.StaticText( self.m_panel4, wx.ID_ANY, u"로그인을 해주세요.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.stalogin.Wrap( -1 )
        bSizer3.Add( self.stalogin, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel4.SetSizer( bSizer3 )
        self.m_panel4.Layout()
        bSizer3.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstGoGek = wx.ListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer4.Add( self.lstGoGek, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.staCount = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer5.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer5 )
        self.m_panel3.Layout()
        bSizer5.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        # 표 제목 설정
        self.lstGoGek.InsertColumn(0, '고객번호', width = 100)
        self.lstGoGek.InsertColumn(1, '고객명', width = 150)
        self.lstGoGek.InsertColumn(2, '고객전화', width = 170)
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnJik_Ok.Bind( wx.EVT_BUTTON, self.OnLogin )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnLogin( self, event ):
        if self.txtJik_no.GetValue() == '' or self.txtJik_name.GetValue() == '':
            wx.MessageBox('입력 자료를 모두 입력하시오', '오류', wx.OK)
            return
        
        num = self.txtJik_no.GetValue()
        name = self.txtJik_name.GetValue()
    
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            tdata = (num, name)
            
            sql = """
            select * from jikwon
            where jikwon_no = '{0}' and jikwon_name = '{1}'
            """.format(*tdata)
            
            logCk = cursor.execute(sql)
            
            self.txtJik_name.SetLabelText('')
            self.txtJik_no.SetLabelText('')
            
            if logCk > 0:
                self.stalogin.SetLabelText('{}번 {}직원의 관리고객'.format(num, name))
                self.ListData(num)
            else:
                wx.MessageBox('로그인 실패 ', '오류', wx.OK)
                return
                
        except Exception as e:
            wx.MessageBox('로그인 작업 실패 : '+str(e), '오류', wx.OK)
        finally:
            cursor.close()
            conn.close()
            
    def ListData(self, num):
        try:
            self.lstGoGek.DeleteAllItems()
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()

            sql = '''
            select gogek_no,gogek_name,gogek_tel
            from gogek g, jikwon j
            where g.gogek_damsano = j.jikwon_no and j.jikwon_no = {0}
            order by gogek_no asc
            '''.format(num)
            
            cursor.execute(sql)
            datas = cursor.fetchall()

            for row in datas:
                i = self.lstGoGek.InsertItem(1000, 0) # 최대행, 초기행 수
                self.lstGoGek.SetItem(i, 0, str(row[0]))
                self.lstGoGek.SetItem(i, 1, row[1])
                self.lstGoGek.SetItem(i, 2, row[2])
                
            self.staCount.SetLabelText('고객 인원수 :' + str(self.lstGoGek.GetItemCount()))
        except Exception as e:
            wx.MessageBox('리스트 읽기: '+str(e), '오류', wx.OK)
        finally:
            cursor.close()
            conn.close()
         
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()