"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc."""
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Công thức cỡ mẫu so sánh hai tỉ lệ độc lập."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    tu_so = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(tu_so / ((p2 - p1) ** 2))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:15s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:15s} {gia_tri:>14,.0f}')
    print(f"Tỉ lệ CPS / Hoá đơn mỗi YC: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    print(f"Tỉ trọng làm lại: {ket_qua['lam_lai'] / ket_qua['tong'] * 100:.1f}% | xem lại: {ket_qua['xem_lai'] / ket_qua['tong'] * 100:.1f}%")

    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, sub_reqs)
        so_yc = len(sub_reqs)
        tl_tc = kq_loai['thanh_cong'] / so_yc * 100
        lan_chay_tb = sub_reqs['so_lan_chay'].mean()
        so_voi_base = kq_loai['cps'] / BASELINE
        print(f"{loai:10s} | YC: {so_yc:4d} | TC: {tl_tc:5.1f}% | Lần chạy/YC: {lan_chay_tb:4.2f} | CPS: {kq_loai['cps']:8,.0f} đ | vs 12k: {so_voi_base:.2f}x")

    print('\n--- Tỉ lệ chạy ok theo từng lần thử (attempt) ---')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(int)
    print((merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100).round(1))

    # Nhiệm vụ A4 · Chi phí cố định cho phạm vi noi_dia + hang_nang
    print('\n=== A4 · Chi phí cố định (noi_dia + hang_nang) ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    tc_mau = kq_pv['thanh_cong']  # 900 trên tổng 1200 yêu cầu mẫu
    hoa_von_viec_thang = math.ceil(40_000_000 / (BASELINE - kq_pv['cps']))
    for ten_kl, tong_yc_thang in [('45.000 yêu cầu/tháng', 45000), ('Một nửa (22.500 yc/tháng)', 22500)]:
        tc_thang = int(tong_yc_thang * tc_mau / len(reqs))
        cd_moi_viec = 40_000_000 / tc_thang
        cps_cong_cd = kq_pv['cps'] + cd_moi_viec
        print(f"{ten_kl:26s} | TC/tháng: {tc_thang:6,d} | CĐ/việc: {cd_moi_viec:6,.0f} đ | CPS+CĐ: {cps_cong_cd:6,.0f} đ ({cps_cong_cd / BASELINE:.2f}x)")
    print(f"Điểm hòa vốn chi phí cố định: {hoa_von_viec_thang:,d} việc thành công/tháng")

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print('\n=== B1 · Bảng độ nhạy (đổi từng yếu tố) ===')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"{ten:25s} {cps:8,.0f} đ ({(cps / goc - 1) * 100:+6.1f}%)")

    print('\n=== B2 · Đổi một cặp (Token x2 + Xem lại x2) ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f"Token x2 + Xem lại x2:    {cps_cap:8,.0f} đ ({(cps_cap / goc - 1) * 100:+6.1f}%)")

    print('\n=== B3 · Giới hạn số lần chạy và chi phí cả hệ thống ===')
    for gh in [1, 2, 3]:
        kq_gh = mo_hinh(runs, reqs, max_lan_chay=gh)
        khong_tc = len(reqs) - kq_gh['thanh_cong']
        ca_he_thong = kq_gh['tong'] + khong_tc * BASELINE
        print(f"Giới hạn {gh} lần | Trợ lý: {kq_gh['tong']:10,.0f} đ | Không TC: {khong_tc:3d} | Cả hệ thống: {ca_he_thong:10,.0f} đ | CPS: {kq_gh['cps']:6,.0f} đ")

    print('\n=== B4 · Xem lại 100% (noi_dia + hang_nang) ===')
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_yc_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    tien_token_tool_pv = kq_pv['token'] + kq_pv['tool']
    tong_b4_9p = tien_token_tool_pv + so_yc_ok * 5 * LUONG_PHUT + so_lam_lai * 9 * LUONG_PHUT
    cps_b4_9p = tong_b4_9p / kq_pv['thanh_cong']
    phut_ll_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    tong_b4_thuc = tien_token_tool_pv + so_yc_ok * 5 * LUONG_PHUT + so_lam_lai * phut_ll_tb * LUONG_PHUT
    cps_b4_thuc = tong_b4_thuc / kq_pv['thanh_cong']
    print(f"Xem lại 100% (9 phút làm lại):    CPS = {cps_b4_9p:,.0f} đ ({cps_b4_9p / BASELINE:.2f}x)")
    print(f"Xem lại 100% ({phut_ll_tb:.1f} phút làm lại): CPS = {cps_b4_thuc:,.0f} đ ({cps_b4_thuc / BASELINE:.2f}x)")

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    print('\n=== D1 · Cỡ mẫu kế hoạch Pilot ===')
    n_a = co_mau(0.70, 0.75)
    de_b = 1 + (75 - 1) * 0.02
    n_b = math.ceil(n_a * de_b)
    nv_moi_nhom = math.ceil(n_b / 75)
    n_eff_max_staff = 20 / 0.02
    n_eff_max_depot = 6 / 0.02
    n_6pt = co_mau(0.70, 0.76)
    m_min = math.ceil(n_6pt * (1 - 0.02) / (20 - n_6pt * 0.02))
    de_e = 1 + (m_min - 1) * 0.02
    es_5pt = proportion_effectsize(0.75, 0.70)
    power_5pt_at_859 = NormalIndPower().power(effect_size=es_5pt, nobs1=n_6pt, alpha=0.05, ratio=1.0)
    print(f"a) Chia theo yêu cầu (+5 điểm): {n_a} yêu cầu/nhóm")
    print(f"b) Chia theo NV (m=75): DE = {de_b:.2f}, cần {n_b} yêu cầu/nhóm -> {nv_moi_nhom} NV/nhóm (tổng {nv_moi_nhom*2} > 40 NV)")
    print(f"c) 20 NV/nhóm: cỡ mẫu hiệu dụng tối đa = {n_eff_max_staff:.0f} < {n_a} (không đạt)")
    print(f"d) 6 depot/nhóm: cỡ mẫu hiệu dụng tối đa = {n_eff_max_depot:.0f} < {n_a} (không đạt)")
    print(f"e) Chấp nhận +6 điểm (cần {n_6pt}/nhóm), 20 NV/nhóm: cần m >= {m_min} YC/NV (DE = {de_e:.2f}; power ở +5 điểm = {power_5pt_at_859:.2f})")

    print('\n=== E1 · Tính thử 3 chỉ số trên 1.200 yêu cầu ===')
    cs_chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean() * 100
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    cs_dung = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean() * 100
    cs_antoan = (reqs['mo_lai_trong_7_ngay'] == 1).mean() * 100
    print(f"Chỉ số chính (đóng 24h & không mở lại 7 ngày): {cs_chinh:.2f}% ({int(((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum())}/{len(reqs)})")
    print(f"Chỉ số dùng (tỉ lệ bỏ qua gợi ý sua+bo):       {cs_dung:.2f}% ({int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())}/{len(xem)})")
    print(f"Chỉ số an toàn (mở lại trong 7 ngày):          {cs_antoan:.2f}% ({int((reqs['mo_lai_trong_7_ngay'] == 1).sum())}/{len(reqs)})")
