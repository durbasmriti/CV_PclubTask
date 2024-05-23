# CV_PclubTask

#### Google drive link for the datasets :
Female_wearing_mask : https://drive.google.com/drive/folders/1--pF1PnyQxZIr53PBH19H5xvKqolY0EI?usp=drive_link
Male_wearing_mask : https://drive.google.com/drive/folders/1pE62nFCIBQGYUUwLXj2lPeeR9qYhX6R_?usp=drive_link

## Approach to find datasets :
-Firstly I tried finding it online and found this https://buffml.com/face-mask-detection-gender-age-prediction/  but here most of the male pictures were of same person so lagged diversity and the images were no labelled , still I thought to work with this only so I made two folders in drive one Female_wearing_mask and the other is male_wearing mask but started uploading images by myself , took some pictures from the link above too .

-After I uploaded approximately 200 pictures in each category I was tired  AND soon I realised this not gonna work so I tried searching online if there were any other sites like Kaggle where datsets can be found but failed after visiting a lot of them .

-Finally I came across a YouTube video about bing_image_downloader and my search ended here . 

-On google colab , I connected google drive to it and used bing_image_downloader and uploaded more than 500 pictures in each category .

-And yes now my two folders in google drive were not empty anymore :)

## Instructions to get your own datasets:
- make two folder one named "female_wearing_mask" and other "Male_wearing_mask"
  
- Copy the code of bing-image-downloader.py in your colab
 
- change your query and directory as per your need

## Instructions on how to run the code 
- download the datasets in your google drive
- connect google with google drive(code included in the code file)
- open the code with google colab
- In Google colab go to "Runtime" -> "change runtime type " to GPU preferably to increase the efficiency of the code
- Run the code with patience because it will take a lot of your time
- If you still face issue running it like "unavailabilty of RAM" in google drive the reduce the "batch size"

![Screenshot 2024-05-21 105514](https://github.com/durbasmriti/CV_PclubTask/assets/152951506/ab80a515-5467-4ed6-8083-0cefd614f7b9)

![Screenshot 2024-05-21 105723](https://github.com/durbasmriti/CV_PclubTask/assets/152951506/3f7472d8-f24b-4c90-84ec-a5ff3f2c2862)

![Screenshot 2024-05-21 110057](https://github.com/durbasmriti/CV_PclubTask/assets/152951506/009213f6-bcd2-456b-98d5-98c37a8942ed)

![Screenshot 2024-05-21 110547](https://github.com/durbasmriti/CV_PclubTask/assets/152951506/9f4cfbbe-d261-443a-8802-c10710f2e2c9)

## HOW TO RUN THE CODE ?
![Team brainstorm](https://github.com/durbasmriti/CV_PclubTask/assets/152951506/f90a8432-2521-44f2-b368-bc594cf88dc6)

## Difficulty faced :
- first wasted too much time searching for datasets
- due to large datasets it was taking too much time for google colab cell to run
- Then I switched to GPU for decreasing the time but in free Google colab , there is some limit to use GPU.
- I forgot to take screenshots of my model working and limit for GPU has also ended so I literally had to wait for 3-4 hours for completing the runtime .
- My google colab was also crashing at times for non-availability of RAM.
- I then tried reducing batch size to minimize the RAM usage but it compromised the accuracy .
- later I switched my google account and got access to GPU again and took the screenshots and GPU takes really less time compared to CPU.

