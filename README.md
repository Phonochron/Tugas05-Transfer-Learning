# Tugas 05 - Advanced CNNs and Transfer Learning

**Andrew Wijaya | NIM 2802508363 | BINUS University**

Repositori private: https://github.com/Phonochron/Tugas05-Transfer-Learning
Pastikan penilai memperoleh akses repositori ketika menyerahkan tautan.

Paket berisi laporan lima halaman, kode training, hasil eksperimen B1-B4,
dan notebook pemeriksaan hasil yang sudah dieksekusi secara lokal.

## Isi paket

- `Laporan_Tugas05_2802508363_AndrewWijaya.pdf`: Bagian A dan C, grafik, delapan hipotesis, referensi dan AI disclosure.
- `Tugas05_Transfer_Learning_Colab.ipynb`: implementasi training Colab beserta output asli dari notebook yang dikirim mahasiswa.
- `Verifikasi_Hasil.ipynb`: verifikasi CSV aktual; memiliki output eksekusi lokal.
- `raw_logs/`: history, prediksi, metrik, manifest, protocol dan environment asli.
- `failure_analysis_reviewed.csv`: delapan hipotesis; CSV mentah asli tetap dipertahankan.
- `figures/`: gambar hasil eksperimen asli.
- `requirements.txt`: versi dependency training asli, termasuk index CPU resmi.
- `requirements-verification.txt`: dependency untuk pemeriksaan hasil tanpa PyTorch.

## Hasil utama

| Kondisi | Validation accuracy | Test Macro F1 |
| --- | --- | --- |
| B1 scratch | 40,40% | 0,3550 |
| B2 feature extraction | 92,93% | 0,9132 |
| B3 fine-tuning + augmentasi | 96,30% | 0,9363 |
| B4 tanpa augmentasi | 94,95% | 0,9331 |

Model terpilih adalah B4_no_aug berdasarkan validation loss minimum (0,184115).
Test tidak dipakai untuk memilih ulang model. Training menggunakan CPU, seed 42.
B5 dan Grad-CAM tidak dijalankan karena opsional.

## Menjalankan

Training: upload notebook training ke Colab, pilih T4 GPU, lalu Run all bila ingin
mengulang eksperimen. Pengulangan dapat menghasilkan angka berbeda dari log yang dilampirkan.

Verifikasi tanpa training: install `requirements-verification.txt`, buka
`Verifikasi_Hasil.ipynb` dari folder paket, lalu Run all. Notebook ini sudah dijalankan
untuk menghitung ulang accuracy/F1 dan memeriksa history, split, serta delta augmentasi.

## Status bukti notebook training

Notebook training dengan output asli telah tersedia dan dimasukkan ke paket.
Output mencakup environment, split, konfigurasi B1-B4, tabel metrik test, kurva,
confusion matrix dan delapan sampel kesalahan. Angkanya cocok dengan raw_logs/.
Execution count pada ekspor Colab kosong; nilai tersebut dipertahankan, tidak direkayasa.
Notebook verifikasi merupakan audit artefak tambahan, bukan pengganti training.

## Integritas dan referensi

Metrik dan gambar berasal dari ZIP hasil eksperimen aktual. ChatGPT dan Codex
digunakan untuk review kode, penyusunan draf laporan dan hipotesis, serta audit artefak.
Mahasiswa perlu memahami kode dan meninjau analisis secara mandiri sebelum pengumpulan.

- Ioffe & Szegedy, Batch Normalization (2015): https://proceedings.mlr.press/v37/ioffe15.html
- He et al., Deep Residual Learning (2016): https://arxiv.org/abs/1512.03385
- Yosinski et al., How transferable are features (2014): https://arxiv.org/abs/1411.1792
- Howard & Ruder, ULMFiT (2018): https://arxiv.org/abs/1801.06146
- PyTorch Transfer Learning Tutorial: https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

Materi slide telah diperiksa: augmentasi berada pada Slide 20-22; Slide 23 adalah
pembuka Modern Architectures. Perbedaan dengan rujukan pertanyaan tugas dijelaskan dalam laporan.

## Audit paket

Jalankan `python verify_artifacts.py` untuk memeriksa hash artefak dan syntax notebook.
