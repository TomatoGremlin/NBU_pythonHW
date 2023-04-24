""" 
Съставете графично приложение с помощта на wxPython, което представлява игра на бесеница. 
Думите да се зареждат от текстов файл и да се избира една случайно.
Първата и последната буква от избраната за познаване дума се показват, другите символи се заместват със символа за подчертаване.
Всеки опит се предприема като се натиска toggle button, който представлява буква от азбуката. 
Ако избраната буква се съдържа в думата, тя се показва на всички позиции, на които се среща. 
В противен случай броя на оставащите допустими грешки се намалява с единица. Това се визуализира и с картинка.

Когато се изчерпят и шестте налични опита, играчът губи. Ако играчът познае всички букви за по-малко от шест опита – печели.




sizer = wx.FlexGridSizer(0, 4, 10, 10)

for i in self.button:
    sizer.Add(i, 0, wx.ALL, 0)

pnl.SetSizer(sizer)

Кода създава грид като css::Grid
задаваш му колони и размери между всяка колона и ред
след това минавам през списъка с бутони и ги добавям.

Накрая го качвам и ги реди супер лесно. 
Това помага вместо да си играем всеки бутон да му слагаме координати отделно


"""

import wx
import random


class HangedMan_Game(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = 'Hanged Man')
        panel = wx.Panel(self)
        
        self.attempts_left = 6
        
        
        # ---- Change path to the text file with words if needed ------- 
        
        txtFile_path = "images/words.txt"
        #self.word_Options = [ "cheese", "forest", "computer"]
        with open(txtFile_path, 'r') as f:
            self.word_Options = [line.strip() for line in f.readlines()]
        self.word = random.choice(self.word_Options).upper()
        
        
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
       
        self.underscoredWord_label = wx.StaticText(panel, label = self.word[0] + '_' * (len(self.word) - 2) + self.word[-1] , pos = (150, 20))
        self.underscoredWord_label.SetFont(font)
        
        self.result_label = wx.StaticText(panel, label="",  pos = (30, 70))
        self.result_label.SetFont(font)

        
        alphabet_matrix = [
        'ABCDEFGHIJK',
        'LMNOPQRSTUV',
        'WXYZ'
        ]
        
        y_axis = 140
        for i in range(0, len(alphabet_matrix)):
            x_axis = 20
            for letter in alphabet_matrix[i]:
                self.letter_btn = wx.ToggleButton(panel, label=letter, pos = (x_axis, y_axis ), size =(30, 30))
                self.letter_btn.Bind(wx.EVT_TOGGLEBUTTON, self.letterClicked_toggle)
                x_axis+= 30
                
            y_axis += 30


        image = wx.Image("images/mistake0.png", wx.BITMAP_TYPE_ANY)
        scaled_image = image.Scale(100, 100)
        self.current_image = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap(scaled_image),  pos = (150, 240 ))
        
        
        # ---- Change paths to pictures if needed ------- 
        self.hanging_images = [
        wx.Image("images/mistake6.png",  wx.BITMAP_TYPE_ANY),
        wx.Image("images/mistake5.png",  wx.BITMAP_TYPE_ANY),
        wx.Image("images/mistake4.png",  wx.BITMAP_TYPE_ANY),
        wx.Image("images/mistake3.png",  wx.BITMAP_TYPE_ANY),
        wx.Image("images/mistake2.png",  wx.BITMAP_TYPE_ANY),
        wx.Image("images/mistake1.png",  wx.BITMAP_TYPE_ANY),
        ]

        
        self.guessButton = wx.Button( panel, label = 'Guess', pos = (160, 360 ))
        self.guessButton.Bind(wx.EVT_BUTTON, self.guessClicked_button)

       
        
    def letterClicked_toggle(self, event):
        
       selected_button = event.GetEventObject()
       selected_letter = selected_button.GetLabel()
       
       if selected_letter in self.word:
            unguessedWord_list = list(self.underscoredWord_label.GetLabel())
            word_list = list(self.word)
            
            for i in range(len(word_list)):
                if word_list[i] == selected_letter:
                    unguessedWord_list[i] = selected_letter
            
            self.underscoredWord_label.SetLabel(''.join(unguessedWord_list))
            
            if '_' not in unguessedWord_list:
                self.result_label.SetLabel("You have won!")
                
       else:
            self.attempts_left -= 1

            if self.attempts_left == 0 :
                self.result_label.SetLabel("Game over! You have lost.")
                
                image = self.hanging_images[self.attempts_left] 
                scaled_image = image.Scale(100, 100)
                self.current_image.SetBitmap(  wx.Bitmap(scaled_image) )
                
            elif self.attempts_left >= 1:
                self.result_label.SetLabel(f"You have {self.attempts_left} tries left.")
                
                image = self.hanging_images[self.attempts_left] 
                scaled_image = image.Scale(100, 100)
                self.current_image.SetBitmap(  wx.Bitmap(scaled_image) )
                
      
        
    def guessClicked_button( self, event ):
        self.underscoredWord_label.SetLabel(self.word)
            

def main(): 
    app = wx.App()
    ex = HangedMan_Game()
    ex.Show()
    app.MainLoop()
 
if __name__ == '__main__':
    main()  