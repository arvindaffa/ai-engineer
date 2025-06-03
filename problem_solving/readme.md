# Sistem Deteksi Fraud Reimbursement Internal Perusahaan

## Deskripsi
Proyek ini bertujuan mengembangkan sistem AI/ML untuk mendeteksi dan mencegah aktivitas kecurangan pada proses reimbursement di perusahaan. Kasus yang ditangani meliputi:
- Manipulasi nota/klaim palsu
- Fraud penggunaan kartu kredit yang bukan untuk kepentingan perusahaan

## Usulan Model
- Autoencoder
Digunakan untuk deteksi anomali pada klaim nota palsu. Model ini dilatih hanya dengan data transaksi valid (tidak fraud). Anomali terdeteksi berdasarkan error rekonstruksi input oleh model.
- Isolation Forest
Digunakan untuk deteksi fraud pada transaksi kartu kredit. Model ini bersifat unsupervised dan efektif mengisolasi transaksi yang berbeda jauh dari pola normal tanpa memerlukan label fraud.

## Data yang diperlukan
- Autoencoder:
Data transaksi klaim yang dipastikan valid, mencakup nominal klaim, kategori pengeluaran, dan informasi vendor.
- Isolation Forest:
Data transaksi kartu kredit, meliputi nominal transaksi, tipe transaksi, dan merchant.

## Cara Penerapan
- Sistem menyediakan dua input pilihan deteksi fraud:
- Deteksi manipulasi nota/klaim palsu
- Deteksi fraud kartu kredit
- Berdasarkan pilihan, data input diarahkan ke model yang sesuai (Autoencoder atau Isolation Forest).
- Output berupa prediksi fraud atau tidak fraud.
- Model dapat di-deploy sebagai microservice terpisah atau dipanggil melalui file model .pkl.

## Infrastruktur yang diperlukan
- Server dengan kapasitas penyimpanan dan komputasi yang memadai untuk menyimpan dan menjalankan model AI.
- API atau service endpoint untuk menerima data input dan memberikan hasil prediksi secara real-time.
- Sistem penyimpanan data transaksi dan klaim yang terintegrasi dengan sistem AI.
