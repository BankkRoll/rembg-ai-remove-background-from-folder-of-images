from rembg import remove
from PIL import Image
import os,glob

folder_path_src = 'WithBG' # input image folder path
output_path = 'WithoutBG' # output image folder path

for filename in glob.glob(os.path.join(folder_path_src, '*.*')):
  with open(filename, 'r') as f:
    input_file_name = os.path.splittext(filename)[0]
    print(input_file_name)
    file_name = input_file_name.replace(folder_path_src,'')
    print(file_name)
    out_path = folder_path_dest+file_name+'.png'
    print(out_path)
    input = Image.open(filename)
    output = remove(input)
    output.save(out_path)
