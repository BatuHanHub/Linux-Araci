# DEB/UBUNTU 

from komutlar import *
from tkinter import *
from tkinter import filedialog,messagebox
import sys
import os

def cik():
    sys.exit()
    
def github():
    messagebox.showinfo('Github','Github sayfam : BatuHanHub')
    
def komutlar():
    with open('Komutlar.txt', 'w', encoding='utf8') as dosya:
        dosya.write('''Kaynak Komutlar
                    
Paket kurmak   : sudo apt-get install paket-adi
Program Kurmak : sudo dpkg -i paket-adi.deb     
Güncelleştirmeler : LC_ALL=C sudo apt update && sudo apt upgrade''')
        messagebox.showinfo('Başarılı','Kaynak komutları yazı dosyasını okuyarak öğrenebilirsiniz.')

def paketKurSayfa():
    global geriDonButtonFrame, geriButton, paketbuttonFrame, paketButtonlariFrame
    
    guncelleButton.pack_forget()
    indirButton.pack_forget()
    paketKurButton.pack_forget()
    
    indirbuttonFrame.place_forget()
    paketbuttonFrame.place_forget()
    guncellebuttonFrame.place_forget()
    
    paketButtonlariFrame = Frame(pencere, bg='#DEDEDE')
    paketButtonlariFrame.place(relx=0.01,rely=0.06,relwidth=0.98, relheight= 0.85)
    
    btn_vlc = Button(paketButtonlariFrame, text='VLC -medya oynatıcısı', font=('arial 15'), width=90, command=vlc)
    btn_firefox = Button(paketButtonlariFrame, text='Firefox -internet tarayıcısı', font=('arial 15'), width=90, command=firefox)
    btn_neofetch = Button(paketButtonlariFrame, text='Neofetch -terminal uygulaması', font=('arial 15'), width=90, command=neofetch)
    btn_htop = Button(paketButtonlariFrame, text='Htop -terminal uygulaması', font=('arial 15'), width=90, command=htop)
    btn_wine = Button(paketButtonlariFrame, text='Wine -uyumluluk katmanı', font=('arial 15'), width=90, command=wine)
    btn_flatpak = Button(paketButtonlariFrame, text='Flatpak -uygulama mağazası', font=('arial 15'), width=90, command=flatpak)
    
    paketler = [btn_wine,btn_firefox,btn_htop,btn_neofetch,btn_vlc,btn_flatpak]

    for paket in paketler:
        paket.pack(side=TOP)
    
    geriDonButtonFrame = Frame(pencere, bg='black')
    geriDonButtonFrame.place(relx=0.35,rely=0.92,relwidth=0.29, relheight= 0.07)
    
    geriButton = Button(geriDonButtonFrame,text='Geri Dön', font=('arial 20 bold'),bg='white',fg='orange',activebackground='orange',
                        activeforeground='white', command=geriDon)
    
    geriButton.pack(side=BOTTOM)
    
def geriDon():
    geriDonButtonFrame.place_forget()
    geriButton.place_forget()
    paketButtonlariFrame.place_forget()
    
    guncelleButton.pack()
    indirButton.pack()
    paketKurButton.pack()
    
    indirbuttonFrame.place(relx=0.35,rely=0.1,relwidth=0.30, relheight= 0.20)
    paketbuttonFrame.place(relx=0.69,rely=0.1,relwidth=0.30, relheight= 0.20)
    guncellebuttonFrame.place(relx=0.01,rely=0.1,relwidth=0.30, relheight= 0.20)
    

pencere = Tk()
pencere.title('Linux aracı')
pencere.iconbitmap('tux.ico')
pencere.geometry('800x500')
pencere.resizable(width=False, height=False)
pencere.configure(bg='black')

guncellebuttonFrame = Frame(pencere)
guncellebuttonFrame.place(relx=0.01,rely=0.1,relwidth=0.30, relheight= 0.20)

indirbuttonFrame = Frame(pencere)
indirbuttonFrame.place(relx=0.35,rely=0.1,relwidth=0.30, relheight= 0.20)

paketbuttonFrame = Frame(pencere)
paketbuttonFrame.place(relx=0.69,rely=0.1,relwidth=0.30, relheight= 0.20)

ustFrame = Frame(pencere)
ustFrame.place(relx=0.0,rely=0.0,relwidth=1, relheight= 0.05)


guncelleButton = Button(guncellebuttonFrame, text='Güncelle', font=('arial 40 bold'),bg='white',fg='orange',activebackground='orange',
                        activeforeground='white', command=guncelle)

indirButton = Button(indirbuttonFrame, text='Program\nİndir', font=('arial 36 bold'),bg='white',fg='orange',activebackground='orange',
                        activeforeground='white', command=uygulamaİndir)

paketKurButton = Button(paketbuttonFrame, text='Paket Kur', font=('arial 38 bold'),bg='white',fg='orange',activebackground='orange',
                        activeforeground='white', command=paketKurSayfa)

guncelleButton.pack()
indirButton.pack()
paketKurButton.pack()

ustKomutlar = Button(ustFrame,text='Komutlar',font=('arial 13 bold'), command=komutlar)
ustKomutlar.pack(side=LEFT)

ustCikis = Button(ustFrame,text='Çık',font=('arial 13 bold'), command=cik)
ustCikis.pack(side=RIGHT)

ustGithub = Button(ustFrame,text='Github',font=('arial 13 bold'), command=github)
ustGithub.pack(side=RIGHT)

pencere.mainloop()