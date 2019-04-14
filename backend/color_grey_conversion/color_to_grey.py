from PIL import Image

#sub 1 to actual value




def convert_rgb_image_to_greyscale(input_file, output_file):
    rgb_to_grey_dict = {}
    label_to_grey = {}
    label_to_rgb = {}
    rgb_to_label = {}
    label_to_rgb["sea"] = (56,79,131)
    label_to_rgb["clouds"] = (239,239,239)
    label_to_rgb["dirt"] = (44,30,22)
    label_to_rgb["bush"] = (93,110,50)
    label_to_rgb["grass"] = (183,210,78)
    label_to_rgb["mountain"] = (60,59,75)
    label_to_rgb["road"] = (152,126,106)
    label_to_rgb["sky-other"] = (117,158,223)
    label_to_rgb["tree"] = (53,38,19)
    label_to_rgb["pavement"] = (99,99,99)
    label_to_rgb["flower"] = (230,112,182)
    label_to_rgb["fog"] = (193,195,201)
    label_to_rgb["hill"] = (119,108,45)
    label_to_rgb["leaves"] = (191,96,44)
    label_to_rgb["river"] = (50,96,77)
    rgb_to_label = {v: k for k, v in label_to_rgb.items()}
    labels = open("labels.md")
    i = 0
    for line in labels:
        if(i>12):
            columns = line.split("|")
            num = int(columns[0].strip())-1
            label = columns[1].strip()
            label_to_grey[label] = (num)
        i = i + 1
    in_img = Image.open(input_file)
    out_img = Image.new("L",(in_img.size[0],in_img.size[1]))
    pixels = in_img.load()
    p_o = out_img.load()
    grey = (0)
    for i in range(in_img.size[0]):    # for every col:
        for j in range(in_img.size[1]):    # For every row
            if(pixels[i,j][0:3] in rgb_to_label.keys()):
                label = rgb_to_label[pixels[i,j][0:3]]
                grey = label_to_grey[label]
            p_o[i,j] = grey
    out_img.save(output_file)





def main():
    in_file = "masterpiece.png"
    out_file = "b.png"
    convert_rgb_image_to_greyscale(in_file,out_file)


if __name__ == '__main__':
    main()
