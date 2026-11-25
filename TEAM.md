# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyễn Thanh Tùng | 2A202603957 | thtung13102004@gmail.com | wewewewe07 | Người viết code (CP1, CP2) |
|   2 | Giang Thái Sơn | 2A202603964 |       |        | Người kiểm số (CP1, CP2) |
|   3 | Nguyễn Văn Anh Trung | 2A202603903 |       |        | Người gắn nhãn 1 |
|   4 | Bùi Quý Anh | 2A202603969 |       |        | Người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Nguyễn Thanh Tùng - 2A202503957

### Phần việc phụ trách

- Người viết code chính nửa đầu buổi (CP1: Nhiệm vụ A & CP2: Nhiệm vụ B).
- Rà soát kỹ thuật, kiểm tra logic code và đối chiếu số liệu nửa sau buổi (CP4 & CP5).

### Đóng góp cụ thể

- Cài đặt môi trường Python trong `src/.venv`, kiểm thử các thư viện cần thiết (`pandas`, `statsmodels`, `scipy`).
- Viết và hoàn thiện các hàm mô hình kinh tế chạy lại A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), vượt qua 3 test assert biết trước (1,20; 1,25; 1,25).
- Xây dựng hàm `mo_hinh()` trong `src/lab13.py` tính toán chi phí token, tool, làm lại, xem lại và CPS trên 1.200 yêu cầu mẫu từ dữ liệu trace.
- Lập trình phân rã chi phí theo 4 loại yêu cầu (A3), tính khấu hao chi phí cố định 40 triệu đ/tháng (A4).
- Lập trình chạy 9 kịch bản độ nhạy đơn lẻ, kịch bản cặp (B1, B2), bài toán tối ưu giới hạn số lần chạy toàn hệ thống (B3) và kịch bản xem lại 100% (B4).

### Bằng chứng

-

## Giang Thái Sơn

### Phần việc phụ trách

- Người kiểm số nửa đầu buổi (CP1: Nhiệm vụ A & CP2: Nhiệm vụ B).
- Người viết code tiếp quản nửa sau buổi (CP4: Nhiệm vụ D & CP5: Nhiệm vụ E).

### Đóng góp cụ thể

- Tính tay độc lập để đối chiếu số liệu chi phí A1, A2 với kết quả từ `lab13.py` (đảm bảo độ lệch dưới 2% theo rubric).
- Điền toàn bộ số liệu và trả lời câu hỏi phân tích cho Nhiệm vụ A và B vào `report/team/bang_chi_phi.md`.
- Tiếp quản vai viết code sau giờ giải lao: viết hàm tính cỡ mẫu `co_mau()` cho kiểm định hai tỷ lệ độc lập, tính Design Effect ($DE = 1 + (m-1)ICC$) và cỡ mẫu cụm nhân viên cho kế hoạch Pilot (D1).
- Lập trình tính thử 3 chỉ số vận hành (chính, dùng, an toàn) trên 1.200 yêu cầu mẫu (E1).

**Kết quả đã kiểm trên nhánh `feature/son-cost-review`:** đối chiếu A1–A2 với CSV và kết quả chạy; sửa ngưỡng hòa vốn A4, ghi phép tính D1 vào chú thích kế hoạch pilot và điền ba giá trị E1 vào `report/team/chi_so.md`. Hàm D1 và phần tính E1 đã có trong code trước lượt này; Sơn rà soát kết quả, không nhận là người viết ban đầu.

### Bằng chứng

- `src/lab13.py`: ba phép thử A1 in ĐẠT; A2 có 1.624 lần chạy, 978 việc thành công, tổng chi phí 4.373.585 đ (`simulated`).
- `report/team/bang_chi_phi.md`: A4 hòa vốn khoảng 4.659 việc thành công/tháng, tính từ chi phí biến đổi 3.072.513 đ/900 việc (`simulated`).
- `report/team/pilot_plan.yaml`: chú thích D1; `report/team/chi_so.md`: ba giá trị E1; báo cáo cá nhân `report/team/2A202603964_GiangThaiSon.md`.

## Nguyễn Văn Anh Trung

### Phần việc phụ trách

- Người gắn nhãn 1 (CP3: Nhiệm vụ C).
- Tham gia xây dựng đặc tả chỉ số, danh sách event và quản trị rủi ro kinh tế (CP5: Nhiệm vụ E).

### Đóng góp cụ thể

- Đọc đề bài, canh điều kiện "Xong khi" và theo dõi tiến độ các checkpoint của nhóm.
- Thực hiện gắn nhãn độc lập 20 ca lỗi trong 8 phút (không trao đổi) theo 5 nhóm nguyên nhân gốc của Google PAIR.
- Cùng Người gắn nhãn 2 đối chiếu kết quả, tính tỉ lệ đồng thuận ($\ge 80\%$), thống nhất nhãn và viết quy tắc phân biệt cho các ca không trùng trong `report/team/bang_loi.md`.
- Thiết kế bảng khắc phục cho 5 ca lỗi đại diện (cách phát hiện đo được bằng event/ngưỡng, giải pháp xử lý và vai trò chịu trách nhiệm cụ thể).
- Phối hợp xây dựng bảng đặc tả 10 event có gắn `trace_id` trong `report/team/chi_so.md`.

### Bằng chứng

-

## Bùi Quý Anh

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ nhóm (CP3, CP4, CP5).
- Phụ trách tổng hợp hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`), kế hoạch pilot (`pilot_plan.yaml`) và phiếu chấm duyệt chéo Gate 2a (`phieu_cham.md`).

### Đóng góp cụ thể

- Thực hiện gắn nhãn độc lập 20 ca lỗi trong 8 phút (không trao đổi) ở CP3, tham gia thống nhất bộ nhãn chung.
- Thu gom và đồng bộ số liệu xuyên suốt buổi lab: tổng hợp kết quả chi phí (A, B), phân loại lỗi (C), kế hoạch pilot (D), chỉ số và rủi ro (E) vào trang hồ sơ chuẩn 1 trang `report/team/ho_so_launch_v0.md`.
- Hoàn thiện kế hoạch pilot trong `report/team/pilot_plan.yaml` (thiết lập 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ, quy trình rollback 30 phút).
- Đóng vai đại diện Hội đồng Gate 2a chấm chéo nhóm $n+1$, soạn các câu hỏi chất vấn định lượng và điền biên bản `report/team/phieu_cham.md`.

### Bằng chứng

-
