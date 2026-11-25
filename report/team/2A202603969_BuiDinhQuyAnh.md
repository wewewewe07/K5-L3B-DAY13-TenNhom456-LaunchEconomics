# Báo cáo cá nhân — BuiDinhQuyAnh-2A202603969

## 1. Thông tin thành viên

- Họ tên: Bùi Đình Quý Anh
- MSSV: 2A202603969
- Email: buiquyanh8@gmail.com
- Vai trong nhóm: người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- CP3 (nhiệm vụ C): gắn nhãn độc lập 20 ca lỗi, so nhãn với người gắn nhãn 1 và ghi quy tắc cho các ca không trùng.
- CP4 (nhiệm vụ D): hoàn thiện `report/team/pilot_plan.yaml` từ kết quả D1 của nhóm.
- CP5 (nhiệm vụ E): giữ hồ sơ `report/team/ho_so_launch_v0.md`; ghi phiếu chấm duyệt chéo `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- **Bảng lỗi:** gắn 20 ca theo năm loại của Google PAIR, theo nguyên nhân gốc. So với người 1 trùng 17/20 = 85% (đạt ngưỡng 80%). Ba ca lệch là ca 3, 8, 17. Nhãn thống nhất: ca 3 Ngữ cảnh, ca 8 Hệ thống, ca 17 Ngầm, mỗi ca có một câu quy tắc phân biệt.
- **pilot_plan.yaml:** chọn chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot. Nhóm chấp nhận mde 0,06 (n = 859/nhóm, DE 6,96, ≥ 299 yêu cầu/người) và ghi rõ con số bất lợi: power 0,64 nếu tác động thật chỉ 5 điểm. Trả lời năm câu D2. Viết ba luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ (an toàn, chi phí, mức sử dụng), cùng rollback 30 phút, ngày quyết định và danh sách số `simulated`.
- **Ngưỡng an toàn:** tính tỉ lệ `mo_lai_trong_7_ngay` từ CSV trước khi đặt ngưỡng: 51/1.200 = 4,25%, trong phạm vi noi_dia + hang_nang là 39/982 = 3,97%. Ngưỡng tuyệt đối 3% sẽ làm pilot dừng ngay tuần đầu, nên luật an toàn so với nhóm đối chứng (+2 điểm) kèm trần 6%.
- **Hồ sơ launch v0:** gom số của A–E vào bảy mục, mỗi mục có con số chính, trạng thái và một vai trò phụ trách. Đề xuất **Go có điều kiện** cho noi_dia + hang_nang, kèm bốn điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra.
- **Phiếu chấm:** chuẩn bị khung phiếu, các điểm chuẩn để đối chiếu và ba câu hỏi định lượng cho đội được chấm.

## 4. Bằng chứng

- `report/team/bang_loi.md`: cột "Nhãn người 2", cột thống nhất, tỉ lệ đồng thuận 17/20 = 85% và quy tắc cho ca 3, 8, 17.
- `report/team/pilot_plan.yaml`: đọc được bằng `yaml.safe_load`, đủ 11 trường, 3 luật dừng, không còn dấu `?` ngoài chú thích.
- `report/team/ho_so_launch_v0.md`: đủ 7 mục và dòng đề xuất cuối trang.
- `report/team/phieu_cham.md`: phiếu chấm nhóm n + 1.
- Con số tự tính từ `src/logix_requests.csv`: mở lại 7 ngày 4,25% (toàn mẫu) và 3,97% (phạm vi pilot); tỉ lệ làm lại trong phạm vi 48/982 = 4,9%; power ở n = 859 với mức chênh 5 điểm là 0,641.

## 5. Công cụ AI đã dùng

- Claude Code: soạn nháp `pilot_plan.yaml`, `ho_so_launch_v0.md`, `chi_so.md`, `group_report.md` và khung `phieu_cham.md` từ số do `src/lab13.py` tính ra; chạy kiểm tra `yaml.safe_load` và kiểm tra không còn dấu `?`.
- Tự kiểm tra: chạy lại `lab13.py`, đối chiếu số trong hồ sơ với `bang_chi_phi.md`, chỉnh lại nội dung trước khi nộp. Nhãn người 2 ở nhiệm vụ C có dùng Claude Code hỗ trợ gắn.

## 6. Tự đánh giá

- Làm tốt: hồ sơ nêu cả con số bất lợi (power 0,64, quoc_te 1,88×, xem lại 100% là 0,98–1,03×) kèm cách xử lý; mọi số giả lập có nhãn `simulated`.
- Cần cải thiện: điểm phiếu chấm chỉ điền được sau khi đọc hồ sơ nhóm bạn tại buổi; mục 4 và 5 của hồ sơ phụ thuộc vào danh sách event trong `chi_so.md` và bảng khắc phục 5 ca, phải đối chiếu lại khi hai phần đó xong.
