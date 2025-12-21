from subprocess import call
import sys
with open("input1-mod1.txt") as file:
    lines = file.readlines()
    penggaris = [x[2:10] for x in lines[1:4]]
    m_sekrup = [x[2:10] for x in lines[5:8]]
    j_sorong = [x[3:10] for x in lines[9:12]]
    n_ohaus = [x[3:10] for x in lines[13:17]]
    a_digital = [x[4:10] for x in lines[19:24]]
    v_digital = [x[3:10] for x in lines[25:30]]
    m_dadu = lines[31].strip('=gD')
def show_list_mod2():
    print(f"Penggaris\nx = {penggaris[0]} cm\ny = {penggaris[1]} cm\nz = {penggaris[2]} cm")
    print("")
    print(f"Mikrometer Sekrup\nx = {m_sekrup[0]} mm\ny = {m_sekrup[1]} mm\nz = {m_sekrup[2]} mm")
    print("")
    print(f"Jangka Sorong\nx = {j_sorong[0]} mm\ny = {j_sorong[1]} mm\nz = {j_sorong[2]} mm")
    print("")
    print("Neraca O'haus")
    for i in range(len(n_ohaus)):
        print(f"Percobaan {i + 1}: {n_ohaus[i]} g")
    print("")
    print("Amperemeter Digital")
    for i in range(len(a_digital)):
        print(f"Percobaan {i + 1}: {a_digital[i]} mA")
        print("")
    print("Voltmeter Digital")
    for i in range(len(v_digital)):
        print(f"Percobaan {i + 1}: {v_digital[i]} V")
    print(m_dadu)
show_list_mod2()
mm_penggaris = []
for x in range(len(penggaris)):
    mm_pg_rep = float(penggaris[x]) / 10
    mm_penggaris.append(mm_pg_rep)
print("")
print(f"Hasil Penggaris dalam mm\nx={mm_penggaris[0]} mm\ny={mm_penggaris[1]}\nz={mm_penggaris[2]} mm")
print("")
print(f"Pengukuran berulang Penggaris\nx={penggaris[0]} ± 0.05 cm\ny={penggaris[1]} ± 0.05 cm\nz={penggaris[2]} ± 0.05 cm")
with open("output1-mod1.txt", "w") as file:
    file.write(f"Hasil Penggaris dalam mm\nx={mm_penggaris[0]} mm\ny={mm_penggaris[1]}\nz={mm_penggaris[2]} mm\n")
    print("", file=file)
    file.write(f"Pengukuran berulang Penggaris\nx={penggaris[0]} ± 0.05 cm\ny={penggaris[1]} ± 0.05 cm\nz={penggaris[2]} ± 0.05 cm\n")
    print("", file=file)
cm_m_sekrup = []
for x in range(len(m_sekrup)):
    cm_skrup = float(m_sekrup[x]) / 10
    cm_m_sekrup.append(cm_skrup)
print("")
print(f"Hasil Mikrometer Sekrup dalam cm\nx={cm_m_sekrup[0]} cm\ny={cm_m_sekrup[1]} cm\nz={cm_m_sekrup[2]} cm")
print("")
print(f"Pengukuran berulang Mikrometer Sekrup\nx={cm_m_sekrup[0]} ± 0.005 cm\ny={cm_m_sekrup[1]} 0.005 cm\nz={cm_m_sekrup[2]} ± 0.005 cm")
with open("output1-mod1.txt", "a") as file:
    file.write(f"Hasil Mikrometer Sekrup dalam cm\nx={cm_m_sekrup[0]} cm\ny={cm_m_sekrup[1]} cm\nz={cm_m_sekrup[2]} cm\n")
    print("", file=file)
    file.write(f"Pengukuran berulang Mikrometer Sekrup\nx={cm_m_sekrup[0]} ± 0.005 cm\ny={cm_m_sekrup[1]} ± 0.005 cm\nz={cm_m_sekrup[2]} ± 0.005 cm\n")
    print("", file=file)
cm_j_sorong = []
for x in range(len(j_sorong)):
    cm_srg = float(j_sorong[x]) / 10
    cm_j_sorong.append(cm_srg)
print("")
print(f"Hasil Jangka Sorong dalam cm\nx={cm_j_sorong[0]} cm\ny={cm_j_sorong[1]} cm\nz={cm_j_sorong[2]} cm")
print("")
print(f"Pengukuran berulang Mikrometer Sekrup\nx={cm_j_sorong[0]} ± 0.005 cm\ny={cm_j_sorong[1]} 0.005 cm\nz={cm_j_sorong[2]} ± 0.005 cm")
print("")
with open("output1-mod1.txt", "a") as file:
    file.write(f"Hasil Jangka Sorong dalam cm\nx={cm_j_sorong[0]} cm\ny={cm_j_sorong[1]} cm\nz={cm_j_sorong[2]} cm\n")
    print("", file=file)
    file.write(f"Pengukuran berulang Mikrometer Sekrup\nx={cm_j_sorong[0]} ± 0.005 cm\ny={cm_j_sorong[1]} 0.005 cm\nz={cm_j_sorong[2]} ± 0.005 cm\n")
    print("", file=file)
    file.write("Pengukuran berulang Neraca O'hauss\n")
