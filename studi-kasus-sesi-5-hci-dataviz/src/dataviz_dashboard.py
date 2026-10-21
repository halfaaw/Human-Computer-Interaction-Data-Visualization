import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    print("=== Memulai Pemrosesan Data & Visualisasi Dashboard HCI ===")
    
    # 1. SETUP DIREKTORI OUTPUT
    os.makedirs("outputs/charts", exist_ok=True)
    
    # 2. LOAD DATA
    try:
        df = pd.read_csv("data/sales_dashboard_data.csv")
    except FileNotFoundError:
        print("Error: File data/sales_dashboard_data.csv tidak ditemukan.")
        return

    # 3. ANALISIS DATA RINGKAS
    print("\nRingkasan Data Penjualan:")
    print(df)
    
    total_revenue = df['total_sales'].sum()
    print(f"\nTotal Pendapatan Keseluruhan: Rp {total_revenue:,}")
    
    # 4. PEMBUATAN VISUALISASI BERSIH (Prinsip Data-Ink Ratio & Menghindari Chartjunk)
    fig, ax = plt.subplots(figsize=(9, 5))
    
    # Menggunakan warna profesional dan konsisten
    bars = ax.bar(df['category'], df['total_sales'] / 1e6, color='#1e3a8a', width=0.6)
    
    # Mengatur label dan judul (Clean Design)
    ax.set_title('Total Penjualan per Kategori Produk (dalam Juta Rupiah)', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Kategori Produk', fontsize=11, labelpad=10)
    ax.set_ylabel('Total Penjualan (Juta Rp)', fontsize=11, labelpad=10)
    
    # Menghilangkan border atas dan kanan untuk mengurangi chartjunk (Prinsip Tufte)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Menambahkan grid vertikal tipis saja
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Menambahkan nilai di atas batang grafik untuk keterbacaan instan (Pre-attentive)
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'Rp {height:.1f}M',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='semibold')

    plt.tight_layout()
    
    # 5. MENYIMPAN GRAFIK KE FOLDER OUTPUTS
    output_path = "outputs/charts/sales_bar_chart.png"
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    print(f"\nVisualisasi berhasil dibuat dan disimpan di '{output_path}'.")

if __name__ == "__main__":
    main()
