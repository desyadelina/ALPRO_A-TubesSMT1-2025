from subprocess import call
import sys
with open("input1-mod2.txt") as file:
    lines = file.readlines()
    V_kuningan = [x[3:10] for x in lines[1:4]]
    l_kuningan = [x[3:10] for x in lines[5:8]]
    T1_kuningan = [x[5:10] for x in lines[9:12]]
    T2_kuningan = [x[5:10] for x in lines[13:16]]
    
    V_tembaga = [x[3:10] for x in lines[18:21]]
    l_tembaga = [x[3:10] for x in lines[22:25]]
    T1_tembaga = [x[5:10] for x in lines[26:29]]
    T2_tembaga = [x[5:10] for x in lines[30:33]]
    
    V_besi = [x[3:10] for x in lines[35:38]]
    l_besi = [x[3:10] for x in lines[39:42]]
    T1_besi = [x[5:10] for x in lines[43:46]]
    T2_besi = [x[5:10] for x in lines[47:50]]
    
    V_aluminium = [x[3:10] for x in lines[52:55]]
    l_aluminium = [x[3:10] for x in lines[56:59]]
    T1_aluminium = [x[5:10] for x in lines[60:63]]
    T2_aluminium = [x[5:10] for x in lines[64:67]]
t = 240
def show_list_mod2(x):
    for a in range(len(x)):
        print(f"Percobaan {a+1}:{x[a]}")
    print("")
print("t (Waktu): 240 s")
print("")
print("V kuningan:")
show_list_mod2(V_kuningan)
print("l kuningan:")
show_list_mod2(l_kuningan)
print("T1 kuningan:")
show_list_mod2(T1_kuningan)
print("T2 kuningan:")
show_list_mod2(T2_kuningan)

print("V tembaga:")
show_list_mod2(V_tembaga)
print("l tembaga:")
show_list_mod2(l_tembaga)
print("T1 tembaga:")
show_list_mod2(T1_tembaga)
print("T2 tembaga:")
show_list_mod2(T2_tembaga)

print("V besi:")
show_list_mod2(V_besi)
print("l besi:")
show_list_mod2(l_besi)
print("T1 besi:")
show_list_mod2(T1_besi)
print("T2 besi:")
show_list_mod2(T2_besi)

print("V aluminium:")
show_list_mod2(V_aluminium)
print("l tembaga:")
show_list_mod2(l_aluminium)
print("T1 tembaga:")
show_list_mod2(T1_aluminium)
print("T2 tembaga:")
show_list_mod2(T2_aluminium)

C_kuningan = []
C_tembaga = []
C_besi = []
C_aluminium = []
for i in range(len(V_kuningan)):
    result = ((float(V_kuningan[i]) * float(l_kuningan[i]) * t) / (float(T2_kuningan[i]) - float(T1_kuningan[i])) - 1)
    C_kuningan.append(result)
    print(f"Kalor jenis kuningan {i + 1}: {C_kuningan[i] + 1} J/C")
with open("output1-mod2.txt", "w") as output:
    output.write(f"Kalor jenis kuningan {1}: {C_kuningan[0]} J/C\n")
    for i in range(len(C_kuningan) - 1):
        print(f"Kalor jenis kuningan {i + 2}: {C_kuningan[i + 1]} J/C", file=output)

for i in range(len(V_tembaga)):
    result = ((float(V_tembaga[i]) * float(l_tembaga[i]) * t) / (float(T2_tembaga[i]) - float(T1_tembaga[i])) - 1)
    C_tembaga.append(result)
    print(f"Kalor jenis tembaga {i + 1}: {C_tembaga[i]} J/C")
    with open("output1-mod2.txt", "a") as output:
        print(f"Kalor jenis tembaga {i + 1}: {C_tembaga[i]} J/C", file=output)

for i in range(len(V_besi)):
    result = ((float(V_besi[i]) * float(l_besi[i]) * t) / (float(T2_besi[i]) - float(T1_besi[i])) - 1)
    C_besi.append(result)
    print(f"Kalor jenis besi {i + 1}: {C_besi[i]} J/C")
    with open("output1-mod2.txt", "a") as output:
        print(f"Kalor jenis besi {i + 1}: {C_besi[i]} J/C", file=output)
        
for i in range(len(V_aluminium)):
    result = ((float(V_aluminium[i]) * float(l_aluminium[i]) * t) / (float(T2_aluminium[i]) - float(T1_aluminium[i])) - 1)
    C_aluminium.append(result)
    print(f"Kalor jenis aluminium {i + 1}: {C_aluminium[i]} J/C")
    with open("output1-mod2.txt", "a") as output:
        print(f"Kalor jenis aluminium {i + 1}: {C_aluminium[i]} J/C", file=output)

C_kuningan_sum = sum(C_kuningan) / len(C_kuningan)
C_tembaga_sum = sum(C_tembaga) / len(C_tembaga)
C_besi_sum = sum(C_besi) / len(C_besi)
C_aluminium_sum = sum(C_aluminium) / len(C_aluminium)
print(f"Rata-rata kalor jenis kuningan: {C_kuningan_sum}\nRata-rata kalor jenis tembaga: {C_tembaga_sum}\nRata-rata kalor jenis besi: {C_besi_sum}\nRata-rata kalor jenis aluminium: {C_aluminium_sum}")
with open("output1-mod2.txt", "a") as output:
    print(f"Rata-rata kalor jenis kuningan: {C_kuningan_sum}\nRata-rata kalor jenis tembaga: {C_tembaga_sum}\nRata-rata kalor jenis besi: {C_besi_sum}\nRata-rata kalor jenis aluminium: {C_aluminium_sum}", file=output)
pengurutan = []
pengurutan.append(C_kuningan_sum); pengurutan.append(C_tembaga_sum); pengurutan.append(C_besi_sum); pengurutan.append(C_aluminium_sum)
pengurutan_len = len(pengurutan)
for i in range(pengurutan_len-1):
  for j in range(pengurutan_len-i-1):
    if pengurutan[j] > pengurutan[j+1]:
      pengurutan[j], pengurutan[j+1] = pengurutan[j+1], pengurutan[j]
print(f"Pengurutan kalor jenis dari yang terkecil ke yang terbesar: {pengurutan}")
with open("output1-mod2.txt", "a") as output:
    print(f"Pengurutan kalor jenis dari yang terkecil ke yang terbesar: {pengurutan}", file=output)
        
print("-----------------------------------------------------------------------------------")
print("Apakah masih ada data yang ingin dihitung dari modul 2? (ketik 1 jika iya; 2 jika tidak)")
