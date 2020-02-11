from PIL import Image
import sys


# 朋友圈发布9宫格图 index_ulr = https://www.jb51.net/article/164708.htm

# 获取图片
def fill_image(image):
    width, height = image.size

    # 选择较长的那个作为新图
    new_image_length = width if width > height else height
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color="white")

    # 将之前的图粘贴在新图上，居中
    if width > height:  # 原图宽大于高，则填充图片的竖直维度
        # (x,y)二元组表示粘贴上图相对下图的起始位置
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))

    return new_image


# 切图
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []

    for i in range(0, 3):  # 两重循环，生成9张图片基于原图的位置
        for j in range(0, 3):
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]

    return image_list


# 保存图片
def save_image(image_list):
    index = 1
    for image in image_list:
        image.save(str(index) + '.jpg')
        index += 1


if __name__ == '__main__':
    image_path = "/Users/hao/PycharmProjects/home_exam/wechat_moments/我不洗碗.jpg"
    image = Image.open(image_path)

    image = fill_image(image)
    image_list = cut_image(image)
    save_image(image_list)
