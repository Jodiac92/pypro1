# 윈도우용 프로그래밍 : wxpython
import wx

# app = wx.App(False)  
# frame = wx.Frame(None, wx.ID_ANY, "Hi")
# frame.Show(show=True)  
# app.MainLoop()

class Ex(wx.Frame):
    def __init__(self, parent, title):
        super(Ex, self).__init__(parent, title = title, size = (300, 300))
        
        # 텍스트 박스
        #self.txtA = wx.TextCtrl(self) # 싱글라인
        #self.txtA = wx.TextCtrl(self, style = wx.TE_MULTILINE) # 멀티라인
        
        self.CreateStatusBar() # 상태 표시줄
        
        # 메뉴
        menuBar = wx.MenuBar()
        
        mnuFile = wx.Menu()
        mnuNew = mnuFile.Append(wx.ID_NEW, 'New','새글')
        mnuOpen = mnuFile.Append(wx.ID_OPEN, 'Open', '열기')
        mnuFile.AppendSeparator() # 구분선
        mnuExit = mnuFile.Append(wx.ID_EXIT, 'Exit', '종료')
        
        menuBar.Append(mnuFile, 'File')
        self.SetMenuBar(menuBar)
        
        # 메뉴에 이벤트 장착
        self.Bind(wx.EVT_MENU, self.OnEvent1, mnuNew)
        self.Bind(wx.EVT_MENU, self.OnEvent2, mnuExit)
        
        # -------------------------------------------
        panel = wx.Panel(self)
        wx.StaticText(panel, label = 'i d : ', pos = (5, 5))
        wx.StaticText(panel, label = 'pwd : ', pos = (5, 40))
        self.TxtA = wx.TextCtrl(panel, pos = (40, 5))
        self.TxtB = wx.TextCtrl(panel, pos = (40, 40))
        
        # 버튼 처리
        btn1 = wx.Button(panel, label = '일반 버튼', pos = (5, 100))
        btn2 = wx.ToggleButton(panel, label = '토글 버튼', pos = (100, 100))
        btn3 = wx.Button(panel, label = '종료', pos = (200, 100), size = (50, -1))
        # 이벤트 핸들러 연결 후 처리 방법1
#         btn1.Bind(wx.EVT_BUTTON, self.OnClick1)
#         btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClick2)
#         btn3.Bind(wx.EVT_BUTTON, self.OnClick3)
        # 이벤트 핸들러 연결 후 처리 방법2
        btn1.id = 1; btn2.id = 2; btn3.id = 3
        btn1.Bind(wx.EVT_BUTTON, self.OnAbc)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnAbc)
        btn3.Bind(wx.EVT_BUTTON, self.OnAbc)
        
        self.Center()
        self.Show()

    def OnEvent1(self, event): # event 핸들러 메소드는 event argument 추가
        #self.TxtA.SetLabelText("evnet")
        # 대화 상자
        msgDial = wx.MessageDialog(self, '메시지', '제목', wx.OK)
        msgDial.ShowModal()
        msgDial.Destroy()
        self.SetTitle('버튼1 클릭')
        
    def OnEvent2(self, event):
        self.Close(force=True)
    
    def abc(self):
        print('일반 메소드')
        
    def OnClick1(self, event):
        self.TxtA.SetLabelText('버튼 1')
        
    def OnClick2(self, event):
        #print(event.GetEventObject().GetValue())
        if event.GetEventObject().GetValue():
            self.TxtA.SetLabelText('kbs')
            self.TxtB.SetLabelText('9')
        else:
            self.TxtA.SetLabelText('')
            self.TxtB.SetLabelText('')
    def OnClick3(self, event):
        self.Close()
        
    def OnAbc(self, event):
        print(event.GetEventObject().id)
        if event.GetEventObject().id == 1:
            self.TxtA.SetLabelText("1")
        elif event.GetEventObject().id == 2:
            self.TxtA.SetLabelText("2")
        else:
            self.Close()
if __name__ == '__main__':
    app = wx.App()
    Ex(None, title = '나의 창')
    app.MainLoop()