from functools import total_ordering

def vend():

    a = {'kode': 'F1', 'item': 'Keripik Kentang', 'harga': 15000, 'stock': 2,'pesan':1}
    b = {'kode': 'F2', 'item': 'Keripik Pisang', 'harga': 18000, 'stock': 1,'pesan':1}
    c = {'kode': 'F3', 'item': 'Kerupuk Udang', 'harga': 20000, 'stock': 3,'pesan':1}
    d = {'kode': 'F4', 'item': 'Biskuit', 'harga': 12000, 'stock': 1,'pesan':1}
    e = {'kode': 'F5', 'item': 'Wafer', 'harga': 11000, 'stock': 3,'pesan':1}
    f = {'kode': 'F6', 'item': 'Lolipop', 'harga': 10000, 'stock': 2,'pesan':1}
    g = {'kode': 'F7', 'item': 'Permen Jagung', 'harga': 2000, 'stock': 1,'pesan':1}
    h = {'kode': 'F8', 'item': 'Mi Instan', 'harga': 14000, 'stock': 3,'pesan':1}
    i = {'kode': 'F9', 'item': 'Coklat', 'harga': 21000, 'stock': 1,'pesan':1}
    j = {'kode': 'F10', 'item': 'Popcorn', 'harga': 16000, 'stock': 3,'pesan':1}
    k = {'kode': 'D1', 'item': 'Soda', 'harga': 9000, 'stock': 2,'pesan':1}
    l = {'kode': 'D2', 'item': 'Susu Coklat', 'harga': 7000, 'stock': 1,'pesan':1}
    m = {'kode': 'D3', 'item': 'Susu Vanila', 'harga': 8000, 'stock': 3,'pesan':1}
    n = {'kode': 'D4', 'item': 'Teh Jasmine', 'harga': 4000, 'stock': 1,'pesan':1}
    o = {'kode': 'D5', 'item': 'Teh Oolong', 'harga': 5000, 'stock': 3,'pesan':1}
    p = {'kode': 'D6', 'item': 'Teh Tarik', 'harga': 6000, 'stock': 2,'pesan':1}
    q = {'kode': 'D7', 'item': 'Kopi Luwak', 'harga': 17000, 'stock': 1,'pesan':1}
    r = {'kode': 'D8', 'item': 'Minuman Isotonik', 'harga': 13000, 'stock': 3,'pesan':1}
    s = {'kode': 'D9', 'item': 'Air Mineral', 'harga': 3000, 'stock': 1,'pesan':1}
    t = {'kode': 'D10', 'item': 'Americano', 'harga': 19000, 'stock': 3,'pesan':1}
    items = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t]
    cart = []
    total = []

    def cetakStruk(uang):
        print('*'*30)
        print(' '*12 + 'STRUK' + ' '*10)
        print('*'*30)
        print('List Pembelian : ')
        x=1
        for item in cart:
            print(str(x) + '. %s x %d : %d' %(item['item'],item['pesan'],item['harga']*item['pesan']))  # type: ignore
            x+=1
        print('*'*30)
        print('Total : ' + str(sum(total)))
        print('Tunai : '+str(uang))
        print('Kembalian : '+str(uang-sum(total)))
        print('Terima kasih, semoga harimu menyenangkan!\n')


    print('Welcome to Vending Machine! \n***************')

    # Menampilkan items dan harga
    def show(items):
        print('\nitems available \n***************')
    
        for item in items:      
            if item.get('stock') == 0:
                items.remove(item)
        for item in items:
            print(item.get('kode'), item.get('item'), item.get('harga'))
       
        
        print('***************\n')
    continueToBuy = True
    # User memilih item
    cim = int(input('Masukkan uang: '))
    while continueToBuy == True:
        show(items)
        Terpilih = input('Pilih item: ')
        for kode in items:
            allHarga = []
            allHarga.append(kode['harga'])
            uang = cim-sum(total) 
            if Terpilih == kode.get('kode'):
                Terpilih = kode
                if((uang-kode['harga']) < 0):
                    print('Maaf Uang Anda Kurang')
                    continue
                if uang>0:
                    for i in cart:
                        if i == Terpilih:
                            cart.remove(cart[-1])
                            total.remove(total[-1])
                            kode['pesan'] += 1
                            
                    print('Anda memilih ' + kode['item'])
                    kode['stock'] -= 1
                    
                    cart.append(kode)
                    total.append(kode['harga']*kode['pesan'])
                    
                    sisa = uang-kode['harga']
                    print('sisa uang: ' + str(sisa))
                    a = input('Apakah Anda ingin membeli item lain? (y/n): ')
                    if a == 'n':
                        continueToBuy = False             
                    else:
                        continue
                elif(uang<min(allHarga)):
                    print('Maaf Uang Anda Kurang') 
                    continueToBuy = False 
    print(cart)
    print(total)      
    cetakStruk(cim)
vend()
