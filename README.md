# Cara Menjalankan Gathering dari kedua data
## Pertama jika menggunakan colab install environmentt yan diperlukan
!pip install streamlit
!pip install pyngrok
!pip install plotly_express
## copy saja coding untuk pembuat app.py
Hal ini digunakan untuk dapat berjalan di locahost

## jalankan code dengan Perintah dibawah
Setelah app.py jadi jalankan streamlit di localhost
from pyngrok import ngrok
import time

Menjalankan Streamlit app (Saya menggunakan NPX localturner dikarenakan tidakbisa dibuka secara langsung)
!streamlit run app.py & npx localtunnel --port 850

# kalo tidak bisa diklik dengan local host? Saya berikan Gambar juga biar urutan jelas....
klik pada bagian yang berada pada lingkaran mearah, lalu copy External URL
pada bagian yang berada pada lingkaran merah nnti akan dimasukkan kedalam link, masukkan link yang telah dicopy lalu hapus https:// dan hapus nomor setelah:(contoh terdapat pada gambar1)
Setelah itu sudah jadi deh dashboardnya 
yeayyyy
