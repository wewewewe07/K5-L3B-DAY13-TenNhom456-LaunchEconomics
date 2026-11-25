# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: TenNhom456
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN trình hội đồng Gate 2a nhằm trả lời 4 câu hỏi cốt lõi: (1) Có đáng chạy về mặt kinh tế không, (2) Nhân viên có sử dụng gợi ý không, (3) Khi xảy ra lỗi thì phát hiện và khắc phục thế nào, và (4) Thiết kế kế hoạch pilot ra sao để tách được tác động nhân quả và đủ cỡ mẫu thống kê. Toàn bộ số liệu được tính tự động từ `src/lab13.py` trên mẫu 1.200 yêu cầu (`logix_requests.csv`) và 1.624 lần chạy (`logix_runs.csv`).

## 3. Giải pháp

- **Nhiệm vụ A & B ([`bang_chi_phi.md`](bang_chi_phi.md)):** Kiểm định 3 phép thử lý thuyết chạy lại (A1), xây dựng hàm `mo_hinh()` tính chi phí thật cho mỗi việc thành công từ trace và phút nhân viên giả lập (A2), phân rã theo 4 loại yêu cầu (A3), cộng chi phí cố định 40 triệu đ/tháng (A4), và chạy phân tích độ nhạy trên 9 kịch bản đơn lẻ, 1 kịch bản cặp, bài toán tối ưu số lần chạy tối đa cho cả hệ thống cùng kịch bản xem lại 100% (B1–B4).
- **Nhiệm vụ C ([`bang_loi.md`](bang_loi.md)):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 nhóm nguyên nhân gốc của Google PAIR, đối chiếu đạt đồng thuận ≥ 80%, rút ra quy tắc phân biệt và thiết kế bảng khắc phục cho 5 ca đại diện kèm event đo lường và vai trò phụ trách.
- **Nhiệm vụ D ([`pilot_plan.yaml`](pilot_plan.yaml)):** Tính cỡ mẫu và hệ số thiết kế (DE) cho 3 phương án chia (theo yêu cầu, theo nhân viên, theo depot), đánh giá 5 tiêu chí tách tác động và thiết lập 3 luật dừng theo cấu trúc NẾU–TRONG–THÌ–KHÔNG THÌ.
- **Nhiệm vụ E ([`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md), [`phieu_cham.md`](phieu_cham.md)):** Đặc tả 5 chỉ số vận hành gắn với 10 event có `trace_id`, lập bảng quản trị rủi ro kinh tế và tổng hợp thành 1 trang hồ sơ launch v0 để bảo vệ chéo tại hội đồng Gate 2a.

## 4. Kết quả

- **Kinh tế & Độ nhạy:** Chi phí mỗi việc thành công toàn mẫu là **4.472 đ** (`simulated`), gấp **16,3 lần** hoá đơn token+tool chia số yêu cầu (274,7 đ), trong đó giờ nhân viên làm lại (51,8%) và xem lại (40,7%) chiếm **92,5%** tổng chi phí (`simulated`). Tách theo loại: `noi_dia` (**2.696 đ = 0,22×**, `simulated`) và `hang_nang` (**8.221 đ = 0,69×**, `simulated`) có hiệu quả kinh tế rõ rệt; `quoc_te` (**22.515 đ = 1,88×**, `simulated`) lỗ nặng và chạy lại không giúp ích; `doi_tac` (**10.215 đ = 0,85×**, `simulated`) sát ngưỡng. Giới hạn **tối đa 2 lần chạy** giúp chi phí cả hệ thống rẻ nhất (**6.901.220 đ**, `simulated`). Nếu xem lại 100% (`noi_dia` + `hang_nang`), chi phí vọt lên **11.743 đ = 0,98×** (9 phút làm lại) hoặc **12.414 đ = 1,03×** (15,3 phút làm lại thực tế, `simulated`).
- **Phân loại lỗi & Thiết kế Pilot:** Đồng thuận gắn nhãn đạt **85% (17/20)**. Chọn chia ngẫu nhiên theo cụm nhân viên (**20 vs 20 nhân viên**), chấp nhận **MDE = 6 điểm phần trăm** ($n_{\text{eff}} = 859$/nhóm, $m \ge 299$ yêu cầu/nhân viên, $\text{DE} = 6{,}96$; power ở mức +5 điểm là 0,64).
- **Đề xuất cuối & Duyệt chéo:** Nhóm đề xuất **Go có điều kiện** cho phạm vi `noi_dia` + `hang_nang` với 4 điều kiện tiên quyết trước và trong tuần đầu pilot.

## 5. Khó khăn và cách xử lý

- **Khó khăn 1:** Khi đọc `logix_requests.csv` bằng `pd.read_csv()` mặc định, các ô trống trong cột `quyet_dinh_xem_lai` bị biến thành `NaN`. *Cách xử lý:* Truyền tham số `keep_default_na=False` theo đúng hướng dẫn kỹ thuật.
- **Khó khăn 2:** Giới hạn 40 nhân viên với $\text{ICC} = 0{,}02$ khiến cỡ mẫu hiệu dụng tối đa bị chặn ở $20 / 0{,}02 = 1.000 < 1.251$ (không đủ cho MDE 5 điểm). *Cách xử lý:* Giải phương trình cỡ mẫu cụm ở MDE 6 điểm ($n_{\text{eff}} = 859$), xác định ngưỡng $m \ge 299$ yêu cầu/nhân viên và ghi rõ đánh đổi power 0,64 ở mức +5 điểm vào hồ sơ.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và các file `report/team/MSSV_HoTen.md`.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Hai khoản chi phí lớn nhất (xem lại và làm lại, chiếm 92,5%) hiện đang dựa trên số phút giả lập (`_simulated`), và đợt chạy thử 2 tuần chưa có nhóm đối chứng song song.
- **Hướng cải thiện:** Triển khai hệ thống tracking 10 event có `trace_id` ngay từ ngày đầu pilot để thu thập thời gian xem lại/làm lại thực tế, đồng thời áp dụng kiểm định tuần tự và lộ trình giảm xem lại theo bậc.

## 8. Tài liệu tham khảo

- Erol và cộng sự (2025), *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu thư viện `statsmodels` (`NormalIndPower`, `proportion_effectsize`).
