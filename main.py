from PIL import Image
import piexif

def add_fake_metadata(image_path, output_path):

    img = Image.open(image_path)


    exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}}
    
    # Add camera details
    exif_dict["0th"][piexif.ImageIFD.Make] = "Apple"  
    exif_dict["0th"][piexif.ImageIFD.Model] = "iPhone 14 Pro" 
    exif_dict["0th"][piexif.ImageIFD.Software] = "iOS 17.1" 
    

    exif_dict["0th"][piexif.ImageIFD.DateTime] = "2024:11:16 12:34:56"
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = "2024:11:16 12:34:56"
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = "2024:11:16 12:34:56"


    exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = "N" 
    exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = (
        (44, 1), (27, 1), (56, 10000)
    )
    exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = "W"
    exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = (
        (88, 1), (5, 1), (24, 10000) 
    )
    exif_dict["GPS"][piexif.GPSIFD.GPSAltitudeRef] = 0
    exif_dict["GPS"][piexif.GPSIFD.GPSAltitude] = (200, 1) 


    exif_dict["Exif"][piexif.ExifIFD.FocalLength] = (5, 1)  
    exif_dict["Exif"][piexif.ExifIFD.ISOSpeedRatings] = 50  


    user_comment = "Photo taken during a trip.".encode("ascii")
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = b"\x00\x00\x00" + user_comment


    exif_bytes = piexif.dump(exif_dict)
    img.save(output_path, exif=exif_bytes)

    print(f"Fake metadata added successfully! Saved to {output_path}")

# Input and output file paths
input_image = "img.jpeg"  # Path to the input image
output_image = "img2.jpeg"  # Path to the output image


add_fake_metadata(input_image, output_image)