# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import MySQLdb
import re #정규 표현식

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'kic1234',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"직원자료 보기", pos = wx.DefaultPosition, size = wx.Size( 319,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer7 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"직급 입력 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer8.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtJik = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txtJik, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.btnOk = wx.Button( self.m_panel6, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.btnOk, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer8 )
        self.m_panel6.Layout()
        bSizer8.Fit( self.m_panel6 )
        bSizer7.Add( self.m_panel6, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.txtList = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.txtList.Enabled = False
        
        bSizer9.Add( self.txtList, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel7.SetSizer( bSizer9 )
        self.m_panel7.Layout()
        bSizer9.Fit( self.m_panel7 )
        bSizer7.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )

        self.SetSizer( bSizer7 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.btnOk.Bind(wx.EVT_BUTTON, self.OnClick)
        self.DbLoadShow()
        
    def __del__( self ):
        pass
    
    def DbLoadShow(self, jik = '전체'):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            if jik == '전체':
                sql = "SELECT jikwon_no, jikwon_name, jikwon_jik, jikwon_pay from jikwon"
            else:
                sql = "SELECT jikwon_no, jikwon_name, jikwon_jik, jikwon_pay from jikwon where jikwon_jik like '%{0}%'".format(jik)
            cursor.execute(sql)
            
            for (jikwon_no, jikwon_name, jikwon_jik, jikwon_pay) in cursor:
                self.txtList.AppendText('{0}\t{1}\t{2}\t{3}\n'.format(jikwon_no, jikwon_name, jikwon_jik, jikwon_pay))
                
        except Exception as e:
            print('err : ',e)
        finally:
            cursor.close()
            conn.close()
    def OnClick(self, event):
        jik = self.txtJik.GetValue()
        if len(jik) >= 2 and re.match(r'[가-힣]', jik):
            self.txtList.SetValue('')
            self.DbLoadShow(jik)
            
        else:
            wx.MessageBox('직급은 두 자 이상 한글만 입력하시오', '알림', wx.OK|wx.ICON_ERROR)
            self.txtJik.SetFocus()
            

