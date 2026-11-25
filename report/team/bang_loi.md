# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Văn Anh Trung · Người gắn nhãn 2: Bùi Quý Anh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Do hệ thống | Do hệ thống | Có | Do hệ thống |
| 3 | Do hệ thống | Lỗi ngữ cảnh | Không | Lỗi ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Lỗi ngầm | Lỗi ngầm | Có | Lỗi ngầm |
| 6 | Do người dùng | Do hệ thống | Không | Do người dùng |
| 7 | Do hệ thống | Do hệ thống | Có | Do hệ thống |
| 8 | Lỗi ngữ cảnh | Lỗi ngữ cảnh | Có | Lỗi ngữ cảnh |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Lỗi ngữ cảnh | Lỗi ngữ cảnh | Có | Lỗi ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Lỗi ngầm | Lỗi ngầm | Có | Lỗi ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Do hệ thống | Do hệ thống | Có | Do hệ thống |
| 16 | Lỗi ngữ cảnh | Lỗi ngữ cảnh | Có | Lỗi ngữ cảnh |
| 17 | Lỗi ngữ cảnh | Lỗi ngầm | Không | Lỗi ngầm |
| 18 | Lỗi ngữ cảnh | Lỗi ngữ cảnh | Có | Lỗi ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Do hệ thống | Do hệ thống | Có | Do hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 3 — Do hệ thống vs Lỗi ngữ cảnh:** Trợ lý tự động hoàn tiền và hủy đơn đúng theo logic kỹ thuật nhưng khách chỉ muốn đổi thời gian giao chứ không muốn hủy, giả định của hệ thống không khớp với ngữ cảnh mong muốn của khách nên nhãn thống nhất là **Lỗi ngữ cảnh**.
- **Ca 6 — Do người dùng vs Do hệ thống:** Nguyên nhân gốc khởi phát là khách chọn sai danh mục ("Hoàn phí giao trễ" cho trường hợp hàng vỡ hỏng), nên nhãn thống nhất là **Do người dùng**; việc hệ thống chưa biết gợi ý chuyển luồng xử lý khiếu nại thuộc về giải pháp ở cột khắc phục.
- **Ca 17 — Lỗi ngữ cảnh vs Lỗi ngầm:** Lỗi áp dụng bảng giá cũ không được khách hàng hay nhân viên nhận ra vì câu trả lời vẫn hiển thị hoàn chỉnh, chỉ được phát hiện khi kế toán đối soát mẫu định kỳ, nên nhãn thống nhất là **Lỗi ngầm**.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` gắn `trace_id`; cảnh báo tự động khi vượt ngưỡng 2% tổng số yêu cầu/ngày | Thêm bước regex nhận diện định dạng mã đơn sàn TMĐT để tự động tra sang mã vận đơn LogiX; nếu không khớp thì hiển thị ảnh hướng dẫn vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Do hệ thống | Job đối soát mỗi giờ giữa event tin nhắn báo "đã hoàn" và event `refund_ledger_write` có `ket_qua == 'ok'` cùng `trace_id`; ngưỡng cảnh báo: ≥ 1 ca lệch | Chỉ gửi thông báo "đã hoàn" khi dịch vụ sổ cái trả về mã thành công cùng `idempotency_key`; nếu API lỗi 503 sau 3 lần thử thì báo "đang xử lý" và bắn `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Lỗi ngữ cảnh | Thống kê hằng tuần tỉ lệ event `ticket_reopened` có `reason == 'thac_mac_so_tien'` trên các đơn kiểm tra lại thấy tính đúng chính sách; ngưỡng > 1%/tuần | Cập nhật template phản hồi bắt buộc hiển thị công thức tính chi tiết (ví dụ: Phí giao 30.000 đ × Mức hoàn trễ 24–48h 50% = 15.000 đ) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi hằng ngày tỉ lệ event `handoff_to_staff` có `reason == 'thieu_du_lieu_chang_ngoai'` theo từng `loai` yêu cầu; ngưỡng > 5% ở nhóm ngoài phạm vi | Loại hoàn toàn đơn `quoc_te` khỏi phạm vi chạy trợ lý ngay ở bước định tuyến đầu vào; với đơn phát sinh chặng đối tác thì chuyển thẳng nhân viên kèm bản tóm tắt | PM trợ lý hoàn phí |
| 17 | Lỗi ngầm | Event `audit_sample_checked` do kế toán kiểm tra mẫu ngẫu nhiên 100 đơn/tuần đối chiếu với bảng giá hiện hành; ngưỡng cảnh báo khi > 1% số đơn kiểm tra bị lệch tiền | Tự động xóa cache bảng giá (cache invalidation) ngay khi có sự kiện cập nhật bảng giá mới và ghi bắt buộc `pricing_version` vào mọi `trace_id` | Kế toán trưởng |
