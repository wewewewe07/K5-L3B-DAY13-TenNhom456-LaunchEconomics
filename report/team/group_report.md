# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: TenNhom456
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có mở pilot hay không. Nhóm trả lời bốn câu hỏi: có đáng chạy không (chi phí mỗi việc thành công), nhân viên có dùng không (chỉ số và event), khi hỏng thì sao (bảng lỗi), và pilot thiết kế thế nào để ra được quyết định (đối chứng, cỡ mẫu, luật dừng). Mọi số tính từ hai cột `_simulated` đều ghi nhãn `simulated`.

## 3. Giải pháp

- **A, B · Chi phí và độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md), `src/lab13.py`): tử số tính mọi lần chạy kể cả lần lỗi, cộng giờ xem lại và làm lại; mẫu số chỉ đếm việc thành công. Tách theo bốn loại yêu cầu, cộng chi phí cố định, chạy 9 kịch bản đổi từng yếu tố, một cặp, giới hạn số lần chạy và xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo năm loại Google PAIR, so nhãn, thống nhất ca lệch, chọn 5 ca (mỗi loại một ca) để ghi cách phát hiện đo được và vai trò phụ trách.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính đủ năm câu D1 rồi mới chọn chia theo nhân viên 20 + 20; trả lời năm câu D2; đặt ba luật dừng sau khi xem tỉ lệ mở lại hiện tại.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): tính thử ba chỉ số, thêm hai chỉ số tự đề xuất, 10 event có `trace_id`, ba dòng rủi ro kinh tế, ghép thành hồ sơ một trang.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** (`simulated`), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu (274,7 đ); 92,5% là giờ nhân viên (`simulated`).
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương (+23,1% khi tăng 25%) (`simulated`).
- Phạm vi noi_dia + hang_nang kể cả cố định: **0,38×** của 12.000 đ (`simulated`). quoc_te **1,88×** (thành công 27,3%) bị loại khỏi pilot. Xem lại 100% đẩy chi phí lên **0,98–1,03×** (`simulated`).
- Bảng lỗi: đồng thuận **17/20 = 85%**.
- Pilot: chia theo nhân viên 20 + 20, mde 0,06, 859 yêu cầu/nhóm, DE 6,96. Con số bất lợi: power chỉ **0,64** nếu tác động thật là 5 điểm.
- Chỉ số trong đợt chạy thử là 82,83% (chính), 27,12% (bỏ qua gợi ý), 4,25% (mở lại 7 ngày).
- Đề xuất của `ho_so_launch_v0.md`: **Go có điều kiện** cho pilot noi_dia + hang_nang.

## 5. Khó khăn và cách xử lý

- Với 40 nhân viên, không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm (tối đa 1.000 < 1.251). Nhóm chấp nhận mức chênh 6 điểm, ghi rõ power 0,64 và đưa việc ký chấp nhận thành điều kiện Go.
- Tỉ lệ mở lại hiện tại là 4,25% (3,97% trong phạm vi), nên ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu. Luật an toàn so với nhóm đối chứng (+2 điểm), kèm trần 6%.
- Ba ca lệch nhãn (3, 8, 17) giữa hai người gắn nhãn đều là ranh giới Hệ thống / Ngữ cảnh / Ngầm. Nhóm viết quy tắc phân biệt theo nguyên nhân gốc.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; tuần 1 của pilot phải đo phút thật qua event `staff_review_decision` và `staff_rework_completed`.
- Đợt chạy thử không có đối chứng, nên chưa nói được trợ lý nâng chỉ số chính.
- Cần sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `NormalIndPower`.
- `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
