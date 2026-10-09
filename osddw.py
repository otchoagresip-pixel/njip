sapa = (input('halo selamat datang di pesta najip, yang boleh masuk hanya orang orang dengan ketentuan ukuran kontol seperti 15+ dan ada perlakuan spesial jika panjang kontol kw di atas 50. bagaimana? enter huruf apa aja untuk lanjut. silahkan masukan huruf : '))
warna_kontol = (input('silahkan masukan warna kontol (putih/hitam) : '))
panjang_kontol = int(input('masukan panjang kntl lu ajg : '))

if warna_kontol == 'hitam' :
    print('kontpl kok hitam')
    if panjang_kontol <15 :
        print('KONTOL UDAH HITTAM KECIL PULAK, PERGI KW BERGURU DULU SAMA NAJIP')
else : 
    if panjang_kontol >=50 :
        print('KONTOL NAJIP') 
    else :
        if panjang_kontol > 15 :
            print('oiyaya silahkan masuk')
        else :
            print('goblok kontol kecil sok sok-an anjing berguru dulu sama najip dkk sana')
        
        