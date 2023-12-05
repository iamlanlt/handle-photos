import cv2

def classify_product_height(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)
    
    # Chuyển ảnh sang ảnh xám
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Làm mịn ảnh để giảm nhiễu
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Phân ngưỡng để tạo ảnh nhị phân
    _, threshold = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
    
    # Tìm contours trong ảnh
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Tính toán hình dạng xấp xỉ của contour
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        
        # Tính toán kích thước của bounding box
        x, y, width, height = cv2.boundingRect(contour)
        
        # Xác định chiều cao của vật thể
        object_height = height  # Hoặc có thể tính toán chiều cao dựa trên ảnh so với khoảng cách camera
        
        # Phân loại vật thể dựa trên chiều cao
        if object_height <= 600:
            print("Loại sản phẩm A: " + str(object_height))
        elif 600 < object_height <= 800:
            print("Loại sản phẩm B: " + str(object_height))
        else:
            print("Loại sản phẩm C: " + str(object_height))
    
    # Hiển thị ảnh và contours (để kiểm tra)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Image with Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Gọi hàm với đường dẫn ảnh
classify_product_height('testA.jpg')
classify_product_height('testB.jpg')
classify_product_height('testC.jpg')
