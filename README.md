# Cara Menjalankan Gathering dari kedua data
## Pertama jika menggunakan colab install environmentt yan diperlukan
!pip install streamlit
!pip install pyngrok
## copy saja coding untuk pembuat app.py
Hal ini digunakan untuk dapat berjalan di locahost

## jalankan code dengan Perintah dibawah
Setelah app.py jadi jalankan streamlit di localhost
from pyngrok import ngrok
import time

Menjalankan Streamlit app (Saya menggunakan NPX localturner dikarenakan tidakbisa dibuka secara langsung)
!streamlit run app.py & npx localtunnel --port 850

# kalo tidak bisa diklik dengan local host?
klik pada bagian yang digaris bawah, lalu copy External URL
pada bagian yang digaris bawah nnti akan dimasukkan kedalam link, masukka link yang telah dicopy lalu hapus https:// dan hapus nomor setelah:
Setelah itu sudah jadi deh dashboarnya 
yeayyyy
