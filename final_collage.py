import random
import matplotlib.pyplot as plt
import os.path
import numpy as np 
import PIL


directory=os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'woman.jpg')
img = plt.imread(filename)


    


directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'sadness.jpg')


student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')


axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400)
axes[1].set_ylim(1100, 850)
fig.show()


earth2_file = os.path.join(directory, 'yooshi.png')
earth2_img = PIL.Image.open(earth2_file)
earth2_small = earth2_img.resize((400, 400))
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth2_img)
axes2[1].imshow(earth2_small)
fig2.show()

earth_file = os.path.join(directory, 'yoshi.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((400, 400))
fig4, axes4 = plt.subplots(1, 2)
axes4[0].imshow(earth_img)
axes4[1].imshow(earth_small)
fig4.show()

earth3_file = os.path.join(directory, 'daquanshi.png')
earth3_img = PIL.Image.open(earth3_file)
earth3_small = earth3_img.resize((400, 400))
fig5, axes5 = plt.subplots(1, 2)
axes5[0].imshow(earth3_img)
axes5[1].imshow(earth3_small)
fig5.show()

earth4_file = os.path.join(directory, 'snowman.jpg')
earth4_img = PIL.Image.open(earth4_file)
earth4_small = earth4_img.resize((400, 400))
fig6, axes6 = plt.subplots(1, 2)
axes6[0].imshow(earth4_img)
axes6[1].imshow(earth4_small)
fig6.show()

student_img.paste(earth_small, (325, 235), mask=earth_small) 
student_img.paste(earth2_small, (200, 1000), mask=earth2_small)
student_img.paste(earth3_small, (600, 800), mask=earth3_small)
student_img.paste(earth4_small, (100, 200), mask=earth4_small)

fig3, axes3 = plt.subplots(1,2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(0, 885)
axes3[1].set_ylim(1100, 400)
fig3.show()    
