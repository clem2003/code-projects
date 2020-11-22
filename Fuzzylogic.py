import pandas as pd
import xlwt
from xlwt import Workbook
import random as rnd


def fuzzy_func(x,a,b): #rumus fungsi keanggotaan
    return ((x-a)/(b-a))

def bacafile(): 
    data = pd.read_excel('D:\IF 2020-2021\SMT 5\Pengantar AI\MEET 7\Mahasiswa.xls')
    read_temp = pd.DataFrame(data, columns=['Id','Penghasilan','Pengeluaran'])
    arr_data = read_temp.values.tolist()
    return arr_data

def earning_fuzz(earning): #fuzzy penghasilan
    earn_temp = []
    if (earning < 5):
        earn_temp.append(["Dikit",1])
        earn_temp.append(["Cukup",0])
    if (earning >= 15):
        earn_temp.append(["Banyak",1])
        earn_temp.append(["Cukup",0])
    if (earning >= 5 and earning < 10 ):
        res = fuzzy_func(earning,5,10)
        earn_temp.append(["Cukup",res])
        earn_temp.append(["Dikit",1-res])
    if (earning == 10):
        earn_temp.append(["Cukup",1])
        earn_temp.append(["Banyak",0])
    if (earning >= 10 and earning < 15):
        res = fuzzy_func(earning,10,15)
        earn_temp.append(["Banyak",res])
        earn_temp.append(["Cukup",1-res])
    return earn_temp


def expenses_fuzz(expenses): #fuzzy pengeluaran
    expenses_temp = []
    if (expenses < 4):
        expenses_temp.append(["Dikit",1])
        expenses_temp.append(["Cukup",0])
    if (expenses >= 10):
        expenses_temp.append(["Banyak",1])
        expenses_temp.append(["Cukup",0])
    if (expenses >= 4 and expenses < 8):
        res = fuzzy_func(expenses,4,8)
        expenses_temp.append(["Cukup",res])
        expenses_temp.append(["Dikit",1-res])
    if (expenses == 8):
        expenses_temp.append(["Cukup",1])
        expenses_temp.append(["Banyak",0])
    if (expenses >= 8 and expenses < 10):
        res = fuzzy_func(expenses,8,10)
        expenses_temp.append(["Banyak",res])
        expenses_temp.append(["Cukup",1-res])
    return expenses_temp


def nilai_kelayakan(expenses, earning): #cari nilai kelayakan untuk defuzzyfication (conjuction)
    conj_arr = [] #array conjunction
    # Yes berarti LAYAK; No berarti TIDAK LAYAK
    NK = []
    for i in range(2):
        for j in range(2):
            if (earning[i][0] == "Dikit" and expenses[j][0] == "Dikit"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["No",earning[i][1]])
                else:
                    conj_arr.append(["No",expenses[j][1]])
            if (earning[i][0] == "Dikit" and expenses[j][0] == "Cukup"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["Yes",earning[i][1]])
                else:
                    conj_arr.append(["Yes",expenses[j][1]])
            if (earning[i][0] == "Dikit" and expenses[j][0] == "Banyak"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["Yes",earning[i][1]])
                else:
                    conj_arr.append(["Yes",expenses[j][1]])
            if (earning[i][0] == "Cukup" and expenses[j][0] == "Dikit"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["No",earning[i][1]])
                else:
                    conj_arr.append(["No",expenses[j][1]])
            if (earning[i][0] == "Cukup" and expenses[j][0] == "Cukup"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["No",earning[i][1]])
                else:
                    conj_arr.append(["No",expenses[j][1]])
            if (earning[i][0] == "Cukup" and expenses[j][0] == "Banyak"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["Yes",earning[i][1]])
                else:
                    conj_arr.append(["Yes",expenses[j][1]])
            if (earning[i][0] == "Banyak" and expenses[j][0] == "Dikit"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["No",earning[i][1]])
                else:
                    conj_arr.append(["No",expenses[j][1]])
            if (earning[i][0] == "Banyak" and expenses[j][0] == "Cukup"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["No",earning[i][1]])
                else:
                    conj_arr.append(["No",expenses[j][1]])
            if (earning[i][0] == "Banyak" and expenses[j][0] == "Banyak"):
                if earning[i][1] < expenses[j][1]:
                    conj_arr.append(["No",earning[i][1]])
                else:
                    conj_arr.append(["No",expenses[j][1]])

    NK_rendah = []
    NK_tinggi = []
    for x in range(4):
        if(conj_arr[x][0] == "Yes"):
            NK_tinggi.append(conj_arr[x][1])
        else:
            NK_rendah.append(conj_arr[x][1])
    
    if (len(NK_tinggi) == 0):
        NK.append(0)
    else:
        NK.append(max(NK_tinggi))
        
    if (len(NK_rendah) == 0):
        NK.append(0)
    else:
        NK.append(max(NK_rendah))
        
    return NK

