import tkinter as tk
from tkinter import messagebox

# Hamming SEC-DED için yardımcı fonksiyonlar

def calculate_hamming(data_bits):
    m = len(data_bits)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1

    hamming_code = ['0'] * (m + r + 1)
    j = 0
    for i in range(1, len(hamming_code)):
        if (i & (i - 1)) == 0:  # 2^n olanlar parity bit
            continue
        hamming_code[i] = data_bits[j]
        j += 1

    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, len(hamming_code)):
            if j & parity_pos:
                parity ^= int(hamming_code[j])
        hamming_code[parity_pos] = str(parity)

    overall_parity = sum([int(b) for b in hamming_code[1:]]) % 2
    hamming_code[0] = str(overall_parity)
    return ''.join(hamming_code)

def detect_and_correct(code):
    code = list(code)
    n = len(code)
    r = 0
    while (2 ** r) < n:
        r += 1

    syndrome = 0
    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, n):
            if j & parity_pos:
                parity ^= int(code[j])
        if parity != int(code[parity_pos]):
            syndrome += parity_pos

    overall_parity = sum([int(b) for b in code[1:]]) % 2
    if overall_parity != int(code[0]):
        if syndrome == 0:
            return code, "Çift bit hatası tespit edildi. Düzeltilemez."
        else:
            code[syndrome] = str(1 - int(code[syndrome]))
            return ''.join(code), f"Tek bit hatası {syndrome}. bitteydi, düzeltildi."
    else:
        if syndrome != 0:
            return code, f"Sendrom var ama parity yok, hata çelişkili."
        return ''.join(code), "Hata yok."

# Arayüz fonksiyonları

def encode_data():
    raw = entry.get().strip()
    if not all(c in '01' for c in raw):
        messagebox.showerror("Hata", "Sadece 0 ve 1 giriniz.")
        return
    global encoded
    encoded = calculate_hamming(raw)
    result_label.config(text=f"Hamming Kodu: {encoded}")

def inject_error():
    if not encoded:
        messagebox.showerror("Hata", "Önce veri kodlaması yapınız.")
        return
    try:
        pos = int(error_entry.get())
    except:
        messagebox.showerror("Hata", "Pozisyon sayısal olmalıdır.")
        return
    if pos < 0 or pos >= len(encoded):
        messagebox.showerror("Hata", f"Geçersiz bit pozisyonu. 0-{len(encoded)-1} arası girin.")
        return
    corrupted = list(encoded)
    corrupted[pos] = str(1 - int(corrupted[pos]))
    corrupted_label.config(text=f"Hatalı Kod: {''.join(corrupted)}")
    global corrupted_data
    corrupted_data = ''.join(corrupted)

def correct_error():
    if not corrupted_data:
        messagebox.showerror("Hata", "Önce hatalı veri oluşturun.")
        return
    corrected, msg = detect_and_correct(corrupted_data)
    correction_label.config(text=f"Düzeltme Sonucu: {corrected}\nMesaj: {msg}")

# GUI oluştur

root = tk.Tk()
root.title("Hamming SEC-DED Simülatörü")

tk.Label(root, text="Veri (örn: 10110010)").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Hamming Kodla", command=encode_data).pack()
result_label = tk.Label(root, text="")
result_label.pack()

tk.Label(root, text="Hata Oluştur (bit pozisyonu):").pack()
error_entry = tk.Entry(root)
error_entry.pack()

tk.Button(root, text="Hata Enjekte Et", command=inject_error).pack()
corrupted_label = tk.Label(root, text="")
corrupted_label.pack()

tk.Button(root, text="Hataları Tespit ve Düzelt", command=correct_error).pack()
correction_label = tk.Label(root, text="")
correction_label.pack()

encoded = ""
corrupted_data = ""

root.mainloop()
