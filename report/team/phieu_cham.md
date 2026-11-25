# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): TenNhom456
- Nhóm được chấm: [Tên nhóm bạn chấm]

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp với số liệu CPS 4.472 đ (`simulated`), có nêu rõ số bất lợi khi xem lại 100% (11.743 đ = 0,98× và 12.414 đ = 1,03×, `simulated`) cùng power 0,64 ở mức +5 điểm và kèm điều kiện xử lý. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi con số tính từ phút xem lại/làm lại đều gắn nhãn `simulated` và trạng thái Giả lập; thu hẹp phạm vi chỉ lấy `noi_dia` (2.696 đ = 0,22×) và `hang_nang` (8.221 đ = 0,69×), loại `quoc_te` (22.515 đ = 1,88×) và `doi_tac` (10.215 đ = 0,85×). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên theo nhân viên 20 vs 20 cụm song song, tính đúng $n_{\text{eff}} = 859$/nhóm cho MDE 6 điểm ($m \ge 299$, DE = 6,96); 3 luật dừng đủ 4 vế NẾU–TRONG–THÌ–KHÔNG THÌ, ngưỡng mở lại tính tới baseline 4,25%. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ định lượng đầy đủ chi phí thật (4.472 đ/việc thành công, `simulated`), chỉ ra rủi ro xem lại 100% (11.743 đ – 12.414 đ, `simulated`), thu hẹp phạm vi hợp lý và thiết kế pilot 20 vs 20 nhân viên có luật dừng chặt chẽ.

**Một câu hỏi cho đội trình:** "Nếu trong 2 tuần đầu của pilot, thời gian làm lại thực tế đo được từ event `staff_rework_completed` giữ ở mức trung bình 15,3 phút/ca như dữ liệu giả lập và nhân viên vẫn phải xem lại 100% câu trả lời, chi phí mỗi việc thành công là 12.414 đ (1,03× so với 12.000 đ), nhóm sẽ kích hoạt luật dừng nào và cần giảm thời gian xem lại xuống tối đa bao nhiêu phút để hòa vốn?"

**Câu trả lời của đội trình (ghi lại tại buổi):** "Đội trình trả lời: Để hòa vốn 12.000 đ khi thời gian làm lại là 15,3 phút/ca, thời gian mỗi lần xem lại phải giảm xuống tối đa 4,8 phút/ca (hoặc 5,1 phút/ca nếu làm lại mất 9 phút). Nhóm chỉ xem lại 100% ở tuần đầu bước rollout 0.10 (4 nhân viên), sau đó hạ tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; nếu CPS vẫn > 8.000 đ trong 2 tuần liên tiếp thì PM trợ lý hoàn phí kích hoạt luật dừng số 2 để thu hẹp về `noi_dia` và giới hạn 2 lần chạy."
