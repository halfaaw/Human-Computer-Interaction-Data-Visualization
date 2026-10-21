# Studi Kasus Sesi 5: Human-Computer Interaction & Data Visualization

## 1. Latar Belakang
PT Maju Bersama (perusahaan fiktif) ingin merancang dasbor analitik penjualan yang intuitif, bersih dari elemen dekoratif berlebihan (*chartjunk*), serta memenuhi prinsip *User-Centered Design* (UCD). Berdasarkan evaluasi antarmuka sebelumnya, banyak pengguna mengalami kebingungan karena tata letak yang tidak terstruktur dan visualisasi yang menyesatkan. Studi kasus ini membangun skrip Python untuk memproses data penjualan sekaligus menghasilkan grafik visualisasi data yang bersih dan efektif.

Keterkaitan dengan seminar: Proyek ini terinspirasi dari materi *"Human-Computer Interaction & Data Visualization"* oleh Bapak Arafat Febrian Dirza, Ph.D. (Badan Riset dan Inovasi Nasional - BRIN). Seminar tersebut menekankan pentingnya analisis kebutuhan pengguna (*user needs*), hukum Gestalt dalam desain antarmuka, prinsip *data-ink ratio* (menghindari *chartjunk*), serta penerapan visualisasi data interaktif untuk mendukung pengambilan keputusan yang presisi.

## 2. Tujuan
- Menerapkan prinsip *User-Centered Design* (UCD) melalui pemahaman kebutuhan data analitik pengguna.
- Membersihkan dan menyiapkan data penjualan (*data preparation*) agar siap divisualisasikan.
- Membuat visualisasi data (seperti *Bar Chart* dan *Line Chart*) menggunakan Python (`matplotlib` dan `pandas`) yang bersih dari elemen dekoratif yang tidak perlu (*chartjunk*).
- Menyimpan hasil visualisasi secara otomatis ke dalam folder *output* untuk laporan eksekutif.
- Menuliskan batasan bahwa antarmuka visual dan grafik terbaik tetap memerlukan pengujian kegunaan (*usability testing*) secara langsung dengan pengguna nyata.

## 3. Data
File `data/sales_dashboard_data.csv` berisi data sintetis kategori produk dan total penjualan untuk keperluan latihan visualisasi, bukan data finansial perusahaan sungguhan. Setiap baris mewakili ringkasan penjualan per kategori.

| Kolom | Arti |
|---|---|
| `category` | Kategori produk (misal: Elektronik, Pakaian, Makanan, Perabot) |
| `total_sales` | Total nilai penjualan dalam mata uang tertentu |
| `transaction_count` | Jumlah total transaksi yang tercatat |

Konsep yang digunakan:
- *Data-Ink Ratio*: Memaksimalkan proporsi tinta yang benar-benar membawa informasi data (menghilangkan grid berlebihan dan efek 3D).
- *Visual Hierarchy*: Menggunakan warna yang konsisten dan kontras untuk menyoroti kategori penjualan tertinggi.
- *Evaluation*: Memastikan grafik mudah dibaca dalam waktu kurang dari 5 detik (*pre-attentive attributes*).

## 4. Struktur Proyek
studi-kasus-sesi-5-hci-dataviz/
├── data/
│   └── sales_dashboard_data.csv
├── src/
│   └── dataviz_dashboard.py
├── tests/
│   └── test_dataviz.py
├── outputs/
│   └── charts/             # Grafik visualisasi disimpan otomatis di sini
├── README.md
└── requirements.txt
