Nama : Nabila Maharani Putri
NPM  : 2306275191
Tugas: Tugas Individu 1 PBP 2024

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! 
 Saya mengimplementasikan satu persatu checklist dengan mengerjakan kembali apa yang dikerjakan di tutorial 0 dan tutorial 1. Pada pengerjaannya saya sambil memahami untuk apa step step tersebut dilakukan. Selain itu, saya menyesuaikan penamaan project, penamaan app, dan juga atribut yang digunakan. Berikut step by stepnya:
 > Membuat sebuah proyek Django baru: 
 Langkah ini saya mulai dengan membuat direktori baru dengan nama floemin (nama e-commerce saya) dan mengaktifkan virtual environment pada direktori ini. 
 > Membuat aplikasi dengan nama main pada proyek tersebut: 
 Saya membuat app baru bernama main dan mendaftaarkannya ke dalam list INSTALLED_APPS di setting.py.
 > Melakukan routing pada proyek agar dapat menjalankan aplikasi main: 
 Saya configure routingnya dengan membuat file urls.py di direktori app main dan menambahkan rute tersebut di urls.py project.
 > Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib(name, price, description): 
 Saya menambahkan atribut atribut tersebut sesuai dengan tipe datanya. setelah itu, saya lakukan makemigration dan migrate.
 > Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu:
 Saya menambahkan nama app, nama saya, dan kelas ke dalam dict yang ada di views.py
 > Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py:
 Saya memanggil function show_main yang ada di views.py
 > Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet: 
 Saya mendeploy ke PWS dengan bantuan dockerfile yang diberikan oleh asdos saya. 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
 ![Bagan Alur] (bagan.jpg)
 Setelah request masuk, URL nya akan dicocokkan dengan pola yang ada di urls.py. Jika cocok, akan dicek izinnya, apakah boleh diakses atau tidak. Jika boleh, akan dipanggil function yg sesuai di views.py. Jika tampilan tersebut membutuhkan data dari database, views.py akan berinteraksi dengan models.py. Setelah data diproses, views.py akan merender template HTML untuk ditampilkan ke client

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
 Git berfungsi sebagai sistem kontrol versi dari kode yang kita buat. Hal tersebut memungkinkan kita untuk melihat perubahan kode dari versi ke versi, bekerja dengan programmer lain pada satu waktu tanpa conflict, dan memudahkan mengembalikan kode ke versi sebelumnya jika terjadi kesalahan.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
 Django dipilih karena mudah dipahami untuk pemula, punya struktur MVT yang membuat pengembangan lebih ter-organize.

5. Mengapa model pada Django disebut sebagai ORM?
 Model pada django disebut Object Relational Mapping (ORM) karena memungkinkan kita untuk berinteraksi dengan database menggunakan object python. Pada models.py, didefinisikan struktur data dan relasi antar data yang kemudian diterjemahkan menjadi tabel di database