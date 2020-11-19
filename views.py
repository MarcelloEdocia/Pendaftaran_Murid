from os import system

def print_menu():
	system("title PENDAFTARAN MURID DI SEKOLAH HARAPAN BANGSA")
	system("cls")
	system("color 9")
	tampilan1 = """
		SELAMAT DATANG PARA HARAPAN BANGSA!!	

		----------------------
		PENDAFTARAN MURID BARU
		----------------------
		[a]. Pendaftaran untuk murid baru
		[b]. Lihat semua murid yang sudah mendaftar
		[c]. Pencarian murid
		[d]. Informasi lain" tentang sekolah
		[e]. Data pribadi murid --> admin only
		[f]. Keluar
		
		"""
	print(tampilan1)

def informasi_sekolah():
	system("cls")
	print("""
		APAKAH YANG INGIN DICARI:
		[a]. Yayasan pendiri sekolah
		[b]. Ketua umum yayasan sekolah
		[c]. Pengurus unit yayasan sekolah
		[d]. Kepala sekolah
		[e]. Akreditasi dan status bangunan sekolah
		[f]. Situs sekolah
		[g]. Bantuan lain		""")
	pilihan = input("pilihlah diatas [a/b/c/d]").lower()
	if pilihan == "a":
		tampilan2 = """
		SEKOLAH HARAPAN BANGSA
		--------------------------------
		Pendiri: Yayasan Harapan bangsa
		--------------------------------
		"""
		print(tampilan2)
		input("press [enter] to return")

	elif pilihan == "b":
		tampilan3 = """
		SEKOLAH HARAPAN BANGSA
		----------------------------------------------------
		Periode Th. 1989 s.d 1998:  Ny. O. Radinal Mochtar
		Periode Th. 1998 s.d 2004:  Bp. Sunaryo Sumaji
		Periode Th 2004 s.d Sekarang:  Bp. Ir. Moh. Soeyuthi
		----------------------------------------------------
		"""
		print(tampilan3)
		input("press [enter] to return")

	elif pilihan == "c":
		tampilan4 = """
		SEKOLAH HARAPAN BANGSA
	  	---------------------------------------------------------
	  	Ketua                  :   Ny. Hj. Sri Kanti M. Joesoef
		Wakil Ketua            :   Ny. Hj. Komariyah B Suyono
		Sekretaris             :   Ny. Hj. Sri Sukarni E. Paminto
		Bendahara              :   Ny. Hj. Sri Retno L Hernowo
		------------
		Bidang Tugas
		------------
		Ketenagakerjaan/Kelembagaan:   Ny. Hj. Sri Sukarni E. P
		Kurikulum/ Ekstrakurikuler:   Ny. Hj. Wardhani Bambang W.
		Sarana dan  Prasarana  :   Ny. Hj. S. Munawaroh R.
		---------------------------------------------------------
		"""
		print(tampilan4)
		input("press [enter] to return")

	elif pilihan == "d":
		tampilan5 = """
		SEKOLAH HARAPAN BANGSA
		-----------------------------------------------------------
		Periode tahun 1989 s.d. 2004  :   Drs. H. Imam Sofan MM
	  	Periode tahun 2004 s.d. 2010  :   Arum Hidayat, S.Pd.
	  	Periode tahun 2010 s.d. 2015  :   Kholik Sadirin, S. Pd.
	  	Periode tahun 2015 s.d. 2017  :   Yunaidah, S. Pd.
	  	Periode tahun 2017 s.d. sekarang:   Dicky Kurniawan, S. Pd.
	  	-----------------------------------------------------------
	  	"""
		print(tampilan5)
		input("press [enter] to return")

	elif pilihan == "e":
		tampilan6 = """
		SEKOLAH HARAPAN BANGSA
	  	-------------------------------------------------------------------
	  	Kualifikasi A (Amat Baik)
	  	Nilai 95
	   	Ditetapkan di Sumatera Selatan,
	   	oleh: Badan Akreditasi Nasional Sekolah/ Propinsi Sumatera Selatan
	   	Tanggal 22 Oktober 2012, dengan nomor SK 163/BAP-S/M/DKI/2012
	   	Berlaku sampai 22 Oktober 2017
	   	-------------------------------------------------------------------
	   	Status Bangunan
	   	----------------------------------
	   	Hak Milik
	  	Nomor IMB: 9373/IMB/1993
	  	Tanggal 27 Agustus 1993
	  	Nomor Bangunan: 1170/PIMB-PB/I/93
	  	Tanggal 03 April 1989
	  	----------------------------------
	  	"""
		print(tampilan6)
		input("press [enter] to return")

	elif pilihan == "f":
		print("silahkan kunjungi website sekolah kami --> https://www.sekolah-harapan-bangsa.sch.id/")
		print("XOXO :)")
		input("press [enter] to return")

	elif pilihan == "g":
		tampilan7 = """
		Jika ada kendala dengan pendaftaran murid silahkan hubungi no. berikut
		0823100010567 : Handani --> Admin sekolah harapan bangsa
		0890011334689 : Bp. Ir. Moh. Soeyuthi --> Ketua yayasan harapan bangsa
		"""
		print(tampilan7) 
		input("press [enter] to return")