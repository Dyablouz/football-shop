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
Pertama-tama, saya membuat 6 fungsi baru, add, detail, show_json, show_xml, show_json_by_id, show_xml_by_id dalam views.py dan menambahkan URL masing masing fungsi tersebut ke dalam urls.py. Setelah itu, saya membuat file baru forms.py agar dapat menerima data baru yang nanti akan diinput user.

Setelah itu, saya lanjut dengan membuild add.html dan detail.html pada direktori main/templates yang berguna untuk menambahkan produk dan juga detail dari produk. Saya juga merubah isi dari main.html untuk menampilkan tombol yang dapat mengakses fungsi add dan detail yang telah saya buat pada views.py yang mengarahkan user ke add.html atau detail.html.

Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada

POSTMAN

XML :
<img width="994" height="809" alt="Screenshot 2025-09-17 at 08 46 56" src="https://github.com/user-attachments/assets/084c2f90-cf5b-4466-b119-1b42265ecd0d" />

JSON :
<img width="1002" height="735" alt="Screenshot 2025-09-17 at 08 47 33" src="https://github.com/user-attachments/assets/98d00386-2b1a-4b5e-807f-8bc7348c621a" />

XML by id (1) :
<img width="993" height="601" alt="Screenshot 2025-09-17 at 08 57 32" src="https://github.com/user-attachments/assets/a712fa21-c091-4cbe-86b3-b6da93935563" />

XML by id (2) :
<img width="997" height="644" alt="Screenshot 2025-09-17 at 08 57 49" src="https://github.com/user-attachments/assets/6b39e2de-0d89-40f5-a799-f83d170608cd" />

JSON by id (1) :
<img width="990" height="731" alt="Screenshot 2025-09-17 at 08 53 31" src="https://github.com/user-attachments/assets/52ab52c6-330e-44a0-aca2-80cc0177b28e" />

JSON by id (2) :
<img width="1000" height="700" alt="Screenshot 2025-09-17 at 08 54 03" src="https://github.com/user-attachments/assets/b5529848-a5d9-46f7-9d43-37c3681c7608" />

# Tugas 4

Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah fitur bawaan yang sudah tersedia dalam Django yang dapat digunakan untuk membuat form proses user login yang memiliki dua field, username dan password. Fitur ini dikhususkan untuk memverifikasi username dan password bukan untuk menambahkan data akun baru. Ketika request terkirim, AuthenticationForm akan mengecek apakah akun dengan username tersebut ada, Jika ada, apakah passwordnya cocok, lalu cek apakah akun user aktif atau tidak.

Kelebihan : 
- Keamanan terjamin karena terdapat hashing password dan t
erdapat pengecekan status keaktifan user.
- Cepat dan praktis, cukup mengimpor saja tanpa perlu membuat logika untuk memvalidasi password/username user.

Kekurangan : 
- Mengharuskan user untuk memiliki username dalam sebuah akun, harus mengimplementasi logika sendiri jika ingin menambahkan fitur login by google.
- UI yang generik sehingga mengharuskan kita untuk customize pesan error untuk menyesuaikan dengan platformnya.

Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses verifikasi identitas dari user. Sementara itu, otorisasi adalah proses pengecekan hak akses user. Setelah identitas Anda terverifikasi, otorisasi akan menentukan izin apa saja yang Anda miliki.

Lebih jelasnya, Autentikasi seperti ditanya “Siapa anda?” sedangkan otorisasi seperti ditanya “Anda boleh melakukan apa saja?”. 

Di Django, kedua konsep ini diimplementasikan melalui aplikasi django.contrib.auth. Autentikasi ditangani dengan memvalidasi username dan password pengguna terhadap model User dan mengelola sesi login. Sedangkan otorisasi diimplementasikan menggunakan permission framework bawaannya, yang memungkinkan pemberian izin spesifik kepada user atau grup. 

Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Cookies disimpan di browser, sementara session menyimpan data nya di server. Kelebihan utama cookies adalah tidak membebani server dan cocok untuk data non-sensitif seperti preferensi tema. Namun, kekurangannya adalah tidak aman karena data bisa dibaca dan dimanipulasi oleh pengguna, ukurannya sangat terbatas, dan selalu dikirim pada setiap request yang bisa memboroskan bandwidth.

Sebaliknya, kelebihan utama session adalah jauh lebih aman karena data sensitif tersimpan di server dan klien hanya memegang ID unik. Kapasitas penyimpanannya juga jauh lebih besar. Kekurangannya, session membebani memori server karena harus menyimpan data untuk setiap pengguna aktif, yang dapat menjadi masalah pada website dengan traffic yang tinggi.


Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tidak, penggunaan cookies tidak aman secara default. Karena disimpan sebagai teks biasa di browser klien, mereka sangat rawan terhadap pencurian. Resiko utamanya meliputi Cross-Site Scripting (XSS), di mana skrip jahat pada sebuah situs dapat mencuri cookie pengguna, dan Cross-Site Request Forgery (CSRF), di mana situs berbahaya menipu browser pengguna untuk mengirimkan request yang tidak diinginkan ke situs lain tempat pengguna sedang login, dengan cookie autentikasi yang terkirim secara otomatis.

