# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import MySQLdb
import ast

with open('mariadb2.txt', mode='r') as f:
    config = ast.literal_eval(f.read())
    
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"회원관리", pos = wx.DefaultPosition, size = wx.Size( 304,378 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"번호 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNo, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.btnInsert = wx.Button( self.m_panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnInsert, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.btnUpdate = wx.Button( self.m_panel2, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btnUpdate, 0, wx.ALL, 5 )
        
        self.btnConfirm = wx.Button( self.m_panel2, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer3.Add( self.btnConfirm, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"전화 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.txtTel = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtTel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.btnDel = wx.Button( self.m_panel3, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btnDel, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstMem = wx.ListCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer5.Add( self.lstMem, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.staCnt = wx.StaticText( self.m_panel5, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCnt.Wrap( -1 )
        bSizer6.Add( self.staCnt, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer6 )
        self.m_panel5.Layout()
        bSizer6.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnInsert.id = 1
        self.btnUpdate.id = 2
        self.btnConfirm.id = 3
        self.btnDel.id = 4
        self.btnConfirm.Enabled = False
        self.btnInsert.Bind( wx.EVT_BUTTON, self.OnButtonHandler )
        self.btnUpdate.Bind( wx.EVT_BUTTON, self.OnButtonHandler )
        self.btnConfirm.Bind( wx.EVT_BUTTON, self.OnButtonHandler )
        self.btnDel.Bind( wx.EVT_BUTTON, self.OnButtonHandler )
    
        self.lstMem.InsertColumn(0, '번호', width=50)
        self.lstMem.InsertColumn(1, '이름', width=100)
        self.lstMem.InsertColumn(2, '전화', width=115)
        
        self.viewListData()
    def __del__( self ):
        pass
    
    def viewListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from pymem"
            cursor.execute(sql)
            
            self.lstMem.DeleteAllItems()
            for r in cursor:
                i = self.lstMem.InsertItem(1000, 0)
                self.lstMem.SetItem(i, 0, str(r[0]))
                self.lstMem.SetItem(i, 1, r[1])
                self.lstMem.SetItem(i, 2, r[2])
                
            self.staCnt.SetLabel(str(self.lstMem.GetItemCount()))
        except Exception as e:
            print('읽기 오료류 : ',e)
        finally:
            cursor.close()
            conn.close()
    # Virtual event handlers, overide them in your derived class
    def OnButtonHandler( self, event ):
        id = event.GetEventObject().id
        
        if id == 1:
            self.MemInsert() # 등록
        elif id == 2:
            self.MemUpdate() # 수정 준비
        elif id == 3:
            self.MemUpdateOk() # 수정
        elif id == 4:
            self.MemDelete() # 삭제
        elif id == 5:
            self.MemUpdateCancel() # 수정 취소
    
    def MemInsert(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel == '':
            wx.MessageBox('모든 자료를 입력하시오','오류',wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            data = self.SelectData(no)
            
            # 중복 체크
            if data != None:
                wx.MessageBox(no + '번은 이미 사용중인 번호 입니다.','알림',wx.OK)
                self.txtNo.SetFocus()
                return
            
            # 추가 작업
            datas = (no, name, tel)
            sql = "insert into pymem values(%s,%s,%s)"
            cursor.execute(sql,datas)
            conn.commit()
            
            # 리스트 초기화
            self.viewListData()
            
            # txt 초기화
            self.txtNo.SetValue('')
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
        except Exception as e:
            print('MemInsert err :',e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
            
    def MemUpdate(self):
        dlg = wx.TextEntryDialog(None, '수정할 번호 입력', '수정')
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                return
            
            upno = dlg.GetValue()
            #print(upno)
            data = self.SelectData(upno)
            
            # 등록 여부 확인
            if data == None:
                wx.MessageBox(upno + '번은 등록된 번호가 아닙니다.', '알림', wx.OK)
                return
            
            # 수정 작업
            self.txtNo.SetValue(str(data[0]))
            self.txtName.SetValue(data[1])
            self.txtTel.SetValue(data[2])
            
            self.txtNo.Enabled = False
            self.btnUpdate.SetLabel('취소')
            self.btnUpdate.id = 5
            self.btnConfirm.Enabled = True
            
        dlg.Destroy()
        
    def MemUpdateOk(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if name == '' or tel == '':
            wx.MessageBox('모든 자료를 입력하시오','오류',wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "update pymem set irum = '{0}', junhwa = '{1}' where bun = '{2}'".format(name, tel, no)
            
            cursor.execute(sql)
            conn.commit()
            
            self.viewListData()
            self.txtNo.SetValue('')
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            
            self.txtNo.Enabled = True
            self.btnUpdate.SetLabel('수정')
            self.btnUpdate.id = 2
            self.btnConfirm.Enabled = False            
        except Exception as e:
            print('MemUpdateOk err :',e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
            
    def MemDelete(self):
        dlg = wx.TextEntryDialog(None, '삭제할 번호 입력', '수정')
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                return
            
            delno = dlg.GetValue()
            data = self.SelectData(delno)
            
            # 등록 여부 확인
            if data == None:
                wx.MessageBox(delno + '번은 등록된 번호가 아닙니다.', '알림', wx.OK)
                return
            
            # 삭제 작업
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                sql = "delete from pymem where bun = {0}".format(delno)
                cursor.execute(sql)
                conn.commit()
                
                self.viewListData()
            except Exception as e:
                print('MemDelete err : ',e)
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
            # 텍스트 초기화
            self.txtNo.SetValue('')
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            
            
        dlg.Destroy()
        
    def MemUpdateCancel(self):
        self.txtNo.SetValue('')
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
        
        self.txtNo.Enabled = True
        self.btnUpdate.SetLabel('수정')
        self.btnUpdate.id = 2
        self.btnConfirm.Enabled = False
        
    def SelectData(self, num): # 번호 체크(등록, 수정, 삭제시 사용)
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from pymem where bun = {0}".format(num)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except Exception as e:
            print('MemInsert err :',e)
        finally:
            cursor.close()
            conn.close()
            
if __name__ == '__main__':
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()  

