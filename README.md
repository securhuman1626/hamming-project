# Hamming SEC-DED Simülatörü

Bu proje, BLM230 **Bilgisayar Mimarisi** dersi kapsamında geliştirilmiştir.  
Projenin amacı, Hamming SEC-DED (Single Error Correcting, Double Error Detecting) algoritmasını kullanarak bit hatalarını tespit edip düzeltmektir.

## 🔍 Proje Özeti

- 8, 16 veya 32 bitlik veri girişi yapılabilir.
- Girilen veriye **Hamming kodu** hesaplanır ve gösterilir.
- Kullanıcı bir bit pozisyonu belirleyerek yapay hata oluşturabilir.
- Hatalı kod üzerinden sendrom değeri hesaplanarak **tek bit hatası düzeltilir**, çift bit hatası ise **tespit edilir**.
- Tüm işlemler kullanıcı dostu bir **Tkinter arayüzü** üzerinden gerçekleştirilir.

## 🎮 Özellikler

✅ Bit verisi girme  
✅ Hamming SEC-DED kodu üretme  
✅ Hatalı bit enjekte etme  
✅ Hata tespiti ve düzeltme  
✅ Görsel kullanıcı arayüzü (GUI)

## 📺 Proje Tanıtım Videosu

[![Hamming SEC-DED Simülatörü Tanıtım Videosu](https://img.youtube.com/vi/euzm4p7dx68/0.jpg)](https://www.youtube.com/watch?v=euzm4p7dx68)

Proje ile ilgili detayları ve kullanımını videodan izleyebilirsiniz.

## 🖥️ Ekran Görüntüsü

![Ekran Görüntüsü](ekran1.png)

## 🚀 Nasıl Çalıştırılır?

1. [Python](https://www.python.org/downloads/) 3.10+ sürümünü kur.
2. Aşağıdaki komutla programı çalıştır:

```bash
python hamming_sim.py