print("Pengukuran berulang Neraca O'hauss")
for x in range(len(n_ohaus)):
    print(f"Percobaan {x + 1}: {n_ohaus[x]} ± 0.005 g")
    with open("output1-mod1.txt", "a") as file:
        file.write((f"Percobaan {x + 1}: {n_ohaus[x]} ± 0.005 g\n"))
A_a_digital = []
print("")
with open("output1-mod1.txt", "a") as file:
    print("Hasil Amperemeter Digital dalam A\n", file=file)
print("Hasil Amperemeter Digital dalam A")
for x in range(len(a_digital)):
    A_dig = float(a_digital[x]) / 1000
    A_a_digital.append(A_dig)
    print(f"Percobaan {x + 1}: {A_a_digital[x]} A")
    with open("output1-mod1.txt", "a") as file:
        file.write(f"Percobaan {x + 1}: {A_a_digital[x]} A\n")
print("")
print("Pengukuran berulang Amperemeter Digital")
with open("output1-mod1.txt", "a") as file:
    print("Pengukuran berulang Amperemeter Digital\n", file=file)
for x in range(len(a_digital)):
    print(f"Percobaan {x + 1}: {A_a_digital[x]} ± 0.005 A")
    with open("output1-mod1.txt", "a") as file:
        file.write((f"Percobaan {x + 1}: {A_a_digital[x]} A\n"))
mV_V_digital = []
print("")
print("Hasil Voltmeter Digital dalam mV")
with open("output1-mod1.txt", "a") as file:
    print("Hasil Voltmeter Digital dalam mV\n", file=file)
for x in range(len(v_digital)):
    V_dig = float(v_digital[x]) * 1000
    mV_V_digital.append(V_dig)
    print(f"Percobaan {x + 1}: {mV_V_digital[x]} mV")
    with open("output1-mod1.txt", "a") as file:
        file.write((f"Percobaan {x + 1}: {mV_V_digital[x]} mV\n"))
print("")
print("Pengukuran berulang Voltmeter Digital")
with open("output1-mod1.txt", "a") as file:
    print("Pengukuran berulang Voltmeter Digital\n", file=file)
for x in range(len(v_digital)):
    print(f"Percobaan {x + 1}: {v_digital[x]} ± 0.005 V")
    with open("output1-mod1.txt", "a") as file:
        file.write((f"Percobaan {x + 1}: {v_digital[x]} ± 0.005 V\n"))
print("")
vol_p_penggaris = float(penggaris[0]) * float(penggaris[1]) * float(penggaris[2])
vol_p_j_sorong = float(cm_j_sorong[0]) * float(cm_j_sorong[1]) * float(cm_j_sorong[2])
vol_p_m_sekrup = float(cm_m_sekrup[0]) * float(cm_m_sekrup[1]) * float(cm_m_sekrup[2])
print(f"Volume pengukuran Penggaris: {vol_p_penggaris} cm")
print(f"Volume pengukuran Jangka Sorong: {vol_p_j_sorong} cm")
print(f"Volume pengukuran Mikrometer Sekrup: {vol_p_m_sekrup} cm")
with open("output1-mod1.txt", "a") as file:
    print("", file=file)
    print(f"Volume pengukuran Penggaris: {vol_p_penggaris} cm", file=file)
    print(f"Volume pengukuran Jangka Sorong: {vol_p_j_sorong} cm", file=file)
    print(f"Volume pengukuran Mikrometer Sekrup: {vol_p_m_sekrup} cm", file=file)
print("")
sum_Div_p = []
def ketidakpastian(x, y):
    v_Div_p_sum = []
    for i in range(len(y)):
        v_Div = abs(x / float(y[i])) * 0.1
        v_Div_p_sum.append(v_Div)
    sum_Div_p.append(sum(v_Div_p_sum))
ketidakpastian(vol_p_penggaris, penggaris)
print(f"Ketidakpastian pengukuran volume Penggaris: {sum_Div_p[0]}")
ketidakpastian(vol_p_j_sorong, j_sorong)
print(f"Ketidakpastian pengukuran volume Jangka Sorong: {sum_Div_p[1]}")
ketidakpastian(vol_p_m_sekrup, m_sekrup)
print(f"Ketidakpastian pengukuran volume Mikrometer Sekrup: {sum_Div_p[2]}")
with open("output1-mod1.txt", "a") as file:
    print("", file=file)
    print(f"Ketidakpastian pengukuran volume Penggaris: {sum_Div_p[0]}", file=file)
    print(f"Ketidakpastian pengukuran volume Jangka Sorong: {sum_Div_p[1]}", file=file)
    print(f"Ketidakpastian pengukuran volume Mikrometer Sekrup: {sum_Div_p[2]}", file=file)
