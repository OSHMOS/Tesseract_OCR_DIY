import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

good = Image.open('중독.png')
result = pytesseract.image_to_string(good, lang='kor')
print(result)
