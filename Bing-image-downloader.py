!pip install bing-image-downloader

from bing_image_downloader import downloader

query = "Female wearing mask"

output_dir = "/content/female_wearing_mask"   ## path of your empty folder of female_wearing_mask

downloader.download(query, limit=100, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60)

import os

for path, subdirs, files in os.walk(output_dir):
  
    for name in files:
      
        print(os.path.join(path, name))
      
### Similarly change the query to "Male wearing mask " and upload those images in Male_wearing_mask folder
