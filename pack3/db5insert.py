# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import MySQLdb
import locale

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'kic1234',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

class MySangpum ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"상품 처리", pos = wx.DefaultPosition, size = wx.Size( 414,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"상품명 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer3.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtSang = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
        bSizer3.Add( self.txtSang, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText10 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"수량 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer3.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtSu = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.txtSu, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText11 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"단가 :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer3.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtDan = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.txtDan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.btnOk = wx.Button( self.m_panel7, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btnOk, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel7.SetSizer( bSizer3 )
        self.m_panel7.Layout()
        bSizer3.Fit( self.m_panel7 )
        bSizer2.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstView = wx.ListCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer4.Add( self.lstView, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel8.SetSizer( bSizer4 )
        self.m_panel8.Layout()
        bSizer4.Fit( self.m_panel8 )
        bSizer2.Add( self.m_panel8, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText13 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"건수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        bSizer5.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.staCount = wx.StaticText( self.m_panel9, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer5.Add( self.staCount, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel9.SetSizer( bSizer5 )
        self.m_panel9.Layout()
        bSizer5.Fit( self.m_panel9 )
        bSizer2.Add( self.m_panel9, 0, wx.EXPAND |wx.ALL, 5 )
        
        # 표 제목 설정
        self.lstView.InsertColumn(0, '코드', width = 50)
        self.lstView.InsertColumn(1, '상품명', width = 150)
        self.lstView.InsertColumn(2, '수량', width = 50)
        self.lstView.InsertColumn(3, '단가', width = 50)
        self.lstView.InsertColumn(4, '금액', width = 100)
        
        # 언어, 지역 , 날짜, 시간, 숫자 등에 형식을 설정 할 수 있다.
        locale.setlocale(locale.LC_NUMERIC, '') # 숫자
        
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnOk.Bind( wx.EVT_BUTTON, self.OnInsert )
        
        self.ListData()
        
    def __del__( self ):
        pass
    
    def ListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            cursor.execute("select * from sangdata order by code desc")
            datas = cursor.fetchall()
            self.lstView.DeleteAllItems()
            for row in datas:
                i = self.lstView.InsertItem(1000, 0) # 최대행, 초기행 수
                self.lstView.SetItem(i, 0, str(row[0]))
                self.lstView.SetItem(i, 1, row[1])
                self.lstView.SetItem(i, 2, str(row[2]))
                self.lstView.SetItem(i, 3, str(row[3]))
                #self.lstView.SetItem(i, 4, str(row[2] * row[3]))
                self.lstView.SetItem(i, 4, locale.format_string('%d',row[2] * row[3], 1))
                
            #self.staCount.SetLabelText(str(len(datas)))
            self.staCount.SetLabelText(str(self.lstView.GetItemCount()))
            
        except Exception as e:
            wx.MessageBox('리스트 오류 : '+str(e), '오류', wx.OK) 
        finally:
            cursor.close()
            conn.close()
    # Virtual event handlers, overide them in your derived class
    # 등록 작업
    def OnInsert( self, event ):
        if self.txtSang.GetValue() == '' or self.txtDan.GetValue() == '' or self.txtSu.GetValue() == '':
            wx.MessageBox('입력 자료를 모두 입력하시오', '오류', wx.OK)
            return
        
        if self.txtSu.GetValue().isalpha() or self.txtDan.GetValue().isalpha():
            wx.MessageBox('수량과 단가는 숫자만 입력하시오', '오류', wx.OK)
            return
        
        sang = self.txtSang.GetValue()
        su = self.txtSu.GetValue()
        dan = self.txtDan.GetValue()
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            # 신상 코드 얻기 작업
            try:
                cursor.execute("select count(*) from sangdata")
                code = cursor.fetchone()[0] + 1
            except:
                code = 1
            
            tdata = (code, sang, su, dan)
            cursor.execute("insert into sangdata values(%s,%s,%s,%s)", tdata)
            conn.commit();
            
            # 추가 후 목록 보기
            self.ListData()
            self.txtSang.SetLabelText('')
            self.txtSu.SetLabelText('')
            self.txtDan.SetLabelText('')
            self.txtSang.SetFocus()
        except Exception as e:
            wx.MessageBox('추가 실패 : '+str(e), '오류', wx.OK)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        
        
if __name__ == '__main__':
    app = wx.App()
    MySangpum(None).Show()
    app.MainLoop()