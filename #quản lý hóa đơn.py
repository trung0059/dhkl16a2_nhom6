#quản lý hóa đơn
import os
_path=""
lstHoaDon=[]
#hàm thứ nhất
def mo_file_hoa_don(_path,lstHoaDon):
    return
#hàm thứ hai
def lưu_ds_hoa_don(lstHoaDon):
    return
#hàm thứ ba
def them_hoa_don(lstHoaDon):
    while True:
        so_hd=input('Nhập số hóa đơn: ')
        ngay_hd=input('Ngày hóa đơn: ')
        ho_tenkh=input('Họ tên khách hàng: ')
        dia_chi=input('Địa chỉ khách hàng: ')
        quan=input('Quận: ')
        dien_thoai=input('điện thoai: ')
        tong_tien_hd=float(input('Tổng tiền hợp đồng: '))
        tam_ung=float(input('Tạm ứng: '))
        con_lai=float(tong_tien_hd-tam_ung)
        lstHoaDon.append({'so_hd':so_hd,'ngay_hd':ngay_hd,\
            'ho_tenkh':ho_tenkh,'dia_chi':dia_chi,'quan':quan,\
            'dien_thoai':dien_thoai, 'tong_tien_hd':tong_tien_hd,\
            'tam_ung':tam_ung, 'con_lai':con_lai})
        #hết lệnh append
        tt=input('Bạn có muốn tiếp tục thêm? (1:TT):')
        if tt!=1:
            break
    return 
them_hoa_don(lstHoaDon)
#-----------------------------------------------
def  in_ds_hoa_don(lstHoaDon):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format('so_hd','ngay_hd','ho_ten_kh','dia_chi','quan','dien_thoai','tong_tien_hd','tam_ung','con_lai'))

    for hd in lstHoaDon:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(hd['so_hd'],hd['ngay_hd'],hd['ho_tenkh'],hd['dia_chi'],hd['quan'],hd['dien_thoai'],hd['tong_tien_hd'],hd['tam_ung'],hd['con_lai']))
    
    return
in_ds_hoa_don(lstHoaDon)
#-----------------------------------------------
def tra_cuu_hoa_don(lstHoaDon):
    return
def thong_ke(lstHoaDon):
    return
