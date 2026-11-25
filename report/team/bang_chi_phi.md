# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | 329.585 ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Chi phí mỗi việc thành công (4.472 đ, `simulated`) gấp **16,3 lần** con số hoá đơn token và tool chia số yêu cầu (274,7 đ). Nếu tính cả hệ thống gồm 222 ca không thành công nhân viên làm thay (222 × 12.000 đ), chi phí là **5.865 đ/yêu cầu = 0,49× của 12.000 đ** (`simulated`).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Khoản lớn nhất là **chi phí làm lại chiếm 51,8%** (2.264.000 đ, `simulated`), đứng thứ hai là chi phí xem lại chiếm **40,7%** (1.780.000 đ, `simulated`). Tổng thời gian nhân viên chiếm tới **92,5%** tổng chi phí vận hành trợ lý (`simulated`).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (`simulated`) | 0,22× (`simulated`) |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (`simulated`) | 0,69× (`simulated`) |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (`simulated`) | 1,88× (`simulated`) |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (`simulated`) | 0,85× (`simulated`) |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? Loại **`quoc_te`** không đáng để trợ lý xử lý vì chi phí lên tới **22.515 đ = 1,88× của 12.000 đ** (`simulated`) và tỉ lệ thành công chỉ đạt **27,3%**. Cho chạy lại tới 3 lần không giúp ích vì tỉ lệ chạy `ok` giảm mạnh từ **30,0% (lần 1) xuống 11,4% (lần 2) và 2,2% (lần 3)** (trung bình 2,32 lần chạy/yêu cầu chỉ làm tốn tiền). Loại **`doi_tac`** cũng sát ngưỡng (**10.215 đ = 0,85×**, `simulated`) và có điều khoản riêng nên loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (`simulated`) | 0,38× (`simulated`) |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (`simulated`) | 0,48× (`simulated`) |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Chi phí cố định 40 triệu đ/tháng không làm đổi kết luận ở quy mô đầy đủ 45.000 yêu cầu/tháng (**4.599 đ = 0,38×** so với 12.000 đ, `simulated`) hay một nửa khối lượng (**5.784 đ = 0,48×**, `simulated`). Điểm hòa vốn là **4.659 việc thành công/tháng**: 40.000.000 ÷ (12.000 − 3.072.513/900) ≈ 4.659. Dưới mức này, chi phí mỗi việc thành công cộng cố định vượt 12.000 đ (`simulated`).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (`simulated`) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (`simulated`) | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (`simulated`) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (`simulated`) | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (`simulated`) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (`simulated`) | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (`simulated`) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (`simulated`) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (`simulated`) | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: Chi phí mỗi việc thành công lên **6.543 đ (+46,3%)** (`simulated`), đúng bằng tổng hai mức tăng riêng lẻ (+5,6% + 40,7% = +46,3%) do mô hình chi phí có tính cộng tuyến tính trên cùng mẫu số 978 việc thành công.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại (±51,8% / −25,9%)** · 2. **Tỉ lệ xem lại (±40,7% / −20,3%)** · 3. **Lương nhân viên (+23,1% khi tăng 25%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (`simulated`) | 319 | 7.449.781 đ (`simulated`) | 4.111 đ (`simulated`) |
| 2 lần | 4.093.220 đ (`simulated`) | 234 | **6.901.220 đ** (`simulated`) | 4.237 đ (`simulated`) |
| 3 lần | 4.373.585 đ (`simulated`) | 222 | 7.037.585 đ (`simulated`) | 4.472 đ (`simulated`) |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn **tối đa 2 lần chạy** rẻ nhất cho công ty với tổng chi phí cả hệ thống là **6.901.220 đ** (`simulated`), tiết kiệm 136.365 đ so với 3 lần và 548.561 đ so với 1 lần. Mức này **không trùng** với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần chạy: 4.111 đ, `simulated`), vì giới hạn 1 lần đẩy thêm 85 ca khó sang nhân viên tự làm với giá 12.000 đ/ca.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 948 yêu cầu chạy `ok` (5 phút xem lại/ca), 48 ca `lam_lai` và 224.513 đ token+tool chia cho 900 việc thành công, nếu tính 9 phút làm lại/ca theo đề thì chi phí là **11.743 đ = 0,98× của 12.000 đ** (`simulated`). Nếu dùng trung bình **15,297 phút/ca** từ cột `phut_lam_lai_simulated` thì chi phí là **12.415 đ = 1,03× của 12.000 đ** (`simulated`), đắt hơn nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% khiến tiền xem lại (9.480.000 đ) chiếm tới **89,7%** tổng chi phí và xóa sạch lợi thế kinh tế của trợ lý (điểm hòa vốn yêu cầu thời gian xem lại ≤ 5,1 phút ở mức 9 phút làm lại, hoặc ≤ 4,8 phút ở mức 15,3 phút làm lại). Do đó, pilot bắt buộc phải đo thời gian xem lại thật và học được lộ trình giảm tỉ lệ xem lại an toàn theo từng bậc khi tỉ lệ sửa + bỏ < 15%.
