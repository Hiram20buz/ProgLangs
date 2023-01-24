import cv2
img=cv2.imread("mr.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

x_edges=cv2.Sobel(gray,-1,1,0,ksize=5)
cv2.imwrite("x.jpg",x_edges)

y_edges=cv2.Sobel(gray,-1,0,1,ksize=5)
cv2.imwrite("y.jpg",y_edges)

cv2.imshow("x",x_edges)
cv2.imshow("y",y_edges)

#dsize=(500,500)
#output=cv2.resize(img,dsize)
#output1=cv2.resize(edges,dsize)
#cv2.imshow("Original",output)
#cv2.imshow("Filtro",output1)
cv2.waitKey(0)
cv2.destroyAllWindows()
