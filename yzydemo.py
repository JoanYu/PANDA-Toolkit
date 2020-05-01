from PANDA import PANDA_IMAGE, PANDA_VIDEO
import panda_utils as util
from ImgSplit import ImgSplit
from ResultMerge import DetResMerge

def main():
    image_root = '/Users/xduyzy/Downloads/PANDA_IMAGE'
    person_anno_file = 'person_bbox_train.json'
    annomode = 'person'
    example = PANDA_IMAGE(image_root, person_anno_file, annomode='person', showwidth=1280)
    # example.showImgs(range=1)
    # print('starting save images with annos...')
    example.showAnns(range=5, shuffle=True, saveimg=True)
    # outpath = 'split' 
    # outannofile = 'split.json'
    # print('starting spriting images to \"'+outpath+'/image\" folder...')
    # split = ImgSplit(image_root, person_anno_file, annomode, outpath, outannofile)
    # split.splitdata(1)
    # print('done!')

if __name__ == '__main__':
    main()