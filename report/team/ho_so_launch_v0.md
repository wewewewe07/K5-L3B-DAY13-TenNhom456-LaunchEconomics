# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: TenNhom456 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc (4.373.585 đ ÷ 978, `simulated`), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); 92,5% là giờ nhân viên xem lại và làm lại (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại gấp đôi +51,8% (6.787 đ) · tỉ lệ xem lại gấp đôi +40,7% (6.292 đ) · lương +25% thì +23,1% (5.506 đ); giá token gấp đôi chỉ +5,6% (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Phạm vi noi_dia + hang_nang cộng cố định 40 triệu đ/tháng: 4.599 đ = 0,38× của 12.000 đ (một nửa khối lượng: 0,48×); hòa vốn 4.659 việc thành công/tháng. Bất lợi: quoc_te 1,88×; xem lại 100% là 0,98–1,03× (`simulated`) | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử là 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200); chưa có đối chứng nên chưa nói được tác động | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 17/20 = 85%; 5 Hệ thống, 4 Do người dùng, 4 Ngữ cảnh, 4 Giới hạn, 3 Ngầm; ca 7 (báo "đã hoàn" khi sổ cái lỗi 503) và ca 20 (hoàn trùng) phải sửa trước pilot | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; mde 0,06, n = 859/nhóm, DE 6,96, ≥ 299 yêu cầu/người; power chỉ 0,64 nếu tác động thật là 5 điểm; 3 luật dừng, rollback 30 phút, quyết định 2027-01-12 | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ (+51,8%); xem lại 100% kéo dài: 11.743–12.415 đ = 0,98–1,03×; khối lượng còn một nửa: +2.370 đ/việc tiền cố định (`simulated`) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho pilot chỉ noi_dia + hang_nang, chia theo nhân viên 20 + 20, bắt đầu 2026-12-07, quyết định 2027-01-12. Không đưa quoc_te (1,88×, `simulated`) và doi_tac vào pilot.

- Sửa khoá chống trùng khi ghi hoàn tiền và chỉ báo "đã hoàn" khi sổ cái trả ok (ca 7, 20); kiểm thử 0 ca lọt. Phụ trách: Kỹ sư trưởng agent · kiểm tra 2026-12-04.
- Ký chấp nhận mức chênh tối thiểu 6 điểm (power 0,64 nếu tác động thật chỉ 5 điểm). Phụ trách: Giám đốc vận hành · kiểm tra 2026-12-04.
- Bật đủ event có `trace_id` (danh sách trong `chi_so.md`) và đo phút xem lại, phút làm lại thật để thay hai cột `simulated` sau tuần 1. Phụ trách: PM trợ lý hoàn phí · kiểm tra 2026-12-14.
- Có lộ trình giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%, vì xem lại 100% làm chi phí lên 0,98–1,03× (`simulated`). Phụ trách: Trưởng nhóm CSKH · kiểm tra 2026-12-21.
