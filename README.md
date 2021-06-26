# Paint-Application
A simple paint application in python

This is a simple Paint application made using python .

![Screenshort of app](https://github.com/Kannampuzha/Paint-Application/blob/master/Screenshot.png)
![Canvas](https://github.com/Kannampuzha/Paint-Application/blob/master/Screenshot2.png)



The image is saved using 'pyscreenshort' , and it can be saved in
formats like jpeg,gif,png etc.

For windows users:
The 'save' button would work well only if 
you change the line 132 as follows:

`filename = asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (('JPEG', ('*.jpg','*.jpeg','*.jpe','*.jfif')),('PNG', '*.png'),('BMP', ('*.bmp','*.jdib')),('GIF', '*.gif')))`

