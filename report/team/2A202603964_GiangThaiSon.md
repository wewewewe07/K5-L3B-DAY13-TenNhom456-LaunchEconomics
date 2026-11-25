# Báo cáo cá nhân — Giang Thái Sơn · 2A202603964

## 1. Thông tin thành viên

- Họ tên: Giang Thái Sơn
- MSSV: 2A202603964
- Email: Chưa cung cấp
- Vai trong nhóm: Người kiểm số CP1–CP2, tiếp quản kiểm code và kết quả D1/E1 sau giờ giải lao

## 2. Phần việc phụ trách

- Đối chiếu độc lập kết quả mô hình chi phí A1–A4 và bảng độ nhạy B1–B4.
- Rà soát phép tính cỡ mẫu D1, điền kết quả vào chú thích kế hoạch pilot.
- Tính thử ba chỉ số E1 từ mẫu 1.200 yêu cầu và điền bảng chỉ số.

## 3. Đóng góp cụ thể

- Kiểm A1 theo công thức: với p = 0,8 và tối đa 2 lần, số lần chạy kỳ vọng là 1 + 0,2 = 1,20; nếu chạy đến khi đúng là 1/0,8 = 1,25. Chi phí mỗi việc thành công ở tối đa 3 lần có hệ số 1/0,8 = 1,25.
- Tính lại A2 trực tiếp từ hai CSV: token 245.585,132 đ, tool 84.000 đ, xem lại 890 × 2.000 = 1.780.000 đ (`simulated`), làm lại 1.132 × 2.000 = 2.264.000 đ (`simulated`). Tổng 4.373.585,132 đ chia 978 việc thành công bằng 4.471,97 đ/việc (`simulated`), khớp số làm tròn 4.472 đ trong bảng.
- Soát A3 và B1–B4 với output script. Sửa ngưỡng hòa vốn A4 theo phép tính 40.000.000 ÷ (12.000 − 3.072.513,274/900) = 4.658,69, cần ít nhất 4.659 việc thành công mỗi tháng để chi phí không vượt mức nhân viên tự làm (`simulated`). Đồng bộ B4 với kết quả chạy 12.415 đ khi dùng số phút làm lại trung bình chưa làm tròn.
- Kiểm D1: 1.251 yêu cầu mỗi nhóm ở mức chênh 5 điểm; chia theo nhân viên với m = 75 có DE = 2,48 và cần 3.103 yêu cầu mỗi nhóm; 20 nhân viên/nhóm chỉ có giới hạn hiệu dụng 1.000; mức chênh 6 điểm cần ít nhất 299 yêu cầu mỗi nhân viên. Ghi kết quả vào chú thích `pilot_plan.yaml` để người giữ hồ sơ chọn phương án và hoàn tất các trường còn lại.
- Kiểm E1 trực tiếp từ CSV và điền bảng: chỉ số chính 994/1.200 = 82,83%; bỏ qua gợi ý 48/177 = 27,12%; mở lại trong 7 ngày 51/1.200 = 4,25%.
- Phần tính D1 và E1 trong `src/lab13.py` đã được Tùng viết trước. Lượt này Sơn kiểm kết quả và bổ sung phép tính hòa vốn A4 vào output code.

## 4. Bằng chứng

- `src/lab13.py` chạy trong `src/` bằng `.venv/Scripts/python.exe lab13.py`, in `Ba phép thử đáp án biết trước: ĐẠT` và kết quả A–E.
- `report/team/bang_chi_phi.md` có ngưỡng hòa vốn A4 đã sửa và các bảng A/B được đối chiếu.
- `report/team/pilot_plan.yaml` có phép tính D1 ở phần chú thích; `report/team/chi_so.md` có ba giá trị E1.
- `TEAM.md` ghi kết quả kiểm số và phạm vi đóng góp của Sơn.

## 5. Công cụ AI đã dùng

- Codex hỗ trợ đọc yêu cầu, chạy kiểm tra, đối chiếu phép tính với CSV và soạn báo cáo.
- Tự kiểm bằng công thức A1/A4, tính tổng độc lập từ hai CSV và chạy `lab13.py` trong môi trường Python của repo. Số trong báo cáo lấy từ dữ liệu và phép tính trên, không suy đoán.

## 6. Tự đánh giá

- Đã hoàn thành phần kiểm số A/B, rà soát D1 và điền ba kết quả E1. Kế hoạch pilot đầy đủ, danh sách event và hồ sơ launch cần các thành viên phụ trách tiếp tục tổng hợp.
