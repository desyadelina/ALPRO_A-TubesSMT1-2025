from subprocess import call
import sys
print("")
print("###################################################################################")
print("\033[95mALAT BANTU HITUNG MODUL PRAKTIKUM FISIKA SEMESTER 1 INSTITUT TEKNOLOGI KALIMANTAN\033[0m")
print("###################################################################################")
print("Silahkan pilih modul yang ingin dikerjakan:")
print("1. Dasar Pengukuran dan Ketidakpastian")
print("2. Kalorimeter")
print("###################################################################################")
inp = True
while inp == True:
    try:
        modul = int(input("Pilih modul yang ingin dikerjakan: "))
        if modul == 1:
            print("-----------------------------------------------------------------------------------")
            print("\033[94mModul 1: Dasar Pengukuran dan Ketidakpastian\033[0m")
            print("-----------------------------------------------------------------------------------")
            call(["python", "mod1.py"])
            inp = False
            sys.exit(0)
        elif modul == 2:
            print("-----------------------------------------------------------------------------------")
            print("\033[94mModul 2: Kalorimeter\033[0m")
            print("-----------------------------------------------------------------------------------")
            call(["python", "mod2.py"])
            inp = False
            sys.exit(0)
        else:
            print("-----------------------------------------------------------------------------------")
            print("\033[91mPilih antara modul 1 - 2!\033[0m")
            print("-----------------------------------------------------------------------------------")
    except ValueError:
        print("-----------------------------------------------------------------------------------")
        print("\033[91mPilih antara modul 1 - 2!\033[0m")
        print("-----------------------------------------------------------------------------------")
        continue

