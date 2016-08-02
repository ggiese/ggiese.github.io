import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL
import PIL.ImageDraw     

def openFile(filename, isPlt = True):
    # Go to the directory
    directory = os.path.dirname(os.path.abspath(__file__))
    # Get the path to the file
    filepath = os.path.join(directory, filename)
    # Open the image
    if isPlt:
        img = plt.imread(filepath)
    else:
        img = PIL.Image.open(filepath)
    return img

def purpleify(img, fig, ax):
# Get Height and Width of image
    height = len(img)
    width = len(img[0])
    
    for r in range(170,655):
        for c in range(140,874):
            if img[r][c][1] < img[r][c][0] or (r in range(356, 537) and c in range(475,552)):
                temp=img[r][c][2]
                img[r][c][2] = img[r][c][0]
                img[r][c][0] = img[r][c][1]
                img[r][c][1] = temp    
    fig.canvas.draw

def circularFade(original_image, (cx, cy)=(0,0), radius=0):
    width, height = original_image.size
    if cx == 0 and cy == 0:
        (cx, cy) = (width / 2, height / 2)
    if radius == 0:
        radius = min([width - cx, cx, cy, height - cy])

    #start with transparent mask
    faded_mask = PIL.Image.new('RGBA', (width, height), (255,255,255,0))
    drawing_layer = PIL.ImageDraw.Draw(faded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    for r in range(radius,0,-10):
        my_color = (0, 0, 0, int(255-255.0/radius*r))
        #color = (127,0,127,0)
        #drawing_layer.ellipse((cx-r, cy-r, cx+r, cy+r), fill=color, outline=color)
        drawing_layer.ellipse((5,5,100,100),fill=my_color)
        
    # Make the new image, starting with all transparent
    retval = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    retval.paste(original_image, (0,0), mask=faded_mask)
    return retval
    
butterfly = openFile('sulfur.JPG')
# Original image
fig1, ax1 = plt.subplots(1,1)
ax1.axis('off')
ax1.imshow(butterfly, interpolation='none')
fig1.show()

# Purple image
purpleButterfly = openFile('sulfur.JPG')
fig2, ax2 = plt.subplots(1,1)
ax2.axis('off')
#ax.imshow(butterfly, interpolation='none')
purpleify(purpleButterfly, fig2, ax2)
ax2.imshow(purpleButterfly, interpolation='none')
fig2.show()

# Purple image with earth
fig3, ax3 = plt.subplots(1,1)
ax3.axis('off')
imgEarth = openFile('earth.png', False)
pilPurpleButterfly = PIL.Image.fromarray(purpleButterfly)
pilPurpleButterfly.paste(imgEarth, (900,600), mask=imgEarth)
ax3.imshow(pilPurpleButterfly, interpolation='none')
fig3.show()

