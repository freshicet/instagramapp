# Instagram App/Metadata

This code uses the Python Imaging Library (PIL) to extract Exif data from an image file and prints the following:

- DateTimeOriginal in the format of "mm/dd/yy"
- Location (Not implemented in code)
- Camera: Nikon D7000
- Lens (FocalLength)
- Filter (Not implemented in code)
- Aperture (FNumber)
- Iso (ISOSpeedRatings)
- Shutter (ExposureTime)

The code also converts the ExposureTime to a fraction format (e.g 1/800 sec) and prints it.

#

## Usage

To run the script, make sure you have PIL, fractions and datetime modules installed.

```bash
python script.py path/to/image.jpg
```

This will call the script and pass the path to the image file as an argument. The script will then open the image file, read its EXIF data, and print the Date, Location, Camera, Lens, Filter, Aperture, ISO, and Shutter.

Please note that above code snippet assumes that the value of ExposureTime is in seconds and the value of DateTimeOriginal is in the format of '%Y:%m:%d %H:%M:%S' If the format is different, you will have to adjust the format string passed to convert_to_date function.

This is just a basic example of how you can use the PIL library to extract Exif data from an image file and use it in your application. You can expand on this code to add more features or to extract additional information from the image file.

#

## Output

```python
=================================
Location:
Date:  12/17/22
Camera: Nikon D7000
Lens:  50.0
Filter: N/A
Aperture:  1.4
Iso:  100
Shutter:  10/8000
=================================
```
