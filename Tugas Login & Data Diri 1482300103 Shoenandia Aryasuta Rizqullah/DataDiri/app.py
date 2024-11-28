from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia Anda

@app.route('/')
def index():
    # Contoh data diri
    data = {
        "nama": "Shoenandia Aryasuta Rizqullah",
        "tanggal_lahir": "28 Agustus 2025",
        "jenis_kelamin": "Laki-laki",
        "kewarganegaraan": "Indonesia",
        "pekerjaan": "Software Developer",
        "email": "Shoenandiaarya@gmail.com",
        "telepon": "+62 0857 4542 2345",
        "alamat": "Jl. Merdeka No. 123, Jakarta",
        "pendidikan": [
            {"institusi": "Universitas 17 Agustus 1945 Surabaya", "jurusan": "Sistem Dan Teknologi Informasi", "tahun": "2022 - 2024"},
            {"institusi": "SMA ", "jurusan": "Bahasa", "tahun": "2019 - 2020"}
        ],
        "pengalaman": [
            {"perusahaan": "PT Teknologi A", "posisi": "Backend Developer", "tahun": "2020 - 2024"},
            {"perusahaan": "Startup B", "posisi": "Software Engineer", "tahun": "2020 - 2023"}
        ],
        "keahlian": ["Python"],
        "proyek": [
            {"judul": "Sistem E-commerce", "deskripsi": "Mengembangkan backend untuk platform e-commerce skala besar."},
            {"judul": "Aplikasi Manajemen Keuangan", "deskripsi": "Membangun aplikasi berbasis web untuk mengelola keuangan personal."}
        ],
        "sertifikasi": [
            {"nama": "AWS Certified Solutions Architect", "tahun": "2021"},
            {"nama": "Google Cloud Professional Engineer", "tahun": "2022"}
        ],
        "media_sosial": {
            "YouTube": "https://www.youtube.com/live/4KaUsIAWJPA?si=v2q7a3He1Xdl6e_d",
            "github": "https://github.com/johndoe",
            "instagram": "https://twitter.com/johndoe"
        },
        "hobi": ["Editing", "Fotografi", "Video Game"]
    }

    flash('Data berhasil dimuat!')  # Contoh pesan flash
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)