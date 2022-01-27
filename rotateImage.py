from importlib.resources import path
import pathlib
from PIL import Image

def rotateImage(fileIn : str | pathlib.Path, fileOut : str | pathlib.Path, angle : float) -> None:
    filePathIn = pathlib.Path(fileIn)
    filePathOut = pathlib.Path(fileOut)
    image = Image.open(filePathIn)
    rotatedImage = image.rotate(angle)
    rotatedImage.save(filePathOut)
