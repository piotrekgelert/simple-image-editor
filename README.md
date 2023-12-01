# simple-image-editor
Simple image editor is made in Python 3.87 with PIL and tkinter in object oriented approach.
For demo purposes I used images from Unsplash.com. 

## A note:
Right after start it creates two txt files: recent_comp_paths.txt and recent_url_paths.txt to save visited places.
Use images with dimension 1080x800 or smaller.
All images if bigger than 1080x800 can be downsized with aspect ratio when opened (very big images don't work properly yet).

### UI example:

<p align="middle">
  <img src="https://github.com/piotrekgelert/simple-image-editor/blob/master/images/waterfall.jpg" width="800"/>
</p>

Photo by [Alexander Schimmeck](https://unsplash.com/@alschim?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 'A large waterfall with a boat in the middle of it' on Unsplash

### Features
- Every command opens as independent pop-up window with possibility of movement on the entire computer screen

### Commands
- [x] File
    - [x] Open file
    - [x] Open url
    - [x] Save as
- [x] Edit
    - [x] Crop image
    - [x] Flip image
    - [x] Rotate
    - [x] Resize
- [x] Color
    - [x] Color Balance
    - [x] Contrast
    - [x] Brightness
    - [x] Sharpness
    - [x] Desaturate
    - [x] Color Noise
    - [x] Color Invert
- [x] Filter
    - [x] Blur
    - [x] Contour
    - [x] Detail
    - [x] Emboss
    - [x] Smooth
    - [x] Edges

Additional info:

### Used packages:
- [tkinter 8.5 - source](https://www.tcl.tk/)
- [tkinter - python docs](https://docs.python.org/3/library/tkinter.html)
- [PIL 10.1.0](https://python-pillow.org/)
- [pyinstaller 6.2.0](https://pyinstaller.org/en/stable/)
- [nullsoft scriptable install system NSIS 3.09](https://nsis.sourceforge.io/Download)

### Running the project
App opens from `image_editor.py` file
or
Use exe file. It will install image editor in any chosen folder 


## Licence
This project is licensed under the [MIT] License - see [Licence.md](LICENSE) file for details.