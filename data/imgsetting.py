
import glob
from PIL import Image

# for i in range(1, 316):
#     imgs = str(i) + '.jpg'
#     url = 'D:/projects/django/sawwell/static/assets/img/market/' + imgs
#     img = Image.open(url)
#
#     img_resize = img.resize((800, 600))
#     img_resize.save(url)

files = glob.glob('D:/projects/django/sawwell/static/assets/img/market/*')
for f in files:
    try:
        img = Image.open(f)
        img_resize = img.resize((800, 600))
        # 타이틀, 확장자
        # title, ext = os.path.splitext(f)
        img_resize.save(f)
        print('succes' + f)
    except OSError as e:
        print('error')
