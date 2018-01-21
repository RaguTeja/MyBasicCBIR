from __future__ import print_function
from pyimagesearch.cbir import HSVDescriptor
from imutils import paths
import progressbar
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True,
	help = "Path to where the features index will be stored")
args = vars(ap.parse_args())
desc=HSVDescriptor((4,6,3))
op=open(args["index"],"w")
imagepaths=list(paths.list_images(args["dataset"]))
widgets=["Indexing: ",progressbar.Percentage()," ",progressbar.Bar(),"",progressbar.ETA()]
pbar=progressbar.ProgressBar(maxval=len(imagepaths),widgets=widgets)
pbar.start()
for (i,imagepath) in enumerate(imagepaths):
 filename=imagepath[imagepath.rfind("/")+1:]
 image=cv2.imread(imagepath)
 features=desc.describe(image)
 features=[str(x) for x in features]
 op.write("{},{}\n".format(filename,",".join(features)))
 pbar.update(i)
pbar.finish()
print("[info] indexed {} images".format(len(imagepaths)))
