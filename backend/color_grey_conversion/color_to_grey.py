from PIL import Image
<<<<<<< HEAD
import json

# sub 1 to actual value

=======

#sub 1 to actual value
>>>>>>> 210d45c28f2787ebe48418d6d8acf842d72fe29f

def convert_rgb_image_to_greyscale(input_file, output_file):
    label_to_grey = {}
    label_to_rgb = {}
    rgb_to_label = {}
<<<<<<< HEAD

    with open("labels.txt", "r") as labels:
        for line in labels.readlines():
            line = line.strip()
            split_line = line.split(' ')
            if len(split_line) < 3:
                continue
            grey, label, rgb_list = split_line
            rgb = tuple(map(int, rgb_list.split(',')))

            label_to_rgb[label] = rgb
            rgb_to_label[rgb] = label
            # I forget why we are off by 1
            label_to_grey[label] = int(grey) - 1

    in_img = Image.open(input_file)
    out_img = Image.new("L", (in_img.size[0], in_img.size[1]))
    pixels = in_img.load()
    p_o = out_img.load()
    grey = (0)

    for i in range(in_img.size[0]):    # for every col:
        for j in range(in_img.size[1]):    # For every row
            # print(pixels[i, j][0:3])
            if(pixels[i, j][0:3] in rgb_to_label.keys()):
                label = rgb_to_label[pixels[i, j][0:3]]
                grey = label_to_grey[label]
            p_o[i, j] = grey
    out_img.save(output_file)


def main():
    in_file = "masterpiece.png"
    out_file = "b.png"
    convert_rgb_image_to_greyscale(in_file, out_file)
=======
    rgb_mapping = open("label_to_rgb")
    labels = open("labels.md")
    for line in rgb_mapping:
        columns = line.split("=")
        num = tuple([int(v) for v in columns[1].strip().split(",")])
        label = columns[0].strip()
        label_to_rgb[label] = (num)
    rgb_to_label = {v: k for k, v in label_to_rgb.items()}
    for line in labels:
        columns = line.split("|")
        num = int(columns[0].strip())-1
        label = columns[1].strip()
        label_to_grey[label] = (num)
    in_img = Image.open(input_file)
    out_img = Image.new("L",(in_img.size[0],in_img.size[1]))
    pixels = in_img.load()
    p_o = out_img.load()
    grey = 0
    for i in range(in_img.size[0]):    # for every col:
        for j in range(in_img.size[1]):    # For every row
            if(pixels[i,j][0:3] in rgb_to_label.keys()):
                label = rgb_to_label[pixels[i,j][0:3]]
                grey = label_to_grey[label]
            p_o[i,j] = grey
    labels.close()
    rgb_mapping.close()
    out_img.save(output_file)



def main():
    in_file = "masterpiece.png"
    out_file = "b.png"
    convert_rgb_image_to_greyscale(in_file,out_file)
>>>>>>> 210d45c28f2787ebe48418d6d8acf842d72fe29f


if __name__ == '__main__':
    main()
