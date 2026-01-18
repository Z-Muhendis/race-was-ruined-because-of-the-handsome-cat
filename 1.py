import tkinter as tk
import time
from tkinter import messagebox
from PIL import Image, ImageTk

pencere=tk.Tk()
# Çıktı Çevirisi: Yakışıklı spikerimiz -> Our Handsome Announcer
tk.Label(text="Our Handsome Announcer", font=("Arial",135)).pack()

logo = tk.PhotoImage(file="tipe bak tipe.png").subsample(2, 2)
etiket = tk.Label(pencere, image=logo)  
etiket.image = logo    
etiket.pack()

# Çıktı Çevirisi: Sonuçlar -> Results
tk.Label(text="Results", font=("Arial",50)).pack()

a=tk.Listbox(pencere,width=60,height=6)
# Araba isimleri İngilizce versiyonlarıyla güncellendi
a.insert(1,"1. Lamborghini")
a.insert(2,"2. Fiat")
a.insert(3,"3. Audi")
a.insert(4,"4. Old Reliable (Tofaş)")
a.pack()

# Mesaj kutuları çevirileri
messagebox.showinfo("STARTING!","3...")
messagebox.showinfo("STARTING!","2...")
messagebox.showinfo("STARTING!","1...")
messagebox.showinfo("STARTED!","GO!")

time.sleep(1)
a.delete(0, tk.END)
a.insert(1,"1. Fiat")
a.insert(2,"2. Lamborghini")
a.insert(3,"3. Audi")
a.insert(4,"4. Old Reliable")
messagebox.showwarning("WARNING","7 SECONDS UNTIL THE FINISH!")

time.sleep(1)
a.delete(0, tk.END)
a.insert(1,"1. Fiat")
a.insert(2,"2. Audi")
a.insert(3,"3. Lamborghini")
a.insert(4,"4. Old Reliable")
messagebox.showwarning("WARNING","6 SECONDS UNTIL THE FINISH!")

# ... (Aradaki saniyeler aynı mantıkla "SECONDS UNTIL THE FINISH!" olarak değişecek)

time.sleep(1)
a.delete(0, tk.END)
a.insert(1,"1. Lamborghini")
a.insert(2,"2. Old Reliable")
a.insert(3,"3. Audi")
a.insert(4,"4. Fiat")
messagebox.showwarning("WARNING","1 SECOND UNTIL THE FINISH!")

# Yeni gelişme çevirisi
messagebox.showinfo("New!","The Handsome Cat has entered the track and joined the race!")

time.sleep(1)
a.delete(0, tk.END)
a.insert(1,"1. Old Reliable")
a.insert(2,"2. Lamborghini")
a.insert(3,"3. Fiat")
a.insert(4,"4. Audi")
a.insert(5,"5. Handsome Announcer")

messagebox.showwarning("WARNING","0.1 SECONDS UNTIL THE FINISH!")

# Hata mesajı çevirisi
messagebox.showerror("Error","What is this?! THE HANDSOME ANNOUNCER FINISHED THE LAP IN 0.1 SECONDS!!!???")

a.delete(0, tk.END)
a.insert(1,"1. Handsome Announcer")
a.insert(2,"2. Old Reliable")
a.insert(3,"3. Lamborghini")
a.insert(4,"4. Audi")
a.insert(5,"5. Fiat")

time.sleep(1)
# Sonuç ekranı çevirisi
messagebox.showinfo("Final Results", "Handsome Announcer 1st (all girls love him), Old Reliable 2nd, Lamborghini 3rd, Audi 4th, Fiat 5th.")

# Görsel değiştirme
yeni_logo = tk.PhotoImage(file="Yakışıklı kedi yakıyo.png").subsample(2, 2)
etiket.config(image=yeni_logo)
etiket.image = yeni_logo
