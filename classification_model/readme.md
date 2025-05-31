# Deskripsi
Proyek ini bertujuan untuk mengklasifikasikan pesan pelanggan dari perusahaan ISP ke dalam tiga kategori:
- Information: permintaan info produk, billing, status registrasi, promo, dll.
- Request: permintaan layanan seperti terminasi, relokasi, reset password, upgrade paket, dll.
- Problem: pengaduan masalah seperti koneksi lambat, modem rusak, kuota tidak reset, dll.

Dataset berisi 2000 pertanyaan pelanggan yang telah dilakukan labeling secara manual.

# Metode
- Preprocessing:
  - Menghapus duplikat
  - Memfilter label unknown
- Ekstraksi fitur: Menggunakan TF-IDF Vectorizer dengan stopwords bahasa Indonesia
- Algoritma: Linear Support Vector Classifier ()
- Evaluasi: Stratified 5-Fold Validation (akurasi, presisi, recall)

# Hasil Evaluasi (Rata-rata dari 5 Fold)
- Akurasi: ±94.27%
- Presisi: ±92.96%
- Recall: ±91.22%

# Langkah Instalasi
1. Clone repository
2. Buat virtual environment (opsional)
3. Install dependencies: pip install -r requirements.txt

# Cara Menjalankan Model
1. Jalankan file `code.py` untuk training ulang dan evaluasi model
2. Atau gunakan model yang sudah disimpan (`text_classifier_pipeline.pkl`) untuk prediksi
3. Buka file tes.py dan ganti nilai variabel 'question' untuk diklasifikasikan 
