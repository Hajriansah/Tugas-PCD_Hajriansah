# Nama  : Juan Sebastian Caesario Bawias
# NIM   : F55121077
# Kelas : B
import cv2

gambar = cv2.imread('img7.jpg')
abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

median_3x3 = cv2.medianBlur(abu, 3)
median_5x5 = cv2.medianBlur(abu, 5)
median_9x9 = cv2.medianBlur(abu, 9)

# menampilkan gambar asli dan hasil median filter
cv2.imshow('Original Image', abu)
cv2.imshow('Median Filter 3x3', median_3x3)
cv2.imshow('Median Filter 5x5', median_5x5)
cv2.imshow('Median Filter 9x9', median_9x9)
# menunggu tombol keyboard ditekan
cv2.waitKey(0)

# menutup semua jendela
cv2.destroyAllWindows()