Django menangani resiko ini dengan sangat baik melalui beberapa lapisan keamanan bawaan. Untuk melawan CSRF, Django memiliki middleware yang mewajibkan adanya token rahasia dan unik ({% csrf_token %}) pada setiap request POST. Untuk keamanan data, framework session Django secara default menyimpan semua data sensitif di sisi server dan hanya mengirim cookie berisi ID acak ke klien. Cookie ini juga ditandatangani secara kriptografis untuk mencegah manipulasi dan secara default diatur sebagai HttpOnly, yang mencegahnya diakses oleh JavaScript dan secara signifikan mengurangi risiko pencurian via XSS.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama-tama, saya buat fungsi register, login, logout di dalam views.py untuk memungkinkan user mengakses websitenya sesuai dengan status login/logoutnya. Saat menambahkan 3 fungsi baru tersebut, tampilan file .html juga sekaligus diupdate untuk tombol yang digunakan untuk register, login dan logout nya. Selain itu, update urls.py untuk menambahkan path urls yang baru. Fungsi show_main() dan add() juga dimodifikasi agar hanya bisa diakses setelah user login dengan akunnya. Kemudian, saya menambahkan cookie untuk user yang baru saja login dan dihapus jika user sudah logout.

Setelah itu, saya menghubungkan model Product dengan User dengan 'from django.contrib.auth.models import User' lalu menambahkan 'user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)' pada class Product.

<<<<<<< HEAD

# Tugas 5

Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika terdapat beberapa CSS selector pada suatu elemen HTML, algoritma akan memeriksa prioritas atribut untuk menentukan yang mana yang akan dipakai. Prioritas pertama adalah yang memiliki Origin & Importance tertinggi, di mana style dari developer dengan !important memiliki kekuatan paling besar. Jika prioritas ini sama, maka browser akan menghitung Selector Specificity, di mana ID selector lebih kuat daripada class selector, dan class selector lebih kuat daripada element selector. Jika hal tersebut juga masih sama, maka aturan yang menang adalah yang didefinisikan terakhir atau paling bawah dalam kode CSS, yang dikenal sebagai Order of Appearance. Terakhir, jika tidak ada aturan yang cocok, elemen akan mewarisi style dari induknya atau menggunakan nilai default dari browser.

Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design sangat penting karena web dapat diakses dari berbagai macam ukuran layar dan kepadatan piksel. Tanpa design responsive, tampilan web akan pecah, sulit dibaca, dan pengguna akan merasa tidak nyaman menggunakannya. Contoh aplikasi yang sudah responsif adalah seperti shopee.com yang memiliki tampilan responsif tergantung dari device pengguna. Untuk yang belum responsif, contoh nya bisa dilihat dari SIAKNG pada tampilan loginnya yang tidak menyesuaikan dengan layar dari device pengguna.

Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Dalam CSS, margin, border, dan padding adalah properti yang mengatur ruang di sekitar sebuah elemen. Perbedaan utamanya terletak pada lokasinya, Margin adalah ruang transparan di luar elemen yang berfungsi untuk memberi jarak antar elemen. Border adalah garis yang mengelilingi elemen, tepat di antara margin dan padding. Sementara itu, Padding adalah ruang transparan di dalam elemen yang memberikan jarak antara konten (seperti teks atau gambar) dengan bordernya. Contoh penggunaannya : margin: 20px; border: 2px solid red; dan padding: 10px.

Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox adalah model layout satu dimensi dalam CSS. Flexbox memudahkan kita untuk meratakan elemen ke kiri/kanan/tengah, memberi jarak antar elemen yang rapi dan membuat item mengecil sesuai space tersisa. Karena fokusnya satu dimensi, flexbox cocok untuk komponen seperti navbar, kartu-kartu produk dalam satu baris, tombol-tombol, atau form yang perlu perataan dan distribusi ruang yang rapi.

Grid Layout adalah model layout dua dimensi dalam CSS. Grid memudahkan kita menyusun elemen dalam baris dan kolom, mengatur ukuran/jarak tiap track, serta menempatkan item pada area tertentu (bisa melebar beberapa kolom atau baris). Karena fokusnya dua dimensi, grid cocok untuk kerangka halaman seperti header–sidebar–konten–footer, galeri gambar, atau dashboard yang butuh struktur rapi dan responsif pada dua arah.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Pertama-tama, dimulai dulu dengan membuat fungsi baru yaitu edit_product untuk mengubah isi/data dari product yang telah ditambahkan dan dibuat file .html nya untuk halaman user mengupdate data. Selain itu, juga membuat fungsi delete_product dan membuat kedua fitur tersebut dapat diakses di halaman home dan memastikan hanya product yang dimiliki oleh user yang sedang login sekarang yang dapat diedit/hapus. 

