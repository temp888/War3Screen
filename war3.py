# coding=utf-8
'''
    war3 宽屏补丁

    将你的分辨率填充到宽和高中即可
'''


from wx import *
import _winreg

class War3Frame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self, parent, -1,title=u'War3改键助手 v1.0',size=(380, 250))
        panel = wx.Panel(self, -1)
        self.widthStatic = wx.StaticText(panel,-1,u'宽度',pos=(100,30))
        self.withText= wx.TextCtrl(panel,-1,'',pos=(140,30))
        self.heightStatic = wx.StaticText(panel,-1,u'高度',pos=(100,80))
        self.heightText = wx.TextCtrl(panel,-1,'',pos=(140,80))
        self.settingButton =wx.Button(panel,-1,u'设置',pos=(130,120))
        self.Bind(wx.EVT_BUTTON,self.Setting,self.settingButton)
        wx.Frame.Show(self, True)
    def Setting(self,EVENT):
        widthvalue = self.withText.GetValue()
        heightvalue = self.heightText.GetValue()
        try:
            widthvalue = int(widthvalue)
            heightvalue = int(heightvalue)
        except:
            print u'参数设置错误'
        try:
            keypath = 'Software\\Blizzard Entertainment\\Warcraft III\\Video'
            hkey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,keypath,0,_winreg.KEY_ALL_ACCESS)
            # print _winreg.QueryInfoKey(hkey)
            # print _winreg.QueryValueEx(hkey,'resheight')
            # print _winreg.QueryValueEx(hkey,'reswidth')
            _winreg.SetValueEx(hkey,'resheight',0,_winreg.REG_DWORD,heightvalue)
            _winreg.SetValueEx(hkey,'reswidth',0,_winreg.REG_DWORD,widthvalue)
            # print _winreg.QueryValueEx(hkey, 'resheight')
            # print _winreg.QueryValueEx(hkey, 'reswidth')
        except Exception as e:
            print e
class War3Screen(wx.App):
    def OnInit(self):
        Server = War3Frame(None)
        return True

if __name__ == '__main__':
    myapp = War3Screen()
    myapp.MainLoop()