"""  
С помощта на wxPython създайте image viewer с възможности за:
● Показване на изображението
● Извеждане на информация за изображението - име, размер, тип, режим на цветовете
● Прилагане на различни трансформации и филтри - въртене на 90 градуса, хоризонтално и вертикално огледално обръщане, промяна на размера, филтри.

Приложението трябва да дава възможност за последователно прилагане на различни трансформации, както и съхраняването на промените във файл.
"""

import wx
import wx.lib.agw.floatspin as FS
from PIL import Image, ImageFilter


class ImageViewerApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ImageViewerApp, self).__init__(*args, **kwargs)
        self.SetSize((800, 600))
        self.SetTitle("Image Viewer")

        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.image_ctrl = wx.StaticBitmap(panel)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)

        info_label = wx.StaticText(panel, label="Image Information:")
        self.info_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(-1, -1))

        load_button = wx.Button(panel, label="Load Image")
        rotate_button = wx.Button(panel, label="Rotate 90°")
        flip_horizontal_button = wx.Button(panel, label="Flip Horizontal")
        flip_vertical_button = wx.Button(panel, label="Flip Vertical")
        resize_label = wx.StaticText(panel, label="Resize:")
        self.resize_width = FS.FloatSpin(panel, value=0, min_val=0, max_val=3000, increment=1, size=(-1, -1))
        self.resize_height = FS.FloatSpin(panel, value=0, min_val=0, max_val=3000, increment=1, size=(-1, -1))

        resize_button = wx.Button(panel, label="Resize")
        filter_label = wx.StaticText(panel, label="Filter:")
        self.filter_choice = wx.Choice(panel, choices=["Blur", "Sharpen", "Contour", "Edge Enhance"])
        apply_filter_button = wx.Button(panel, label="Apply Filter")
        save_button = wx.Button(panel, label="Save Changes")

        vbox1.Add(self.image_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox1.Add(info_label, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox1.Add(self.info_text, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        vbox2.Add(load_button, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(rotate_button, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(flip_horizontal_button, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(flip_vertical_button, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(resize_label, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(self.resize_width, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(self.resize_height, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(resize_button, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(filter_label, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(self.filter_choice, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(apply_filter_button, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)
        vbox2.Add(save_button, flag=wx.TOP | wx.LEFT | wx.RIGHT, border=10)

        hbox.Add(vbox1, proportion=2, flag=wx.EXPAND | wx.ALL, border=10)
        hbox.Add(vbox2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(hbox)

        self.image = None
        self.current_image_path = ""
        self.original_image_size = (0, 0)

        load_button.Bind(wx.EVT_BUTTON, self.on_load_image)
        rotate_button.Bind(wx.EVT_BUTTON, lambda event: self.apply_image_transform(self.image.rotate(90, expand=True)))
        flip_horizontal_button.Bind(wx.EVT_BUTTON, lambda event: self.apply_image_transform(self.image.transpose(Image.FLIP_LEFT_RIGHT)))
        flip_vertical_button.Bind(wx.EVT_BUTTON, lambda event: self.apply_image_transform(self.image.transpose(Image.FLIP_TOP_BOTTOM)))
        resize_button.Bind(wx.EVT_BUTTON, lambda event: self.apply_image_transform(self.image.resize((int(self.resize_width.GetValue()), int(self.resize_height.GetValue())))))
        apply_filter_button.Bind(wx.EVT_BUTTON, self.on_apply_filter)
        save_button.Bind(wx.EVT_BUTTON, self.on_save_changes)

        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_load_image(self, event):
        wildcard = "Image files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png"
        dialog = wx.FileDialog(self, message="Select an image file", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dialog.ShowModal() == wx.ID_OK:
            self.current_image_path = dialog.GetPath()
            self.load_image(self.current_image_path)
        dialog.Destroy()

    def load_image(self, path):
        self.current_image_path = path
        self.image = Image.open(path)
        self.original_image_size = self.image.size
        self.scale_image_to_fit()
        self.update_image_ctrl()
        self.update_info_text()

    def scale_image_to_fit(self):
        max_width = 400
        max_height = 300
        image_width, image_height = self.image.size

        if image_width > max_width or image_height > max_height:
            ratio = min(max_width / image_width, max_height / image_height)
            new_width = int(image_width * ratio)
            new_height = int(image_height * ratio)
            self.image = self.image.resize((new_width, new_height))

    def update_image_ctrl(self):
        if self.image is not None:
            wx_image = wx.Image(self.image.size[0], self.image.size[1])
            wx_image.SetData(self.image.convert("RGB").tobytes())
            self.image_ctrl.SetBitmap(wx_image.ConvertToBitmap())

    def update_info_text(self):
        if self.image is not None:
            info = f"Name: {self.current_image_path}\n"
            info += f"Size: {self.original_image_size[0]} x {self.original_image_size[1]}\n"
            info += f"Type: {self.image.format}\n"
            info += f"Mode: {self.image.mode}"
            self.info_text.SetValue(info)

    def apply_image_transform(self, new_image):
        if new_image is not None:
            self.image = new_image
            self.scale_image_to_fit()
            self.update_image_ctrl()

    def on_apply_filter(self, event):
        if self.image is not None:
            selected_filter = self.filter_choice.GetStringSelection()
            if selected_filter == "Blur":
                filtered_image = self.image.filter(ImageFilter.BLUR)
            elif selected_filter == "Sharpen":
                filtered_image = self.image.filter(ImageFilter.SHARPEN)
            elif selected_filter == "Contour":
                filtered_image = self.image.filter(ImageFilter.CONTOUR)
            elif selected_filter == "Edge Enhance":
                filtered_image = self.image.filter(ImageFilter.EDGE_ENHANCE)
            else:
                filtered_image = None

            self.apply_image_transform(filtered_image)

    def on_save_changes(self, event):
        if self.image is not None:
            self.image.save(self.current_image_path)
            wx.MessageBox("Changes saved successfully.", "Save Changes")

    def on_close(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = ImageViewerApp(None)
    frame.Show()
    app.MainLoop()
