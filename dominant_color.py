from PIL import Image
import numpy as np
import requests
from io import BytesIO


def rgb_to_hex(r, g, b):
    hex_str = ["0", "1", "2", "3", "4", "5", "6",
               "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_vals = ['f', 'f', 'f', 'f', 'f', 'f']
    hex_vals[0] = hex_str[r // 16]
    hex_vals[1] = hex_str[int((r/16 - (r // 16))*16)]
    hex_vals[2] = hex_str[g // 16]
    hex_vals[3] = hex_str[int((g/16 - (g // 16))*16)]
    hex_vals[4] = hex_str[b // 16]
    hex_vals[5] = hex_str[int((b/16 - (b // 16))*16)]
    return "".join(hex_vals)


def dominant_color(img_url, resize_ratio=20, round_group=20):
    response = requests.get(img_url)
    im = Image.open(BytesIO(response.content))

    (width, height) = (im.width // resize_ratio, im.height // resize_ratio)
    img = im.resize((width, height))

    arr = np.asarray(img)

    [r, g, b] = count_colors(arr, round_group)
    color = rgb_to_hex(int(r), int(g), int(b))

    return color


def count_colors(arr, group=20):
    colors = {}
    for i in arr:
        for j in i:
            r = j[0] - (j[0] % group)
            g = j[1] - (j[1] % group)
            b = j[2] - (j[2] % group)
            name = str(r) + "." + str(g) + "." + str(b)
            if(name in colors):
                colors.__setitem__(name, colors[name] + 1)
            else:
                colors[name] = 1
    a = np.array(list(colors.values()))
    index = a.argmax()
    color = list(colors.keys())[index]
    return color.split(".")


if __name__ == "__main__":
    image = "https://images.unsplash.com/photo-1591520323419-7dc0c8ea23e7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
    print("#" + dominant_color(image))
