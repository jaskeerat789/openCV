import cv2
import numpy as np
import matplotlib.pyplot as plt 
def make_coordinate(image,line_parameters):
	slope,intercept=line_parameters
	y1=image.shape[0]
	y2=int(y1*(3/5))

	return
def averaged_slope_intercept(image,lines):
	left_fit=[]
	right_fit=[]
	for line in lines:
		x1,y1,x2,y2=line.reshape(4)
		parameters=np.polyfit((x1,y2),(x2,y2),1)
		slope=parameter[0]
		intercept=parameterp[1]
		if slope<0:
			left_fit.append((slope,intercept))
		else:
			right_fit.append((slope,intercept))
	left_fit_average=np.average(left_fit,axis=0)
	right_fit_average=np.average(right_fit,axis=0)
	left_line=make_coordinate(image,left_fit_average)
	rigth_line=make_coordinate(image,right_fit_average)


def canny(image):
	gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
	blur=cv2.GaussianBlur(gray,(5,5),0)
	canny=cv2.Canny(blur,50,150)
	return canny

def display_lines(image,lines):
	line_image=np.zeros_like(image)
	if lines is not None:
		for line in lines:

			 x1,y1,x2,y2=line.reshape(4)
			 cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
	return line_image
 


def region_of_interest(image):
	height=image.shape[0]
	polygons=np.array([
	[(200,height ),(1100,height),(500,250)]
	])
	mask=np.zeros_like(image)
	cv2.fillPoly(mask,polygons,255)
	masked_image=cv2.bitwise_and(image,mask) 
	return masked_image

image=cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny_image=canny(lane_image)
cropped_image = region_of_interest(canny_image) 
lines=cv2.HoughLinesP(cropped_image,2,np.pi/100, 100,np.array([]),minLineLength=40,maxLineGap=5)
averaged_lines=averaged_slope_intercept(lane_image,averaged_lines)
line_image=display_lines(lane_image,lines)
combo_image=cv2.addWeighted(lane_image,0.8,line_image,1,1)
cv2.imshow("result",combo_image)
cv2.waitKey(0)

# plt.imshow(canny)
# plt.show()

