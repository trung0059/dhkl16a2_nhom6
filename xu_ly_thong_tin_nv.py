#Nhóm 6
print('Trần Đức Lương|Trần Đức Trung|Khuất Duy Hưởng\Từ Tất Duy|lê tất thành')





#quan ly nhan vien
print("ẤN 1 ĐỂ TIẾP TỤC")
import os
_path=""
listnv=[]
def mo_file_dsnv(_path,listnv):
    return
def luu_dsnv(listnv):
    return
def them_tt(listnv):
    while True:
        ma_nv=input("Nhập mã nhân viên:")
        ten_nv=input("Tên nhân viên:")
        nam_cong_tac=int(input('Năm công tác :'))
        luong_co_ban=int(input("LươnG cơ bản:"))
        if nam_cong_tac>=20:
            phu_cap=10000000
        elif nam_cong_tac<20 and nam_cong_tac>=15:
            phu_cap=8000000
        elif nam_cong_tac>=10 and nam_cong_tac<15:
            phu_cap=5000000
        elif nam_cong_tac >=5 and nam_cong_tac<10:
            phu_cap=3000000
        else:
            phu_cap=1000000
        thu_nhap=luong_co_ban+phu_cap
        tt=int(input('Bạn có muốn tiếp tục? '))
        listnv.append({'Mã nv':ma_nv,'Tên nv':ten_nv,'Năm công tác':nam_cong_tac,'Lương cơ bản':luong_co_ban,'Phụ cấp':phu_cap,'Thu nhập':thu_nhap})
        if tt!=1:
            break
    return
them_tt(listnv)
print(listnv)
#bảng nhân viên
def in_ds_nv(listnv):
    print('{:20}{:18}{:18}{:>20}{:>20}{:>20}'.format('Mã nv','Tên nv','Năm công tác','Lương cơ bản','Phụ cấp','Thu nhặp'))
    for nv in listnv:
        print('{:20}{:18}{:12}{:15}{:28}{:>20}'.format(nv['Mã nv'],nv['Tên nv'],nv['Năm công tác'],nv['Lương cơ bản'],nv['Phụ cấp'],nv['Thu nhập']))
    return
#tra cứu nhân viên
def tra_cuu_nv(listnv,manv):
    for i in listnv:
        if i['Mã nv']==manv:
            return i
    return
#xóa dữ liệu
def xoa_nv(listnv,xoanv):
    for y in range(len(listnv)):
        nv=listnv[y]
        if nv['Mã nv']==xoanv:
            del(listnv[y])
            return 1
    return 0

#sắp xếp 
def sap_xep_luong(listnv):
     list=sorted(listnv,key=lambda x :x['Thu nhập'])
     return list
#sap_xep_luong(listnv)
#bắt đầu chương trình
print('VUI LÒNG CHỌN CÚ PHÁP!')
while True:
    print('1:Thêm nhâm viên ')
    print('2: In danh sách nhân viên')
    print("3:Tra cứu nhân viên ")
    print("4:Xóa dữ liệu nhân viên")
    print('5:Lập danh sách ra file csv')
    print("6:Sắp xếp")
    choose=int(input("Vui lòng nhập cú pháp:"))
    if choose==1:
        them_tt(listnv)
    elif choose==2:
        in_ds_nv(listnv)
    elif choose==3:
        manv=input('Vui lòng nhập mã nhân viên:')
        i=tra_cuu_nv(listnv,manv)
        if  i ==None:
            print('Mã nhân viên không hợp lệ')
        else:
            print(i)
    elif choose==4:
        xoanv=int(input("Nhập mã nhân viên muốn xóa:"))  
        check=input("Bạn có chắc chắn muốn xóa mã ?(1:có|2:không)") 
        if check==1:
            y=xoa_nv(listnv,xoanv)
            if y==1:
                print('Đã xóa ',xoanv)
            else:   
                print("Mã nhân viên không tồn tại")  
    elif choose==5:
        import csv
        with open('qly_nhan_vien.csv','w',encoding='utf8') as f:
            writer=csv.writer(f)
            writer.writerow(listnv)
    elif choose==6:
        print("Danh sách nhân vien trước khi sắp xếp",listnv)
        print('Danh sách nhân viên sau khi sắp xếp:\n')
        sap_xep_luong(listnv)
        print('{:20}{:18}{:18}{:>20}{:>20}{:>20}'.format('Mã nv','Tên nv','Năm công tác','Lương cơ bản','Phụ cấp','Thu nhặp'))
        for vn in sap_xep_luong(listnv):
            print('{:20}{:18}{:12}{:15}{:28}{:>20}'.format(vn['Mã nv'],vn['Tên nv'],vn['Năm công tác'],vn['Lương cơ bản'],vn['Phụ cấp'],vn['Thu nhập']))
        

    else :
        break
    ctn=input('Bạn có muốn tiếp tục (1:tt) ')   
    if ctn!='1':
        break
    else: 
        os.system('cls')
    input('Gõ phím bất kỳ để tiếp tục chương trình !!!')
