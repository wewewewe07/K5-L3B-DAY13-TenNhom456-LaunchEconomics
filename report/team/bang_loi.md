# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Văn Anh Trung · Người gắn nhãn 2: Bùi Quý Anh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Hệ thống | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6 — Do người dùng vs Hệ thống:** Nguyên nhân gốc khởi phát là khách chọn sai danh mục ("Hoàn phí giao trễ" cho trường hợp hàng vỡ hỏng), nên gắn nhãn **Do người dùng**; việc trợ lý chưa biết gợi ý chuyển luồng khiếu nại thuộc về giải pháp khắc phục.
- **Ca 8 — Hệ thống vs Ngầm:** Lỗi trích dẫn điều khoản 7.2 không tồn tại hiển thị rõ ngay trên câu trả lời và nhân viên soát xét phát hiện được ngay, nên là lỗi **Hệ thống**; lỗi **Ngầm** chỉ dùng cho các ca mà cả khách lẫn hệ thống đều không nhận ra cho tới khi đối soát định kỳ (như Ca 5, 12, 17).
- **Ca 13 — Giới hạn hệ thống vs Hệ thống:** Yêu cầu hoàn phí bảo hiểm của đối tác vận tải ngoài phạm vi dữ liệu và quyền hạn của trợ lý nên nguyên nhân gốc là **Giới hạn hệ thống**, dù cách trợ lý phản hồi chung chung khi gặp giới hạn cần được cải thiện.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` gắn `trace_id`; cảnh báo tự động khi vượt ngưỡng 2% tổng số yêu cầu/ngày | Thêm bước regex nhận diện định dạng mã đơn sàn TMĐT để tự động tra sang mã vận đơn LogiX; nếu không khớp thì hiển thị ảnh hướng dẫn vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Job đối soát mỗi giờ giữa event tin nhắn báo "đã hoàn" và event `refund_ledger_write` có `ket_qua == 'ok'` cùng `trace_id`; ngưỡng cảnh báo: ≥ 1 ca lệch | Chỉ gửi thông báo "đã hoàn" khi dịch vụ sổ cái trả về mã thành công cùng `idempotency_key`; nếu API lỗi 503 sau 3 lần thử thì báo "đang xử lý" và bắn `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Thống kê hằng tuần tỉ lệ event `ticket_reopened` có `reason == 'thac_mac_so_tien'` trên các đơn kiểm tra lại thấy tính đúng chính sách; ngưỡng > 1%/tuần | Cập nhật template phản hồi bắt buộc hiển thị công thức tính chi tiết (ví dụ: Phí giao 30.000 đ × Mức hoàn trễ 24–48h 50% = 15.000 đ) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi hằng ngày tỉ lệ event `handoff_to_staff` có `reason == 'thieu_du_lieu_chang_ngoai'` theo từng `loai` yêu cầu; ngưỡng > 5% ở nhóm ngoài phạm vi | Loại hoàn toàn đơn `quoc_te` khỏi phạm vi chạy trợ lý ngay ở bước định tuyến đầu vào; với đơn phát sinh chặng đối tác thì chuyển thẳng nhân viên kèm bản tóm tắt | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` do kế toán kiểm tra mẫu ngẫu nhiên 100 đơn/tuần đối chiếu với bảng giá hiện hành; ngưỡng cảnh báo khi > 1% số đơn kiểm tra bị lệch tiền | Tự động xóa cache bảng giá (cache invalidation) ngay khi có sự kiện cập nhật bảng giá mới và ghi bắt buộc `pricing_version` vào mọi `trace_id` | Kế toán trưởng |
