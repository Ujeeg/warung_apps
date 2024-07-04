import pandas as pd
from tabulate import tabulate

def read_data(data):
    df = pd.read_csv(data)
    return df

data_barang = "data_barang.csv"
data_penjualan = "data_penjualan.csv"
df_barang = read_data(data_barang)
df_penjualan = read_data(data_penjualan)

line_1 = "---------------------------------------------------------------------------"
line_2 = "==========================================================================="

# change interface from dataFarame into tabulate
def table_to_tabualte(df):
    table = tabulate(df, headers='keys', tablefmt='grid')
    return table
    
# Ineterface Main Menu
def interface_main_menu():
    print(f"""{line_1}
                    Selamat Datang di Toko Fajar
{line_2}
                            Main Menu
{line_2}
          1. Daftar Barang
          2. Menu Penjualan
          3. Admin 
          4. Exit
{line_1}
          
""")

# interface menu Daftar Barang
def interface_daftar_barang():
    print(f"""
    {line_1}
                            Selamat Datang di Toko Fajar
    {line_1}
    {table_to_tabualte(df_barang)}
    {line_1}
    1. Cari Barang Berdasarkan Nama
    2. Cari Barang Berdasarkan Kode
    0. Back to Main Menu         
    """)
    while True:
        try:   
            input_daftar_barang = int(input("Input 0 utuk kembali ke Main Menu :"))
            if input_daftar_barang == 0:
                return # Kembali ke main_menu() karena fungsi interface_daftar_barang() dipanggil di dalam loop
            elif input_daftar_barang == 1:
                filtering_by_name(df_barang)
            elif input_daftar_barang == 2:
                filtering_by_kode(df_barang)
            else:
                print("Input tida valid")
        except ValueError:
            print("Input yang dimasukan tidak sesuai")
        
         
    
# interface Admin
def interface_Admin():
    print(f"""
{line_1}
                        Selamat Datang di Toko Fajar
{line_1}
        1. Tambah Barang
        2. Hapus Barang
        0. Back to Main Menu
{line_1}
""")
    while True :
        try :
            input_menu_admin = int(input("Masukan Input 0 - 2 : "))
            if input_menu_admin == 1:
                tambah_barang(df_barang)
            # elif input_menu_admin == 2:
            #     hapus_barang()
            # elif input_menu_admin == 3:
            #     ganti barang()
            elif input_menu_admin == 0:
                return
            else:
                print("input yang dimasukan tidak ada")
        except ValueError:
            print("Masukan Angka")

# interface Menu Penjualan
def interface_menu_penualan():
        print(f"""
{line_1}
                        Selamat Datang di Toko Fajar
{line_1}
"Masukan kode Barang"
"Masukan Jumlah Barang"
{line_1}

          
""")

# filtering data berdasarkan nama
def filtering_by_name(df_barang):
    search_term = str(input("Masukan Kata kunci barang yang dicari : "))
    condition = df_barang["Nama Barang"].str.contains(search_term, case=False)
    hasil = df_barang[condition]
    print(table_to_tabualte(hasil))

# filtering data berdasarkan kode
def filtering_by_kode(df_barang):
    search_term = str(input("Masukan Kata kunci barang yang dicari : "))
    condition = df_barang["Kode Barang"].str.contains(search_term, case=False)
    hasil = df_barang[condition]
    print(table_to_tabualte(hasil))


# menambah barang 
def tambah_barang(df_barang):
    kode_barang = str(input("Masukan Kode Barang : "))
    nama_barang = str(input("Masukan Nama Barang : "))
    harga_beli = int(input("Masukan Harga Beli : "))
    harga_jual = int(input("Masukan Harga Jual : "))
    
    data_baru = pd.DataFrame({
        'Kode Barang': [kode_barang],
        'Nama Barang': [nama_barang],
        'Harga Beli': [harga_beli],
        'Harga Jual': [harga_jual]
    })
    
    # Concatenate the existing DataFrame with the new row DataFrame
    df_barang = pd.concat([df_barang, data_baru], ignore_index=True)
    
    print("Barang berhasil ditambahkan!")
    
    return df_barang


def main_menu():
    
    # Main Menu Loop
    while True:
        interface_main_menu()
        try :
            input_main_menu = int(input("Masukan Menu Pilihan dengan angka 0 - 3 :"))
            if input_main_menu == 1:
                interface_daftar_barang()
            elif input_main_menu == 2:
                interface_menu_penualan()
            elif input_main_menu == 3:
                interface_Admin()
            elif input_main_menu == 0:
                break 
            else:
                print("Input yang dimasukan tidak sesuai")
        except ValueError:
            print("Input yang dimasukan Harus Berupa Angka 0 - 3")



main_menu()
