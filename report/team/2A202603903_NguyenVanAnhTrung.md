# Báo cáo cá nhân — Nguyễn Văn Anh Trung · 2A202603903

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Anh Trung
- MSSV: 2A202603903
- Email:
- Vai trong nhóm: Người gắn nhãn 1 (chính ở CP3: Nhiệm vụ C); đọc đề, theo dõi điều kiện "Xong khi" của các checkpoint; tham gia CP5 (Nhiệm vụ E).

## 2. Phần việc phụ trách

- **Xuyên suốt buổi (CP1 → CP5):** đọc đề, theo dõi điều kiện "Xong khi" / "Tự kiểm tra" của từng checkpoint trước khi nhóm chuyển sang nhiệm vụ tiếp theo.
- **CP3 · Nhiệm vụ C (chính):** gắn nhãn độc lập 20 ca lỗi theo 5 loại của Google PAIR; cùng Người gắn nhãn 2 tính tỉ lệ đồng thuận, thống nhất nhãn, viết quy tắc phân biệt và bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- **CP5 · Nhiệm vụ E (phối hợp):** tham gia đặc tả danh sách event có `trace_id` và các dòng rủi ro kinh tế trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

### CP3 · Gắn nhãn độc lập 20 ca lỗi

- Gắn nhãn cả 20 ca trong 8 phút, ngồi tách và không trao đổi với Người gắn nhãn 2, theo nguyên tắc gắn nhãn theo **nguyên nhân gốc**, không theo chỗ cần sửa.
- Phân bố bộ nhãn 1:

| Loại (Google PAIR) | Các ca | Số ca |
| --- | --- | --: |
| Do người dùng | 1, 6, 9, 11, 14 | 5 |
| Hệ thống | 2, 3, 7, 15, 20 | 5 |
| Ngữ cảnh | 8, 10, 16, 17, 18 | 5 |
| Giới hạn hệ thống | 4, 13, 19 | 3 |
| Ngầm | 5, 12 | 2 |
| **Tổng** | | **20** |



## 4. Bằng chứng

- File: `report/team/bang_loi.md`, cột "Nhãn người 1" (20/20 ca đã gắn nhãn).
- Commit: `b24f757` (_Cập nhật checkpoint 3_) trên nhánh `NguyenVanAnhTrung`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (Claude Opus 5.5).
- **Mục đích:** tổng hợp nhiệm vụ của vai Người gắn nhãn 1 qua từng checkpoint từ `TEAM.md`, `CHECKPOINTS.md` và hướng dẫn chi tiết; soạn khung báo cáo cá nhân này.
- **Không dùng AI để gắn nhãn:** 20 nhãn ở CP3 do tự gắn độc lập, đúng yêu cầu không trao đổi.
- **Cách tự kiểm tra:** đối chiếu danh sách điều kiện "Xong khi" với nguyên văn `CHECKPOINTS.md` và `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; đếm lại phân bố nhãn trực tiếp từ `bang_loi.md`.

## 6. Tự đánh giá

- Đã hoàn thành: bộ nhãn độc lập 20/20 ca ở CP3; theo dõi điều kiện "Xong khi" của các checkpoint.
- Chưa hoàn thành tại thời điểm viết: tỉ lệ đồng thuận và quy tắc phân biệt (chờ bộ nhãn 2), bảng khắc phục 5 ca, phần event và rủi ro trong `chi_so.md`.
- Điều rút ra: gắn nhãn theo nguyên nhân gốc giúp phân biệt "Ngầm" với "Hệ thống": lỗi ngầm là lỗi không ai nhận ra cho tới khi kiểm tra, còn lỗi hệ thống đã lộ ra.
- Mức độ hoàn thành đề xuất: 7/10, vì một số ngữ cảnh không được đọc kĩ để tìm đúng dấu hiệu để phân loại đúng lỗi.