def defuzzy(nilai1, nilai2): #parameter defuzzy adalah tinggi,rendah
    jml_dikit = 0
    jml_cukup = 0
    jml_banyak = 0
    dikit_list = []
    cukup_list = []
    banyak_list = []
    temp1 = 0
    
    rnd_arr = rnd.sample(range(0,100),10) #mengambil 10 titik acak dari 100 nilai pada data
    for i in rnd_arr:
        if (i < 50):
            dikit_list.append(i)
        elif (i >= 50 and i < 80):
            cukup_list.append(i)
        elif (i > 80):
            banyak_list.append(i)

    for i in dikit_list:
        jml_dikit += i
    jml_dikit = jml_dikit*nilai2
    
    for i in banyak_list:
        jml_banyak += 1
    jml_banyak = jml_banyak*nilai1
    
    for i in range(len(cukup_list)):
        if (nilai2 < nilai1):
            jml_cukup += cukup_list[i] * (cukup_list[i]/(50+80))
            temp1 = cukup_list[i]/130
        else:
            jml_cukup += -(((cukup_list[i]/(50+80)) - 1) * cukup_list[i])
            temp1 = -(((cukup_list[i]/130) - 1) * cukup_list[i])
    res = (jml_dikit + jml_dikit + jml_banyak)
    res2 = (nilai2 * len(dikit_list)) + temp1 + (nilai1 * len(banyak_list))
    
    return (res/res2) #return hasil akhir nilai kelayakan


#MAIN PROGRAM
data = bacafile()

earning_list = []
expenses_list = []
list_nilai = []

earning_temp = []
expenses_temp = []
kelayakan_list = []
arr_akhir = []

for d in data:
    earning_temp = earning_fuzz(d[1])
    expenses_temp = expenses_fuzz(d[2])
    earning_temp.append(d[0])
    expenses_temp.append(d[0])
    
    earning_list.append(earning_temp)
    expenses_list.append(expenses_temp)
    
for i in range(100):
    temp = nilai_kelayakan(expenses_list[i], earning_list[i])
    list_nilai.append(temp) #append nilai dari temp ke list nilai
    
for d in range(100):
    temp = defuzzy(list_nilai[i][0], list_nilai[i][1])
    kelayakan_list.append([d+1,temp]) #append nilai kelayakan ke list
hasil = sorted(kelayakan_list, key = lambda x: x[1], reverse = True) #sort nilai kelayakan

for x in range(20):
    arr_akhir.append(hasil[x][0])    #Append 20 nomor penerima ke list untuk output ke excel


def tulisExcel(namafile,kelayakan_list):#kode untuk write ke excel
    wb = Workbook()
    row, column = 1,0
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0,0,'ID Penerima')
    for konten in kelayakan_list:
        sheet1.write(row,column,konten)
        row += 1
    wb.save(namafile)


tulisExcel('D:\IF 2020-2021\SMT 5\Pengantar AI\MEET 7\Bantuan.xls',arr_akhir) 
#untuk write excel ada penulisan direktori karena di kasus saya file nya tertulis di folder random