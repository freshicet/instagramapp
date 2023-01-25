import argparse
from PIL import Image, ExifTags
from fractions import Fraction
from datetime import datetime


def get_exif_data(image_file):
    with Image.open(image_file) as img:
        exif_data = {ExifTags.TAGS[k]: v for k, v in img._getexif().items()}
    return exif_data

def get_fnumber(exif_data):
    if 'FNumber' in exif_data:
        return exif_data['FNumber']
    return None

def get_focal_length(exif_data):
    if 'FocalLength' in exif_data:
        return exif_data['FocalLength']
    return None

def get_iso(exif_data):
    if 'ISOSpeedRatings' in exif_data:
        return exif_data['ISOSpeedRatings']
    return None

def get_exposure_time(exif_data):
    if 'ExposureTime' in exif_data:
        return exif_data['ExposureTime']
    return None

def get_datetime_original(exif_data):
    if 'DateTimeOriginal' in exif_data:
        return exif_data['DateTimeOriginal']
    return None

def convert_to_fraction(value):
    frac = Fraction(value).limit_denominator()
    return str(frac.numerator) + '/' + str(frac.denominator)

def convert_to_date(datetime_original):
    date_time_obj = datetime.strptime(datetime_original, '%Y:%m:%d %H:%M:%S')
    return date_time_obj.strftime("%m/%d/%y")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="path to image file")
    args = parser.parse_args()
    
    
    exif_data = get_exif_data(args.image)
    fnumber = get_fnumber(exif_data)
    focal_length = get_focal_length(exif_data)
    iso = get_iso(exif_data)
    exposure_time = get_exposure_time(exif_data)
    datetime_original = get_datetime_original(exif_data)
    exposure_time_fraction = convert_to_fraction(exposure_time)
    date = convert_to_date(datetime_original)
    
    print('=================================')
    print("Date: ",date)
    print("Location:")
    print("Camera: Nikon D7000")
    print("Lens: ",focal_length)
    print("Filter: N/A")
    print("Aperture: ",fnumber)
    print("Iso: ",iso)
    print("Shutter: ",exposure_time_fraction)
    print('=================================')
