# Tugas 2

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama tama, saya membuat direktori utama terlebih dahulu, yaitu football-shop, memastikan terminal sudah berada di direktori football-shop dan menjalankan
python3 -m venv env
dan
source env/bin/activate
setelah itu, membuat requirements.txt dan menjalankan django-admin startproject football_shop . dan membuat file .env dan .env.prod
Memodifikasi settings.py dengan menambahkan 
import os
from dotenv import load_dotenv
Load environment variables from .env file
load_dotenv()

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'

// Database configuration
if PRODUCTION:
    # Production: gunakan PostgreSQL dengan kredensial dari environment variables
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'OPTIONS': {
                'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
            }
        }
    }
else:
    // Development: gunakan SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

Dengan langkah langkah tersebut, saya sudah berhasil menjalankan server Django pada folder football-shop.

Setelah berhasil, saya menjalankan 'python manage.py startapp main' untuk membuat aplikasi baru bernama main, dan mendaftarkannya ke 'INSTALLED APPS', menambahkan
file main.html pada aplikasi main dan mengisi models.py dengan name, price, description, thumbnail, category, is_featured.
Setelah itu, saya menambahkan fungsi
def show_main(request):
    context = {
        'app_name': 'Football Shop',
        'nama' : 'Fernando Lawrence',
        'kelas': 'PBP B',
    }

    return render(request, "main.html", context)

  untuk mengembalikan nilai nilai dari nama, kelas dan nama aplikasi saya kepada main.html.

  untuk memetakan fungsi yang telah dibuat pada views.py, saya menambahkan
  
from .views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
Sehingga ketika ada permintaan masuk ke URL utama aplikasi, permintaan tersebut dapat diarahkan dengan benar ke fungsi show_main.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

<img width="963" height="525" alt="Screenshot 2025-09-10 at 09 59 19" src="https://github.com/user-attachments/assets/59afaa92-d64f-4918-bcd2-bab18f16d1ff" />


Jelaskan peran settings.py dalam proyek Django!
File settings.py adalah pusat kendali atau logika utama untuk seluruh projek Django.

Bagaimana cara kerja migrasi database di Django?
Proses migrasi terdiri dari dua langkah :
Langkah pertama, python manage.py makemigrations, Perintah ini membandingkan models.py saat ini dengan versi terakhir yang disimpan. 
Jika ada perubahan, Django akan membuat file baru di dalam folder migrations/.

Langkah kedua, python manage.py migrate, Perintah ini membaca semua file instruksi di dalam folder migrations/ yang belum dijalankan, 
lalu mengeksekusinya untuk mengubah struktur database yang sebenarnya.


Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering direkomendasikan untuk permulaan dalam pembelajaran pengembangan perangkat lunak karena fitur fitur yang terdapat di Django
sangat banyak dan siap dipakai sehingga mempermudah orang untuk fokus memperdalam kemampuan mereka dengan produktif dan efisien tanpa perlu
mengulangi hal hal yang sama hanya untuk membuat suatu hal karena sudah disediakan oleh Django.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Komentar dari asdos membantu saya membantu saya untuk lebih teliti lagi dengan apa yang sedang saya kerjakan





# Tugas 3

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena proses ini adalah fondasi yang membuat platform dari yang hanya sekedar kerangka kosong menjadi sebuah sistem yang fungsional dan bernilai. Tanpa adanya data delivery, platform tidak akan memiliki informasi informasi yang menjadi bahan untuk memanfaatkan fitur fitur pada platform.

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, tidak bisa dinilai secara langsung apakah XML atau JSON yang lebih baik karena ini akan bergantung dengan konteks penggunaannya. Semisal JSON yang sekarang menjadi lebih populer dibandingkan XML karena formatnya yang lebih ringkas, rapi dan lebih mudah untuk dibaca oleh orang. Selain itu, size dari file JSON juga lebih kecil dibandingkan XML. Namun, walau begitu, XML tetap memiliki peran penting dalam penggunaan di skenario yang lebih kompleks seperti untuk data yang berorientasi pada dokumen serta dalam lingkungan korporat yang memerlukan validasi skema yang ketat dan fitur canggih seperti namespace untuk mencegah konflik data. Sehingga tidak bisa secara mutlak menyatakan XML atau JSON lebih baik daripada yang lainnya.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi sebagai untuk menjalankan serangkaian proses validasi dan pembersihan data yang dikirim oleh user secara otomatis. Kita sangat membutuhkan method ini karena is_valid() sangat penting untuk menjaga keamanan aplikasi. is_valid() secara efektif memeriksa setiap input terhadap aturan yang telah ditetapkan—mulai dari tipe data yang benar hingga batasan spesifik—sekaligus membersihkan potensi yang berbahaya.

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan {% csrf_token %} saat membuat form di Django sebagai fitur keamanan dasar untuk mencegah serangan Cross-Site Request Forgery (CSRF), yang pada dasarnya memastikan bahwa setiap permintaan yang mengubah data benar-benar berasal dari user yang sadar di dalam situs kita.
Tanpa csrf_token, sebuah aplikasi menjadi rentan karena hanya mengandalkan cookie sesi untuk otentikasi, padahal browser akan secara otomatis melampirkan cookie tersebut ke setiap permintaan ke domain terkait, tidak peduli apakah permintaan itu berasal dari situs asli atau dari situs berbahaya. Hal ini dapat dimanfaatkan oleh penyerang dengan cara menipu user yang sedang login untuk mengunjungi situs mereka sendiri, di mana sebuah form tersembunyi secara otomatis mengirimkan permintaan palsu untuk menipu user lewat platform kita.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama-tama, saya membuat folder templates pada direktori football_shop yang berisi base.html sebagai template dasar dari halaman web yang nanti akan saya buat. Lalu saya tambahkan 

Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada
