from PIL import Image
from keygen import *
from utils import *
import argparse


def encode(image_path,degree,pwd):
    extension=image_path.split('.')[-1]

    try:
    	im = Image.open(image_path, "r")
    except FileNotFoundError:
    	print ('Image path is incorrect. Try again.')
    	exit(0)

    im = Image.open(image_path, "r")
    arr = im.load()  # pixel data stored in this 2D array
    (W, H) = im.size
    print(W, H)

    KEY = generate_tuples(H, W, pwd)

    for i in range(4):
        # ith Wave
        first = cascade(KEY[i][0:2], degree, W, H)
        second = cascade(KEY[i][2:], degree, W, H)
        automate_swap(first, second, degree + 1, im, arr)

    color(arr,KEY[0][0:3],W,H)
    saved_path="Enc/" + image_path.split("/")[-1] + "_en.png"
    if "uploads" in image_path:
        saved_path="uploads/"+saved_path
        saved_path=saved_path.replace('Enc/','')
    # im.show() #To display the image im
    im.save(saved_path)
    return (im,arr,saved_path)


def efficiency_calc(image_path,im,arr):
    im2 = Image.open(image_path, "r")
    (W,H) = im.size
    # To calculate efficiency of the algorithm
    arr2 = im2.load()
    efficiency(arr2, arr, W, H)
    im.show()

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='absolute/relative path to the image file')
    args = parser.parse_args()

    image_path = args.path

    if(image_path is None):
        print ('Please provide the path to image file. Try again.')
        exit(0)
    degree = int(input("Enter degree: "))
    pwd = getpass.getpass("Enter password: ")
    (im,arr)=encode(image_path,degree,pwd)
    efficiency_calc(image_path,im,arr)
