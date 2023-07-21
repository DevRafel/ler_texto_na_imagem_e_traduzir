# Para install (pip install opencv-python)
# Para install (pip install pytesseract)

import pytesseract
import cv2
from translate import Translator
import translate

# passo 1 : ler a imagem

imagem = cv2.imread("print11.png")

caminho = r"C:\Program Files\Tesseract-OCR"
# passo 2 : pedir pro tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(imagem)

s = Translator(from_lang="english", to_lang="pt-br")

res = s.translate(texto)

print(texto)
print(f"Tradução: {res}")
