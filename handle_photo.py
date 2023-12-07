import cv2

def classify_product_dimensions(image_path):
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
        
        # Xác định chiều dài, rộng và cao của vật thể
        object_width = width
        object_height = height
        object_depth = min(object_width, object_height)
        
        # Phân loại vật thể dựa trên chiều dài, rộng và cao
        if object_depth <= 600:
            print("Loại sản phẩm A: " + str(object_width) + " x " + str(object_height) + " x " + str(object_depth))
        elif 600 < object_depth <= 800:
            print("Loại sản phẩm B: " + str(object_width) + " x " + str(object_height) + " x " + str(object_depth))
        else:
            print("Loại sản phẩm C: " + str(object_width) + " x " + str(object_height) + " x " + str(object_depth))
    
    # Hiển thị ảnh và contours (để kiểm tra)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Image with Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Gọi hàm với đường dẫn ảnh
classify_product_dimensions('testA.jpg')
classify_product_dimensions('testB.jpg')
classify_product_dimensions('testC.jpg')
