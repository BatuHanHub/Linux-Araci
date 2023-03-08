from tkinter import filedialog,messagebox
from tkinter import *
import os

### PAKETLER ###

class paketler():
    
    def __init__(self, paketAdi, paketİndirmeKomutu):
        self.paketAdi = paketAdi
        self.paketİndirmeKomutu = paketİndirmeKomutu

    def __str__(self):
        return str(self.paketAdi, self.paketİndirmeKomutu)
    
    def indir(self):
        print(self.paketİndirmeKomutu)
        # os.system(self.paketİndirmeKomutu)

pkt_neofetch = paketler('neofetch','sudo apt install neofetch')
pkt_htop = paketler('htop','sudo apt install htop')
pkt_wine = paketler('wine','sudo apt install wine')
pkt_firefox = paketler('firefox','sudo apt install firefox')
pkt_vlc = paketler('vlc','sudo apt install vlc')
pkt_flatpak = paketler('flatpak','sudo apt install flatpak')

def neofetch():
    os.system(pkt_neofetch.paketİndirmeKomutu)

def vlc():
    os.system(pkt_vlc.paketİndirmeKomutu)
    
def htop():
    os.system(pkt_htop.paketİndirmeKomutu)

def wine():
    os.system(pkt_wine.paketİndirmeKomutu)

def firefox():
    os.system(pkt_firefox.paketİndirmeKomutu)

def vlc():
    os.system(pkt_vlc.paketİndirmeKomutu)

def flatpak():
    os.system(pkt_flatpak.paketİndirmeKomutu)
    
### diğerleri ###

def guncelle():
    os.system('LC_ALL=C sudo apt update && sudo apt upgrade')
    messagebox.showinfo('Başarılı Güncelleme','Güncellemeler başarıyla tamamlandı.')

def uygulamaİndir():
    uygulama = filedialog.askopenfilename(initialdir="/", title="Kuracağınız uygulamayı seçiniz",
                                          filetypes=(("Debian dosyası", "*.deb*"),("Tüm Dosyalar", "*.*")))
    
    os.system(f'sudo dpkg -i {uygulama}')

# print(pkt_vlc.paketİndirmeKomutu)

# def neofetch():
#     os.system('sudo apt install neofetch')
    
# def htop():
#     os.system('sudo apt install htop')
    
# def wine():
#     os.system('sudo apt install wine')

# def firefox():
#     os.system('sudo apt install firefox')

# def vlc():
#     os.system('sudo apt install vlc')
    
# def flatpak():
#     os.system('sudo apt install flatpak')