from PIL import Image
import os


# infile: The actual image file name (ex: Name.png)
# lnX: The list of x positions for horizontal bounds
# lnY: The list of y positions for vertical bounds


def crop(imgFile, lnX, lnY, exportPath):
    imgSource = Image.open(imgFile)  # Open the image source

    for i in range(3):  # Loop for rows 
        #To split vertically in halves use range(1)
        for j in range(3):  # Loop for cols
            #To split vertically in halves use range(2)
            imgHeight = lnY[i + 1] - lnY[i]  # Define the height of specific crop
            #To split vertically in halves keep it constant, i.e. equal to half(considering we are splitting vertically) like 
            #imgHeight = 1700
            imgWidth = lnX[j + 1] - lnX[j]  # Define the width of specific crop

            # Set crop bounds [aka box] (LeftEdgeX, TopEdgeY,RightEdgeX, BottomEdgeY)
            box = (lnX[j], lnY[i], lnX[j + 1], lnY[i + 1])

            # Create new image with crop
            img = Image.new('RGB', (imgWidth, imgHeight), 255)  # (mode, (width, height), color)
            img.paste(imgSource.crop(box))  # apply crop to new image

            # Export file
            si = str(i)
            sj = str(j)
            fileName = si + sj  # Name by rows and cols (ex: 00, 01, 02, 10, 11, 12)
            path = os.path.join(exportPath, "%s.png" % fileName)  # Joins specified path with file name
            img.save(path)  # Saves the image to specified path


if __name__ == '__main__':
    # Config
    # ----------------------------------------
    # imgFile: the source img
    # exportPath: the folder to export images to
    # lnX: x positions for horizontal bounds
    # lnY: y positions for vertical bounds
    # ----------------------------------------
    imgFile = 'Test-Crop-Image.png'
    exportPath = '\Exported-Folder'

    lnX1 = 0
    lnX2 = 1080
    lnX3 = 2160
    lnX4 = 300
    #To split vertically in halves
#     lnX1 = 0#keep it 0
#     lnX2 = 1080#change it to half of width
#     lnX3 = 2160#change it to total width

    
    lnY1 = 0
    lnY2 = 100
    lnY3 = 200
    lnY4 = 300
    ##To split vertically in halves
#     lnY1 = 0#keep it 0
#     lnY2 = 1700#change it to height of image

    # ----------------------------------------

    lnX = [lnX1, lnX2, lnX3, lnX4]
    #To split vertically in halves
#     lnX = [lnX1, lnX2, lnX3]
    lnY = [lnY1, lnY2, lnY3, lnY4]
    #To split vertically in halves
#     lnY = [lnY1, lnY2]

    crop(imgFile, lnX, lnY, exportPath)
