import requests #Package to get images from the web
import shutil #Package to save images locally

#Open files that contain the name of each file
summary = open("filenames.txt")	

for line in summary:
    photos = open(line.strip()) #Opens the file containing the photo link
    lines = photos.readlines()	

    num = int(lines[0].replace("\n",""))

    for i in range(num):
        #Reads each line that contains a photo link and cleans the filename
        image_url = lines[i+3].replace("\n","")
        filename = line.strip("-photo.txt\n")+"_img_"+str(i)+".jpg"

        #Opens the url image
        r = requests.get(image_url, stream = True)	

        #Check if the image was retrieved successfully
        if r.status_code == 200: 	
            r.raw.decode_content = True

            #Save the file locally with write permission
            with open(filename,'wb') as f:	
                shutil.copyfileobj(r.raw, f)
            print('Image sucessfully Downloaded: ',filename)
      else:
            print('Image Couldn\'t be retreived')

    photos.close()
summary.close()