Kemudian saya menambahkan global.css untuk mendesain komponen form agar semua form memiliki tema yang sama. Setelah itu, saya membuat satu file html baru lagi yaitu navbar.html untuk navigation bar. Setelah itu, saya styling semua file html agar seragam dengan tema yang saya pilih yaitu hitam putih dicampur dengan warna merah. Untuk format masing masing file, saya mengikuti format dari tutorial 4 namun untuk detail.html, saya merubah beberapa hal agar semua informasi tentang product dapat langsung terlihat user ketika tombol “Description” ditekan.

Dan untuk step terakhir, saya menambahkan sebuah gambar yang akan ditampilkan ketika product di website football-shop sedang tidak ada sama sekali.
=======
# Tugas 4

Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah fitur bawaan yang sudah tersedia dalam Django yang dapat digunakan untuk membuat form proses user login yang memiliki dua field, username dan password. Fitur ini dikhususkan untuk memverifikasi username dan password bukan untuk menambahkan data akun baru. Ketika request terkirim, AuthenticationForm akan mengecek apakah akun dengan username tersebut ada, Jika ada, apakah passwordnya cocok, lalu cek apakah akun user aktif atau tidak.

Kelebihan :

Keamanan terjamin karena terdapat hashing password dan t erdapat pengecekan status keaktifan user.
Cepat dan praktis, cukup mengimpor saja tanpa perlu membuat logika untuk memvalidasi password/username user.
Kekurangan :

Mengharuskan user untuk memiliki username dalam sebuah akun, harus mengimplementasi logika sendiri jika ingin menambahkan fitur login by google.
UI yang generik sehingga mengharuskan kita untuk customize pesan error untuk menyesuaikan dengan platformnya.
Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses verifikasi identitas dari user. Sementara itu, otorisasi adalah proses pengecekan hak akses user. Setelah identitas Anda terverifikasi, otorisasi akan menentukan izin apa saja yang Anda miliki.

Lebih jelasnya, Autentikasi seperti ditanya “Siapa anda?” sedangkan otorisasi seperti ditanya “Anda boleh melakukan apa saja?”.

Di Django, kedua konsep ini diimplementasikan melalui aplikasi django.contrib.auth. Autentikasi ditangani dengan memvalidasi username dan password pengguna terhadap model User dan mengelola sesi login. Sedangkan otorisasi diimplementasikan menggunakan permission framework bawaannya, yang memungkinkan pemberian izin spesifik kepada user atau grup.

Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Cookies disimpan di browser, sementara session menyimpan data nya di server. Kelebihan utama cookies adalah tidak membebani server dan cocok untuk data non-sensitif seperti preferensi tema. Namun, kekurangannya adalah tidak aman karena data bisa dibaca dan dimanipulasi oleh pengguna, ukurannya sangat terbatas, dan selalu dikirim pada setiap request yang bisa memboroskan bandwidth.

Sebaliknya, kelebihan utama session adalah jauh lebih aman karena data sensitif tersimpan di server dan klien hanya memegang ID unik. Kapasitas penyimpanannya juga jauh lebih besar. Kekurangannya, session membebani memori server karena harus menyimpan data untuk setiap pengguna aktif, yang dapat menjadi masalah pada website dengan traffic yang tinggi.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tidak, penggunaan cookies tidak aman secara default. Karena disimpan sebagai teks biasa di browser klien, mereka sangat rawan terhadap pencurian. Resiko utamanya meliputi Cross-Site Scripting (XSS), di mana skrip jahat pada sebuah situs dapat mencuri cookie pengguna, dan Cross-Site Request Forgery (CSRF), di mana situs berbahaya menipu browser pengguna untuk mengirimkan request yang tidak diinginkan ke situs lain tempat pengguna sedang login, dengan cookie autentikasi yang terkirim secara otomatis.

Django menangani resiko ini dengan sangat baik melalui beberapa lapisan keamanan bawaan. Untuk melawan CSRF, Django memiliki middleware yang mewajibkan adanya token rahasia dan unik ({% csrf_token %}) pada setiap request POST. Untuk keamanan data, framework session Django secara default menyimpan semua data sensitif di sisi server dan hanya mengirim cookie berisi ID acak ke klien. Cookie ini juga ditandatangani secara kriptografis untuk mencegah manipulasi dan secara default diatur sebagai HttpOnly, yang mencegahnya diakses oleh JavaScript dan secara signifikan mengurangi risiko pencurian via XSS.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama-tama, saya buat fungsi register, login, logout di dalam views.py untuk memungkinkan user mengakses websitenya sesuai dengan status login/logoutnya. Saat menambahkan 3 fungsi baru tersebut, tampilan file .html juga sekaligus diupdate untuk tombol yang digunakan untuk register, login dan logout nya. Selain itu, update urls.py untuk menambahkan path urls yang baru. Fungsi show_main() dan add() juga dimodifikasi agar hanya bisa diakses setelah user login dengan akunnya. Kemudian, saya menambahkan cookie untuk user yang baru saja login dan dihapus jika user sudah logout.

Setelah itu, saya menghubungkan model Product dengan User dengan 'from django.contrib.auth.models import User' lalu menambahkan 'user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)' pada class Product.

# Tugas 5
>>>>>>> 5974b82 (Tugas 5)
