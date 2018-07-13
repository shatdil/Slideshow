import matplotlib.image as mpi
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from glob import glob


img_folder = 'images\\*.jpg'
images = glob(img_folder)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)

ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)    
plt.title("Slide-show with button", color="red", fontsize=16)   
img = mpi.imread(images[1])
ax.imshow(img)

str1 = 'A simple Slideshow'
str2 = 'Please press the next or previous button'

ax.imshow(img)
fig.suptitle(str1, color="red", fontsize=22, fontweight='bold') 
ax.set_title(str2, color="blue", fontsize=10)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False) 
ax.tick_params(labelbottom="off")
ax.tick_params(labelleft="off")    
         
class Index(object):
    ind = 1

    def next(self, event):
        self.ind += 1
        i = self.ind % len(images)
        img = mpi.imread(images[i])
        ax.imshow(img)

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(images)
        img = mpi.imread(images[i])
        ax.imshow(img)


callback = Index()
axprev = plt.axes([0.3, 0.05, 0.2, 0.06])
axnext = plt.axes([0.55, 0.05, 0.2, 0.06])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()		
