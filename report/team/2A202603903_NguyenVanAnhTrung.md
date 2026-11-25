# Báo cáo cá nhân — Nguyễn Văn Anh Trung · 2A202603903

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Anh Trung
- MSSV: 2A202603903
- Email:
- Vai trong nhóm: Người gắn nhãn 1 (chính ở CP3: Nhiệm vụ C); đọc đề, theo dõi điều kiện "Xong khi" của các checkpoint; tham gia CP5 (Nhiệm vụ E).

## 2. Phần việc phụ trách

- **Xuyên suốt buổi (CP1 → CP5):** đọc đề, theo dõi điều kiện "Xong khi" / "Tự kiểm tra" của từng checkpoint trước khi nhóm chuyển sang nhiệm vụ tiếp theo.
- **CP3 · Nhiệm vụ C (chính):** gắn nhãn độc lập 20 ca lỗi theo 5 loại của Google PAIR; cùng Người gắn nhãn 2 đối chiếu, tính tỉ lệ đồng thuận, thống nhất nhãn, viết quy tắc phân biệt và bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- **CP5 · Nhiệm vụ E (phối hợp):** tham gia đặc tả danh sách event có `trace_id` và các dòng rủi ro kinh tế trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

### CP3 · Bộ nhãn 1 (làm độc lập)

- Gắn nhãn cả 20 ca trong 8 phút, ngồi tách và không trao đổi với Người gắn nhãn 2, theo nguyên tắc gắn nhãn theo **nguyên nhân gốc**, không theo chỗ cần sửa.
- Phân bố bộ nhãn 1:

| Loại (Google PAIR) | Các ca | Số ca |
| --- | --- | --: |
| Do người dùng | 1, 6, 9, 14 | 4 |
| Hệ thống | 2, 3, 7, 15, 20 | 5 |
| Ngữ cảnh | 8, 10, 16, 17, 18 | 5 |
| Giới hạn hệ thống | 4, 11, 13, 19 | 4 |
| Ngầm | 5, 12 | 2 |
| **Tổng** | | **20** |

### CP3 · Đối chiếu với bộ nhãn 2 (Bùi Quý Anh)

- Trùng 17/20 ca, **tỉ lệ đồng thuận 85%** (≥ 80%, không phải viết lại định nghĩa).
- Ba ca không trùng và nhãn thống nhất:

| Ca | Nhãn người 1 | Nhãn người 2 | Nhãn thống nhất | Lý do (tóm tắt quy tắc phân biệt) |
| --: | --- | --- | --- | --- |
| 3 | Hệ thống | Ngữ cảnh | Ngữ cảnh | Agent chạy đúng logic nhưng giả định "hủy đơn" không khớp ý khách chỉ muốn đổi giờ giao. |
| 6 | Do người dùng | Hệ thống | Do người dùng | Nguyên nhân khởi phát là khách chọn sai danh mục; việc hệ thống chưa gợi ý chuyển luồng thuộc cột khắc phục. |
| 17 | Ngữ cảnh | Ngầm | Ngầm | Áp bảng giá cũ, câu trả lời trông hoàn chỉnh nên không ai nhận ra, chỉ lộ khi kế toán đối soát mẫu. |

- Phân bố sau thống nhất: Do người dùng 4 · Hệ thống 4 · Ngữ cảnh 5 · Giới hạn hệ thống 4 · Ngầm 3.
- Bảng khắc phục chọn mỗi loại một ca: 9 (Do người dùng), 7 (Hệ thống), 18 (Ngữ cảnh), 4 (Giới hạn hệ thống), 17 (Ngầm); mỗi dòng có event, ngưỡng đo và vai trò phụ trách cụ thể.

### CP5 · Nhiệm vụ E

- Phối hợp đặc tả 10 event có `trace_id` (từ `refund_request_created` đến `audit_sample_checked`) và phần kiểm tra chéo chỉ số ↔ event trong `chi_so.md`. Các event `ticket_reopened`, `refund_ledger_write`, `audit_sample_checked` được dùng lại làm cách phát hiện trong bảng khắc phục ở `bang_loi.md`, để hai file khớp nhau.

## 4. Bằng chứng

- File `report/team/bang_loi.md`: cột "Nhãn người 1" (20/20 ca), tỉ lệ đồng thuận 17/20 = 85%, quy tắc phân biệt ca 3, 6, 17, bảng khắc phục 5 ca.
- File `report/team/chi_so.md`: danh sách 10 event có `trace_id`, kiểm tra chéo 5 chỉ số, 3 dòng rủi ro kinh tế E2.
- Commit của mình trên nhánh `NguyenVanAnhTrung`, đã merge vào `main` qua Pull Request #1 (`7b569c9`):
  - `b24f757` (_Cập nhật checkpoint 3_): gắn nhãn 20 ca ở cột "Nhãn người 1".
  - `df640b2` (_Cập nhật báo cáo cá nhân_): tạo báo cáo cá nhân này.
  - `f64f157` (_Update bảng lỗi - checkpoint 3_): chỉnh nhãn ca 11 sang Giới hạn hệ thống.
- Commit tổng hợp của nhóm trên nhánh `test` (do Nguyễn Thanh Tùng đẩy lên): `5863349` hoàn thiện `bang_loi.md`, `chi_so.md`; `8705cd3` đồng bộ lại cột "Nhãn người 1" cho khớp đúng bộ nhãn trên nhánh `NguyenVanAnhTrung`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Claude Opus 5.5).
- **Mục đích:** tổng hợp nhiệm vụ của vai Người gắn nhãn 1 qua từng checkpoint từ `TEAM.md`, `CHECKPOINTS.md` và hướng dẫn chi tiết; soạn và cập nhật báo cáo cá nhân này theo nội dung các file nhóm.
- **Không dùng AI để gắn nhãn:** 20 nhãn ở CP3 do tự gắn độc lập, đúng yêu cầu không trao đổi.
- **Cách tự kiểm tra:** đối chiếu danh sách điều kiện "Xong khi" với nguyên văn `CHECKPOINTS.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; đếm lại phân bố nhãn và số ca trùng trực tiếp từ `bang_loi.md`; kiểm tra mỗi event dùng trong bảng khắc phục đều có trong danh sách event của `chi_so.md`.

## 6. Tự đánh giá

- Đã hoàn thành: bộ nhãn độc lập 20/20 ca; đối chiếu đạt đồng thuận 85%; quy tắc phân biệt cho 3 ca không trùng; bảng khắc phục 5 ca có event và ngưỡng đo; phối hợp danh sách event và rủi ro kinh tế trong `chi_so.md`; theo dõi điều kiện "Xong khi" của các checkpoint.
- Chưa tốt: bộ nhãn 1 lệch ở ca 3 và ca 17 do gắn theo chỗ lỗi lộ ra thay vì nguyên nhân gốc; phần tổng hợp cuối được đẩy lên qua nhánh `test` của người khác nên commit của mình chỉ thể hiện phần CP3.
- Điều rút ra: gắn nhãn theo nguyên nhân gốc giúp phân biệt "Ngầm" với "Ngữ cảnh"/"Hệ thống": lỗi ngầm là lỗi không ai nhận ra cho tới khi kiểm tra (ca 17), còn lỗi hệ thống hay ngữ cảnh đã lộ ra với khách hoặc nhân viên.
- Mức độ hoàn thành đề xuất: 8/10.
