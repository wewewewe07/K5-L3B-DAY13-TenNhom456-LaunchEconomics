# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Văn Anh Trung
Người gắn nhãn 2: Bùi Đình Quý Anh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Do hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Do hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Lỗi ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Do hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Lỗi ngữ cảnh | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Lỗi ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Lỗi ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Do hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Lỗi ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Lỗi ngữ cảnh | Ngầm | Không | Ngầm |
| 18 | Lỗi ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Do hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85% (đạt ngưỡng 80%, không cần viết lại định nghĩa). Người 1 ghi "Do hệ thống", "Lỗi ngữ cảnh", "Lỗi ngầm"; khi so nhãn coi là cùng loại Hệ thống, Ngữ cảnh, Ngầm.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 3 → Ngữ cảnh:** trợ lý hoàn về ví LogiX đúng thiết kế, chỉ giả định "khách biết tiền về ví" không khớp hoàn cảnh; Hệ thống chỉ dùng khi trợ lý làm sai thiết kế hoặc chính sách.
- **Ca 8 → Hệ thống:** dẫn "Điều 7.2" không có trong chính sách hiện hành là sai so với chính sách và nhìn thấy được, dù số tiền đúng; Ngữ cảnh chỉ dùng khi trợ lý làm đúng hoàn toàn.
- **Ca 17 → Ngầm:** dùng bảng giá cũ là sai thật, 212 đơn lệch trong 9 ngày mà không khách nào mở lại; sai mà không ai nhận ra cho tới khi kiểm tra là Ngầm, không phải Ngữ cảnh.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (loại mã, trace_id); cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã đơn sàn TMĐT và tự tra sang mã vận đơn; không tra được thì hướng dẫn tìm mã vận đơn kèm ảnh, không dừng câu trả lời | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có `refund_ledger_write` kết quả ok cùng trace_id; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với lý do "số tiền" mà kiểm tra thấy đúng chính sách, theo tuần; ngưỡng 1% số yêu cầu | Mẫu tin nhắn luôn ghi cách tính, ví dụ "30.000 đ × 50% = 15.000 đ", kèm điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = thieu_du_lieu, đếm theo loại yêu cầu mỗi ngày | Giữ cách chuyển nhân viên kèm tóm tắt; đưa quoc_te ra khỏi phạm vi pilot (thành công 27,3%, 1,88× của 12.000 đ, `simulated`) | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked`: kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace của mỗi lần chạy | Kế toán trưởng |
