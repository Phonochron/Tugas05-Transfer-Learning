# Transfer Learning dengan ResNet-18

**Tugas 05 — Advanced CNNs and Transfer Learning**  
Andrew Wijaya · NIM **2802508363** · BINUS University

Perbandingan scratch, feature extraction, dan fine-tuning pada **1.981 citra dari 10 ras Oxford-IIIT Pet**, termasuk kontrol data augmentation.

## Hasil eksperimen

| Kondisi | Strategi | Validation accuracy | Test Macro F1 |
| --- | --- | ---: | ---: |
| B1 | Scratch | 40,40% | 0,3550 |
| B2 | Feature extraction | 92,93% | 0,9132 |
| B3 | Fine-tuning + augmentasi | 96,30% | 0,9363 |
| B4 | Fine-tuning tanpa augmentasi | 94,95% | 0,9331 |

**Model terpilih: B4**, berdasarkan validation loss terendah (**0,184115**). Test set digunakan untuk evaluasi akhir.

Protokol: split stratified 70/15/15, seed 42, input 224 × 224, batch 32, AdamW, dan early stopping patience 5. Training aktual menggunakan **CPU**; hasil berasal dari satu seed.

## Berkas utama

| Berkas | Isi |
| --- | --- |
| [Laporan PDF](Laporan_Tugas05_2802508363_AndrewWijaya.pdf) | Analisis konseptual, hasil, grafik, hipotesis, dan referensi; 5 halaman |
| [Notebook training](Tugas05_Transfer_Learning_Colab.ipynb) | Kode B1–B4 dan output Colab asli |
| [Notebook verifikasi](Verifikasi_Hasil.ipynb) | Pemeriksaan metrik dari log; sudah dieksekusi lokal |
| [raw_logs/](raw_logs/) · [figures/](figures/) | Log per epoch, prediksi test, konfigurasi, dan visualisasi |
| [Analisis kesalahan](failure_analysis_reviewed.csv) | Bukti visual dan hipotesis delapan misklasifikasi |

## Menjalankan

**Training di Colab:** buka notebook training, pilih **T4 GPU**, lalu **Run all** untuk mengulang eksperimen. Output dari run sebelumnya sudah tersimpan.

**Verifikasi lokal:** jalankan dari folder repositori.

```bash
python -m pip install -r requirements-verification.txt
python verify_artifacts.py
```

Untuk menghitung ulang metrik dan melihat grafik, jalankan `Verifikasi_Hasil.ipynb`. Versi dependency training asli tercatat di `requirements.txt`.

## Referensi dan atribusi

- [Batch Normalization — Ioffe & Szegedy](https://proceedings.mlr.press/v37/ioffe15.html)
- [Deep Residual Learning — He et al.](https://arxiv.org/abs/1512.03385)
- [Transfer Learning Tutorial — PyTorch](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)

ChatGPT dan Codex membantu review kode, penyusunan laporan, dan pemeriksaan artefak. AI disclosure lengkap tercantum dalam laporan.

**Akses:** repositori private; berikan akses kepada penilai saat pengumpulan.
