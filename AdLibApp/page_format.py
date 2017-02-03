class T_Handler(webapp2.RequestHandler):

    header = "<h1>AdLibMania.Com</h1>" + """<br><img src="/images/Image_NAOF.jpg" name="1">"""
    header = header + """<br><br><BR><img src="/Image_NAOF.JPG" name="2">""" # """<br><img src="C:\Users\Chien\Desktop\images\Image_NAOF.JPG">""" #
    body = "<br>Hello, World, again!<br>"
    background = """<body background="theBG" bgcolor="green">"""
    background = background.replace("theBG", "http://pad1.whstatic.com/images/f/f6/Stick-figure-Step-1.jpg")
    #body2 = keyboard
    footer = "<br><br><br><br><br><br><br><br><br>Made by Team ______<br><br>"
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def write_html(self):
        self.write(self.header)
        #self.write(self.header2)
        self.write(self.body)
        self.write(self.background)
        #self.write(self.body2)
        self.write(self.footer)
