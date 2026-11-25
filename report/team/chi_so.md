# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = 82,83% |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = 27,12% |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = 4,25% |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm dùng trợ lý được mở bằng trợ lý | Số yêu cầu có `agent_suggestion_shown` của nhân viên nhóm trợ lý, chia tổng số yêu cầu nhóm trợ lý nhận (`refund_request_created`, arm = tro_ly) | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn trong `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra (100 đơn/tuần) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

Ba chỉ số trong đợt chạy thử lần lượt là 82,83%, 27,12% và 4,25%, tính trên dữ liệu CSV của lab.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai đo thật, trace_id | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi hoàn tiền vào sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, 100 đơn mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `refund_request_created` (mẫu số), `ticket_closed` (closed_at trong 24 giờ từ lúc tạo) và không có `ticket_reopened` trong 7 ngày.
- Dùng, bỏ qua gợi ý: `staff_review_decision` với quyet_dinh là sua hoặc bo, chia tổng `staff_review_decision`.
- An toàn, lỗi lọt đến khách: `ticket_reopened` trong 7 ngày, chia `refund_request_created`.
- Dùng, tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` có arm = tro_ly.
- An toàn, tự đề xuất: `audit_sample_checked` có so_tien_da_hoan khác so_tien_dung, chia số đơn kiểm tra.
- Chi phí mỗi việc thành công trong luật dừng: `agent_run_completed` (token, tool), `staff_review_decision` và `staff_rework_completed` (phút thật thay cho cột `simulated`). Cả năm chỉ số đều tính được từ danh sách event.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công +51,8%, lên 6.787 đ (`simulated`) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 48/982 = 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, giới hạn 2 lần chạy, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu (`simulated`) | % yêu cầu được xem lại còn > 50% ở cuối bước rollout 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% trong 1 tuần | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Tiền cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa; hòa vốn 4.659 việc thành công/tháng (`simulated`) | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, đàm phán lại chi phí cố định | Giám đốc vận hành |
