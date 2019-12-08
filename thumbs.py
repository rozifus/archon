import os
import shutil

thumbs_folder = "thumbs"
thumb_ext = "jpg"


def move_to_thumbs(d, f):
    thumb_d = os.path.join(d, thumbs_folder)
    if not os.path.exists(thumb_d):
        os.makedirs(thumb_d)
    shutil.move(os.path.join(d, f), os.path.join(thumb_d, f))


def tidy(d):

    for root, dirs, files in os.walk(d, topdown=False):
        for f in files:
            if os.path.splitext(f)[-1] == ".jpg" and \
               os.path.split(root)[-1] != thumbs_folder:
                   move_to_thumbs(root, f)



if __name__=="__main__":
    tidy(os.getcwd())
