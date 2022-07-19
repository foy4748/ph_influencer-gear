import os, random

filenames = os.listdir('./logos/');
images = os.listdir('./images')

img = '<img src=\"./logos/{a}\" alt=\"{a}\">'

product = '''<div class="product">
            <img src="./images/{a}" alt="{a}" />
            <h1 class="product-title">{a}</h1>
            <h2 class="price">${n}.{n}</h2>
            <p class="ratings">
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star"></i>
              <i class="fa-solid fa-star-half"></i>
              4.9
            </p>
            <p class="someText">
              Wordwide shifting available Buyers protection possible!
            </p>
          </div>'''


#with open('test.txt','w') as file:
#    for filename in filenames:
#        file.write(img.format(a=filename)+'\n')

with open('test.txt','w') as file:
    for image in images:
        file.write(product.format(a=image,n=random.randint(50, 2000))+'\n')

