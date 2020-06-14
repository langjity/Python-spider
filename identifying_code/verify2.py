import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr



print(tesserocr.file_to_text('a.png'))