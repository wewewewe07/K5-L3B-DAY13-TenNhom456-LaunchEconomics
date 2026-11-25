# Báo cáo cá nhân — Nguyễn Thanh Tùng · 2A202603957

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thanh Tùng
- MSSV: 2A202503957
- Email: thtung13102004@gmail.com
- Vai trong nhóm: Người viết code (nửa đầu: CP1, CP2) / Rà soát kỹ thuật (nửa sau: CP4, CP5)

## 2. Phần việc phụ trách

- Người viết code chính nửa đầu buổi cho CP1 (Nhiệm vụ A · Mô hình chi phí mỗi việc thành công) và CP2 (Nhiệm vụ B · Bảng độ nhạy).
- Rà soát kỹ thuật, kiểm tra logic code và đối chiếu số liệu thống kê nửa sau buổi cho CP4 (Nhiệm vụ D) và CP5 (Nhiệm vụ E).

## 3. Đóng góp cụ thể

- Thiết lập môi trường Python ảo trong `src/.venv` và cài đặt đầy đủ các thư viện phụ thuộc (`pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`).
- Viết và hoàn thiện các hàm toán học kinh tế chạy lại A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), đảm bảo vượt qua 100% ba phép thử assert đáp án biết trước (1,20 · 1,25 · 1,25).
- Lập trình hàm `mo_hinh(runs, reqs, ...)` trong `src/lab13.py` tính toán chi phí token, tool, làm lại, xem lại và CPS trên mẫu 1.200 yêu cầu từ `logix_runs.csv` và `logix_requests.csv`.
- Phân rã chi phí theo 4 loại yêu cầu ở A3 (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`), chỉ ra `quoc_te` không hiệu quả kinh tế (CPS 22.515 đ = 1,88× so với 12.000 đ).
- Tính toán chi phí cố định 40 triệu đ/tháng phân bổ theo quy mô 45.000 yêu cầu/tháng (A4).
- Lập trình chạy 9 kịch bản độ nhạy đơn lẻ, 1 kịch bản cặp (B1, B2), giải bài toán tối ưu giới hạn số lần chạy toàn hệ thống (B3) và kịch bản xem lại 100% (B4).
- Hỗ trợ hoàn thiện và đối chiếu toàn bộ các bảng số liệu, câu trả lời phân tích trong `report/team/bang_chi_phi.md`.

## 4. Bằng chứng

- File code chính: `src/lab13.py` chạy thông suốt và in ra toàn bộ kết quả phân tích.
- File bảng chi phí: `report/team/bang_chi_phi.md` điền đầy đủ các bảng A1, A2, A3, A4, B1, B2, B3, B4 và câu trả lời phân tích.
- Nhánh làm việc và các commit trên GitHub repo:
  - Branch: `feat/coder-wewewewe07`
  - Commit khởi tạo code: `f5fe338` (*feat(coder): hoan thien code lab13.py va phan vai TEAM.md*)
  - Kết quả kiểm thử terminal: `Ba phép thử đáp án biết trước: ĐẠT` và CPS toàn mẫu đạt 4.472 đ (`simulated`).

## 5. Công cụ AI đã dùng

- **Công cụ:** Google Gemini (Antigravity).
- **Mục đích:** Hỗ trợ giải thích bản chất toán học của các công thức chạy lại cấp số nhân (A1), gợi ý khung cấu trúc hàm `mo_hinh()` xử lý dữ liệu với pandas, và soát lỗi định dạng bảng markdown A3 trong `bang_chi_phi.md`.
- **Cách tự kiểm tra:** 
  - Tự chạy script `.venv/Scripts/python.exe lab13.py` trên terminal máy cục bộ để đối chiếu từng con số output với dữ liệu gốc `logix_requests.csv` và `logix_runs.csv`.
  - Tính tay độc lập 3 phép thử A1 theo công thức lý thuyết để xác minh hàm `so_lan_chay_ky_vong` và `ti_le_thanh_cong`.
  - Kiểm tra tính cộng tuyến tính ở bài toán đổi một cặp B2 (+5,6% + 40,7% = +46,3%).

## 6. Tự đánh giá

- Mức độ hoàn thành công việc: 100% (hoàn thành đúng hạn các checkpoint CP1, CP2 và hỗ trợ nhóm hoàn thiện báo cáo).
- Điểm đóng góp đề xuất: 10/10.
