import cv2

def compare_images(image1_path, image2_path, output_path):
    image1 = cv2.imread(image1_path)  # 改修前の画像
    image2 = cv2.imread(image2_path)  # 改修後の画像
    
    if image1 is None or image2 is None:
        print("Error: Could not read one or both of the images.")
        return
    
    diff = cv2.absdiff(image1, image2)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    #_, thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(gray_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    image2_diff = image2.copy()  # 改修後の画像に短形の印をつける画像
    for contour in contours:  # 改修後の画像に短形の印をつける
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image2_diff, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imwrite(output_path, image2_diff)  # 短形が追加された改修後の画像を保存