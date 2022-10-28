import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img = cv2.imread("1.jpg")
cv2.imshow("img", img)
text = pytesseract.image_to_string(img, config=config, lang="amh")
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()