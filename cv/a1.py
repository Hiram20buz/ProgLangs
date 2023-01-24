import cv2
img=cv2.imread("mr.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,100,200,3)
cv2.imwrite("canny_edges.jpg",edges)
#cv2.imshow("canny_edges",edges)

dsize=(500,500)
output=cv2.resize(img,dsize)
output1=cv2.resize(edges,dsize)
cv2.imshow("Original",output)
cv2.imshow("Filtro",output1)
cv2.waitKey(0)
cv2.destroyAllWindows()
