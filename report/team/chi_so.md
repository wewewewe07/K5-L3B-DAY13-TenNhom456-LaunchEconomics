# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là **27,12%** (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (51 / 1.200) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu trong nhóm can thiệp được nhân viên mở và sử dụng gợi ý của trợ lý | Số yêu cầu có event `agent_suggestion_shown` và `staff_review_decision` thuộc nhóm `arm == 'treatment'`, chia tổng số yêu cầu được giao cho nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai số tiền hoặc hoàn trùng phát hiện qua đối soát sổ cái và kiểm tra mẫu hằng tuần | Số đơn trong mẫu kiểm tra có `so_tien_da_hoan != so_tien_dung` hoặc trùng `request_id` trong `refund_ledger_write`, chia tổng số đơn được kiểm tra | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách hàng | `request_id`, `depot`, `loai`, `so_tien_vnd`, `arm`, `created_at`, `trace_id` | Khi khách hàng gửi yêu cầu hoàn phí mới |
| `agent_run_completed` | Dịch vụ Agent | `run_id`, `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `pricing_version`, `trace_id` | Ngay sau mỗi lần chạy của agent (kể cả lần chạy lỗi) |
| `agent_suggestion_shown` | Giao diện nhân viên CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `shown_at`, `trace_id` | Khi gợi ý của trợ lý hiển thị trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc_te`, `trace_id` | Khi nhân viên bấm xác nhận giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai_thuc_te`, `ly_do_lam_lai`, `trace_id` | Khi nhân viên hoàn tất xử lý lại một ca trợ lý trả lời sai |
| `refund_ledger_write` | Dịch vụ sổ cái kế toán | `request_id`, `idempotency_key`, `so_tien_da_hoan`, `ket_qua` (`ok`/`loi`), `trace_id` | Khi hệ thống gọi lệnh ghi nhận giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Dịch vụ Agent | `request_id`, `reason`, `so_lan_chay`, `tom_tat`, `trace_id` | Khi trợ lý chuyển yêu cầu cho nhân viên sau khi quá số lần thử hoặc ngoài phạm vi |
| `ticket_closed` | Hệ thống quản lý ticket | `request_id`, `closed_at`, `dong_trong_24h`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / Hệ thống ticket | `request_id`, `reopened_at`, `reason`, `mo_lai_trong_7_ngay`, `trace_id` | Khi khách hàng mở lại yêu cầu trong vòng 7 ngày sau khi đóng |
| `audit_sample_checked` | Kế toán đối soát | `request_id`, `auditor_id`, `so_tien_da_hoan`, `so_tien_dung`, `is_correct`, `trace_id` | Hằng tuần khi kế toán kiểm tra mẫu ngẫu nhiên 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h và không mở lại trong 7 ngày):** Nối `refund_request_created` (`created_at`), `ticket_closed` (`closed_at`, `dong_trong_24h`) và `ticket_reopened` (`mo_lai_trong_7_ngay`) qua `trace_id` và `request_id`.
- **Chỉ số dùng 1 (Tỉ lệ bỏ qua gợi ý):** Đếm các bản ghi `staff_review_decision` có `quyet_dinh` thuộc `{'sua', 'bo'}` chia cho tổng số bản ghi `staff_review_decision` (hoặc `agent_suggestion_shown`) nối qua `trace_id`.
- **Chỉ số an toàn 1 (Tỉ lệ lỗi lọt đến khách):** Đếm các yêu cầu trong `refund_request_created` có xuất hiện event `ticket_reopened` trong vòng 7 ngày kể từ `ticket_closed` qua `trace_id`.
- **Chỉ số dùng 2 (Tỉ lệ yêu cầu nhóm can thiệp mở trợ lý):** Nối `refund_request_created` (`arm == 'treatment'`) với `agent_suggestion_shown` và `staff_review_decision` qua `trace_id`.
- **Chỉ số an toàn 2 (Tỉ lệ đơn hoàn sai tiền/hoàn trùng qua kiểm tra mẫu):** Nối `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung`) và `refund_ledger_write` (`idempotency_key`, `ket_qua`) qua `trace_id`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (hoặc thời gian làm lại thực tế cao như mức trung bình 15,3 phút) | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** (`simulated`) | Tỉ lệ event `staff_rework_completed` hằng tuần > 7% (đợt chạy thử phạm vi `noi_dia` + `hang_nang` là 4,89%) hoặc thời gian làm lại trung bình > 12 phút | Tạm dừng nhận `hang_nang`, thu hẹp pilot về chỉ còn `noi_dia`, giới hạn tối đa 2 lần chạy và rà soát 20 `trace_id` làm lại | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài sang các tuần sau | Chi phí mỗi việc thành công trong phạm vi `noi_dia` + `hang_nang` vọt lên **11.743 đ = 0,98×** (với 9 phút làm lại) hoặc **12.414 đ = 1,03×** (với 15,3 phút làm lại) so với 12.000 đ (`simulated`), mất toàn bộ lợi ích kinh tế | Tỉ lệ yêu cầu có event `staff_review_decision` vẫn > 50% ở cuối bước rollout 0.25 hoặc thời gian xem lại đo thật > 4,8 phút/ca | Hạ tỉ lệ xem lại theo bậc (100% → 50% → 20%) đối với nhóm `noi_dia` ngay khi tỉ lệ `sua + bo` < 15% và không có lỗi sổ cái | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thực tế trong phạm vi thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng làm cộng thêm **1.185 đ/việc** ở mức 45.000 yêu cầu/tháng (tổng **4.599 đ = 0,38×**, `simulated`), nhưng tăng gấp đôi lên **+2.370 đ/việc** nếu khối lượng giảm một nửa (tổng **5.784 đ = 0,48×**, `simulated`) | Số việc thành công thực tế theo tuần đạt < 50% kế hoạch (< 4.200 việc thành công/tuần khi ở quy mô đầy đủ) | Không mở rộng quy mô hạ tầng, đàm phán lại gói chi phí vận hành cố định theo bậc khối lượng | Giám đốc vận hành LogiX-VN |
