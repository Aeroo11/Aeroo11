# Efan Ramdhani

**Mahasiswa ITS dengan fokus AI engineering.**

Saya membangun pipeline data, mengevaluasi model, dan membuat aplikasi
agar hasilnya bisa diperiksa.

## Coba proyek saya

### KANAL | Tebak kanal berita

**Pilih judul untuk membuka prediksi model.** Satu dari dua contoh ini meleset.

<details>
<summary>Persib melaju ke final setelah menang lewat adu penalti</summary>

**KANAL memilih olahraga dengan skor 29,26%.**

</details>

<details>
<summary>Bank Indonesia pertahankan suku bunga acuan</summary>

**KANAL memilih teknologi dengan skor 36,02%.** Judul ini lebih cocok masuk kanal
**ekonomi**. Contoh ini menunjukkan kesalahan yang bisa muncul meskipun
modelnya mengungguli baseline pada data uji.

</details>

**Macro-F1 0,420** pada 517 artikel uji temporal. Baseline kelas mayoritas
mencapai **0,026**. [Studi kasus dan demo Docker](https://github.com/Aeroo11/kanal-berita-dashboard/blob/main/docs/portfolio.md) | [Dataset publik](https://huggingface.co/datasets/aeroo11/kanal-berita)

### TokenWatch | Ubah routing model LLM

Apa yang terjadi pada biaya jika separuh trafik dari endpoint *summarize*
dialihkan ke model lain? Buka simulator, pilih model tujuan, lalu geser
porsi trafik ke **50%**. Proyeksi dihitung dari trafik simulasi.

[**Buka simulator TokenWatch**](https://llm-cost-dashboard-omega.vercel.app/?view=simulator) | [Telusuri anomali biaya](https://llm-cost-dashboard-omega.vercel.app/?view=anomalies)

<details>
<summary>Lihat tampilan simulator</summary>

<a href="https://llm-cost-dashboard-omega.vercel.app/?view=simulator"><img width="640" alt="Simulator TokenWatch yang mengalihkan 50 persen trafik summarize dan membandingkan proyeksi biaya dengan baseline" src="https://raw.githubusercontent.com/Aeroo11/LLM-Cost-Dashboard/e63b6d0b531fdf1bea88b29cfe74f533d3115af2/docs/screenshot-simulator.png"></a>

[Kode dan catatan teknis](https://github.com/Aeroo11/LLM-Cost-Dashboard)

</details>

### Faktura | Periksa selisih invoice

Pemasok menagih **100 unit**, sementara bukti penerimaan mencatat **80 unit**.

<details>
<summary>Lihat keputusan Faktura</summary>

**Perlu peninjauan.** Pengecekan kuantitas menemukan selisih 20 unit, sehingga
invoice masuk antrean peninjauan dengan status *business exception*.

</details>

Skenario ini menggambarkan aturan pencocokan Faktura. Pada evaluasi invoice
sintetis, Faktura mendeteksi **99 dari 99 anomali**. [Proyek dan hasil evaluasi](https://github.com/Aeroo11/faktura/blob/main/README.id.md)

**Stack utama** Python, SQL, DuckDB, dbt, FastAPI, Next.js, dan Docker.

<details>
<summary>Proyek lain</summary>

- [Dashboard IDX](https://github.com/Aeroo11/Dashboard_IDX) untuk screening saham BEI, jurnal, dan backtest.
- [share.yow](https://github.com/Aeroo11/shareyow) untuk membagi pengeluaran bersama dan menyimpan transaksi secara offline.

</details>

<details>
<summary>Aktivitas kontribusi</summary>

![Grafik kontribusi GitHub dalam 12 bulan terakhir](assets/kontribusi.svg)

[Pembaruan grafik melalui GitHub Actions](.github/workflows/kontribusi.yml)

</details>
