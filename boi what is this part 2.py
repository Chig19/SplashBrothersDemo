import random
import matplotlib.pyplot as plt
import os.path
import numpy as np 
import PIL


directory=os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'woman.jpg')
img = plt.imread(filename)


    

        # Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'sadness.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.show()

# Open, resize, and display earth
earth_file = os.path.join(directory, 'snowman.jpg')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((400, 400)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (325, 235), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(0, 885)
axes3[1].set_ylim(1100, 400)
fig3.show()    


def round_corners_one_image(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
   
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1 is the corner radius as 
    portion of shorter dimension of original_image
    """
    # Set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) #radius in pixels
  
    ###
    # Create a mask
    ###
  
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
  
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
  
    # Draw two rectangles to fill interior with opaqueness 
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))
  
    # Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius),
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0, height-2*radius, 2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
  
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)

    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result