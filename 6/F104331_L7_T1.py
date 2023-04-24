""" 
Съставете графично приложение с помощта на wxPython, което изчислява Body Mass Index. 
Входните параметри са височина в сантиметри и тегло в килограми и BMI се получава като 
се раделят килограмите на височината в метри на квадрат. 
Програмата да е с име FXXXXX_L7_T1.py, където XXXXX е вашият факултетен номер.

"""

import wx

class BMI(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = 'BMI Calculator')
        panel = wx.Panel(self)
        
        bmi_label = wx.StaticText( panel, label = "Body Mass Index:", pos = (20, 20) )
        self.bmi = wx.StaticText( panel, label = " ", pos = (150, 20) )
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        bmi_label.SetFont(font)
        self.bmi.SetFont(font)
        
        weight_label = wx.StaticText( panel, label = "Weight (Kg):", pos = (20, 80) )
        height_label = wx.StaticText( panel, label = "Height (Cm):", pos = (20, 150) )
        self.weight = wx.SpinCtrl( panel, value = '0', min = 0, max = 500, pos = (150, 80) )
        self.height = wx.SpinCtrl(panel, value='0', min = 100, max = 250, pos = (150, 150) )
        
        calculateButton = wx.Button( panel, label = 'Calculate BMI', pos = (70, 210))
        closeButton = wx.Button( panel, label = 'Close', pos = (220, 210))
        
        calculateButton.Bind( wx.EVT_BUTTON, self.Calculate_BMI )
        closeButton.Bind( wx.EVT_BUTTON, self.On_Close )

    def Calculate_BMI(self, event):
        weight = self.weight.GetValue()
        height = self.height.GetValue()
        bmi = weight / (( height / 100 )** 2)
        
        self.bmi.SetLabel( str( round( bmi, 2 )) )

    def On_Close(self, event):
        self.Close(True)

def main():  
    app = wx.App()
    ex = BMI()
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()  