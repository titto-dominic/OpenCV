import cv2 as cv 

cv::Mat image = cv::imread("lena.jpg");

// SetImageRoi
cv::Rect roi(100, 100, 280, 80);
cv::Mat image_roi = image(roi);

//show the result
imshow("src",image);
imshow("roi",image_roi);
waitKey();