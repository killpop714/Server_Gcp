import qrcode

# 링크 설정
url = "http://35.224.83.108:5000"

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,  # QR 코드 크기 (1 ~ 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 정정 수준
    box_size=10,  # 각 박스 크기
    border=4,  # 테두리 두께
)
qr.add_data(url)
qr.make(fit=True)

# 이미지로 변환
img = qr.make_image(fill_color="black", back_color="white")

# 파일로 저장
img.save("qr_code.png")