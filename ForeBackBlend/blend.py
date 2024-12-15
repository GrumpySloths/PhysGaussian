from PIL import Image

# 打开前景和背景图片
foreground = Image.open('/home/jiahao/PhysGaussian/fore.png')
background = Image.open('/home/jiahao/PhysGaussian/background.png')

print("foreground size: ", foreground.size)
print("background size: ", background.size)
print("foreground mode: ", foreground.mode)
print("background mode: ", background.mode)
# 确保前景和背景图片的尺寸相同
foreground = foreground.resize(background.size)

# 创建一个新的图像，大小与背景图像相同
combined = Image.new('RGBA', background.size)

# 将背景图像粘贴到新图像上
combined.paste(background, (0, 0))

# 将前景图像粘贴到新图像上，使用前景图像的alpha通道作为掩码
combined.paste(foreground, (0, 0), foreground)

# 保存合成后的图像
combined.save('/home/jiahao/PhysGaussian/combined.png')