m_jenis = []
def massa_jenis(x, y):
    m_j = float(x) / float(y)
    m_jenis.append(m_j)
print("")
massa_jenis(m_dadu, vol_p_penggaris)
print(f"Massa jenis pengukuran volume Penggaris: {m_jenis[0]} g/cm^3")
massa_jenis(m_dadu, vol_p_j_sorong)
print(f"Massa jenis pengukuran volume Jangka Sorong: {m_jenis[1]} g/cm^3")
massa_jenis(m_dadu, vol_p_m_sekrup)
print(f"Massa jenis pengukuran volume Mikrometer Sekrup: {m_jenis[2]} g/cm^3")
with open("output1-mod1.txt", "a") as file:
    print("", file=file)
    print(f"Massa jenis pengukuran volume Penggaris: {m_jenis[0]} g/cm^3", file=file)
    print(f"Massa jenis pengukuran volume Jangka Sorong: {m_jenis[1]} g/cm^3", file=file)
    print(f"Massa jenis pengukuran volume Mikrometer Sekrup: {m_jenis[2]} g/cm^3", file=file)
print("")
m_over_v_sQ = []
ketidakpastian_m_jenis = []
def m_over_v_sq(x,y):
    for i in x:
        result = abs(-(float(x) / float((y ** 2))))
        m_over_v_sQ.append(result)
m_over_v_sq(m_dadu, vol_p_penggaris)
m_over_v_sq(m_dadu, vol_p_j_sorong)
m_over_v_sq(m_dadu, vol_p_m_sekrup)
ketidakpastian_p = m_over_v_sQ[0] * sum_Div_p[0] + (1 / vol_p_penggaris) * 0.005
print(f"Ketidakpastian massa jenis Penggaris: {ketidakpastian_p}")
ketidakpastian_j = m_over_v_sQ[1] * sum_Div_p[1] + (1 / vol_p_j_sorong) * 0.005
print(f"Ketidakpastian massa jenis Jangka Sorong: {ketidakpastian_j}")
ketidakpastian_m = m_over_v_sQ[2] * sum_Div_p[2] + (1 / vol_p_m_sekrup) * 0.005
print(f"Ketidakpastian massa jenis Mikrometer Sekrup: {ketidakpastian_m}")
with open("output1-mod1.txt", "a") as file:
    print("", file=file)
    print(f"Ketidakpastian massa jenis Penggaris: {ketidakpastian_p}", file=file)
    print(f"Ketidakpastian massa jenis Jangka Sorong: {ketidakpastian_j}", file=file)
    print(f"Ketidakpastian massa jenis Mikrometer Sekrup: {ketidakpastian_m}", file=file)
def ketidakpastian_v(x):
    x1 = []
    x_sq = []
    xsum = sum(float(i) for i in x) / len(x)
    print(f"Rata-rata: {xsum}")
    for i in range(len(x)):
        result = float(x[i]) - xsum
        x1.append(result)
        result2 = result ** 2
        x_sq.append(result2)
        print(f"Percobaan {i + 1}: ({x[i]} - {xsum})^2 = {x_sq[i]}")
        with open("output1-mod1.txt", "a") as f:
            f.write(f"Percobaan {i + 1}: ({x[i]} - {xsum})^2 = {x_sq[i]}\n")
    total = (sum(x_sq) / len(x)) ** 0.5
    print(f"Hasil pengukuran berulang: {total}")
print("")
print("Pengukuran berulang Amperemeter Digital")
with open("output1-mod1.txt", "a") as f:
    print("", file=f)
    f.write(f"Pengukuran berulang Amperemeter Digital\n")
ketidakpastian_v(a_digital)
print("")
with open("output1-mod1.txt", "a") as f:
    print("", file=f)
    f.write(f"Pengukuran berulang Voltmeter Digital\n")
print("Pengukuran berulang Voltmeter Digital")
ketidakpastian_v(v_digital)
print("-----------------------------------------------------------------------------------")
print("Apakah masih ada data yang ingin dihitung dari modul 1? (ketik 1 jika iya; 2 jika tidak)")
try:
    def ask():
        ask = int(input())
        if ask == 1: 
            ask_del_outp_m1 = int(input(("Hapus file output? 1 jika iya: ")))
            if ask_del_outp_m1 == 1:
                with open("output1-mod1.txt", "w") as file:
                    file.write("")
                print("File sudah terhapus.")
            s = input("Silahkan input data terlebih dahulu lalu jika sudah pencet ENTER.") 
            call(["python", "mod1.py"])
        elif ask == 2:
            print("Apakah anda ingin menghitung data untuk modul lain? (Ketik 1 jika iya; 2 jika tidak)")
            askm2_choice = int(input())
            if askm2_choice == 1:
                print("###################################################################################")
                call(["python", "11251030-MRAIFAN-TUBES.py"])
            if askm2_choice == 2:
                print("Terima kasih sudah menggunakan alat bantu hitung praktikum fisika Institut Teknologi Kalimantan!")
    ask()
except:
    print("Error")