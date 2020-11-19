from os import system 

from json import load, dump

def pendaftaran_sekolah():
	print("sebelumnya bacalah kententuan berikut dulu untuk pendaftaran murid baru")
	print("""
	Syarat Masuk SD HARAPAN BANGSA 2020:
	-->Usia paling rendah 6 tahun pada 1 Juli tahun berjalan
	-->Berusia 7 tahun sampai dengan 12 tahun
	-->Sekolah wajib menerima calon siswa mulai dari usia 7 tahun hingga 12 tahun
	-->Calon siswa baru yang memiliki kecerdasan atau bakat istimewa dan siap secara psikis diberi pengecualian dengan syarat usia minimal 5 tahun 6 bulan pada 1 Juli tahun berjalan
	-->Bukti potensi kecerdasan atau memiliki bakat istimewa dari calon siswa harus disertakan bersama rekomendasi tertulis dari psikolog profesional ataupun dewan guru sekolah 
	Syarat Masuk SMP HARAPAN BANGSA 2020:
	-->Usia maksimal 15 tahun pada 1 Juli tahun berjalan dengan dibuktikan akta kelahiran yang dikeluarkan pihak berwenang dan dilegalisir oleh lurah atau kepala desa setempat seusai domisili calon siswa
	-->Memiliki ijazah SD atau dokumen lain yang menjelaskan telah menyelesaikan kelas 6 SD
	-->Bagi WNI yang ingin mendaftar PPDB khusus kelas 7 dan berasal dari sekolah di luar negeri, wajib menyertakan surat keterangan dari direktur jenderal bidang pendidikan dasar dan menengah selain 
	   memenuhi syarat yang dimaksudkan
	-->Peserta didik WNA wajib ikut matrikulasi pendidikan Bahasa Indonesia minimal 6 bulan dari sekolah yang bersangkutan
	-->Khusus calon siswa penyandang disabilitas di sekolah mendapat pengecualian dari syarat usia maupun ijazah sesuai dengan Pasal 10 Permendikbud Nomor 44 Tahun 2019)
	Syarat Masuk SMA HARAPAN BANGSA 2020:
	-->Usia maksimal 21 tahun pada 1 Juli tahun berjalan dan memiliki ijazah SMP/sederajat yang menjelaskan telah lulus dari kelas 9 SMP
	-->Syarat usia dibuktikan dengan akta kelahiran yang dikeluarkan pihak berwenang dan dilegalisir oleh lurah atau kepala desa setempat sesuai domisili calon siswa
	-->Khusus persyaratan calon peserta didik SMK dengan bidang keahlian, program keahlian, ataupun kompetensi keahlian tertentu dapat menetapkan tambahan syarat dalam penerimaan peserta didik baru kelas 10
	-->Bagi WNI yang ingin mendaftar PPDB khusus kelas 10 dan berasal dari sekolah di luar negeri, wajib menyertakan surat keterangan dari direktur jenderal bidang pendidikan dasar dan menengah selain
	   memenuhi syarat yang dimaksudkan
	-->Peserta didik WNA wajib ikut matrikulasi pendidikan Bahasa Indonesia minimal 6 bulan dari sekolah yang bersangkutan
	-->Khusus calon siswa penyandang disabilitas di sekolah mendapat pengecualian dari syarat usia maupun ijazah sesuai dengan Pasal 10 Permendikbud Nomor 44 Tahun 2019)"""
	)
	jawaban = input("Jika sudah baca tekan enter untuk lanjut atau ketik n untuk kembali: ")
	if jawaban == "":
		print("Pendaftaran murid baru")
		nama = input("Nama murid: ")
		lahir = input("tanggal lahir: ")
		agama = input("agama: ")
		anak_ke = input("anak ke: ")
		alamat = input("alamat rumah: ")
		asal_sekolah = input("asal sekolah (nama sekolah/tidak ada): ")
		nama_ayah = input("Nama ayah murid: ")
		nama_ibu = input("Nama ibu murid: ")
		pekerjaan_ayah = input("Pekerjaan ayah: ")
		pekerjaan_ibu = input("Pekerjaan ibu: ")
		no_telp_org_tua = input("nomor telpon orang tua(ayah/ibu): ")
		ingin_daftar_ke = input("Ingin daftar ke jenjang: ").upper()
		respon = input("Apakah data sudah benar(Y/N): ").upper()
		if respon == "Y":
			daftar[nama] = {

			"lahir" : lahir,
			"agama" : agama,
			"anak_ke" : anak_ke,
			"alamat" : alamat,
			"asal_sekolah" : asal_sekolah,
			"nama_ayah" : nama_ayah,
			"nama_ibu" : nama_ibu,
			"pekerjaan_ayah" : pekerjaan_ayah,
			"pekerjaan_ibu" : pekerjaan_ibu,
			"no_telp_org_tua" : no_telp_org_tua,
			"ingin_daftar_ke" : ingin_daftar_ke

			}
			save_daftar()
			print("data tersimpan")
			input("tekan [enter] to return")
		else:
			print("pendaftaran batal")
			input("press [enter] to return")
	elif jawaban.lower() == "n":
		print("")

def tampilan_nama_murid():
	system("cls")
	print("daftar murid")
	if len(daftar) == 0:
		print("belum ada data yg disimpan saat ini")
	else:
		print("-nama-\t\t\t   -asal sekolah-\t\t-ingin daftar ke-")
		for data in daftar:
			print(data, "\t\t", daftar[data]["asal_sekolah"], "\t\t", daftar[data]["ingin_daftar_ke"])
	input("press [enter] to return")

def cari_murid(data):
	if data in daftar:
		print("---HASIL PENCARIAN---")
		print("nama: ",data)
		print("asal sekolah: ",daftar[data]["asal_sekolah"])
		print("ingin daftar ke jenjang: ", daftar[data]["ingin_daftar_ke"])
		return True
	else:
		print("data tidak ditemukan")
		return False


def tampilan_cari_murid():
	system("cls")
	print("Pencarian murid")
	nama = input("Nama murid yg dicari: ")
	cari_murid(nama)
	input("press [enter] to return")

def private(data):
	if data in daftar:
		print("---RESULT---")
		print("nama: ", data)
		print("lahir: ", daftar[data]["lahir"])
		print("agama: ", daftar[data]["agama"])
		print("anak ke: ", daftar[data]["anak_ke"])
		print("alamat: ",daftar[data]["alamat"])
		print("asal sekolah: ",daftar[data]["asal_sekolah"])
		print("nama ayah: ",daftar[data]["nama_ayah"])
		print("nama ibu: ", daftar[data]["nama_ibu"])
		print("pekerjaan ayah: ",daftar[data]["pekerjaan_ayah"])
		print("pekerjaan ibu: ",daftar[data]["pekerjaan_ibu"])
		print("nomor telfon orang tua: ", daftar[data]["no_telp_org_tua"])
		print("ingin daftar ke jenjang: ", daftar[data]["ingin_daftar_ke"])

	else:
		print("data tidak ditemukan")


def edit_lahir(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['lahir']}")
	new_lahir = input("tanggal lahir: ")
	daftar[name]['lahir'] = new_lahir
	save_daftar()
	print("\n**Data berhasil diperbarui**")



def edit_agama(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['agama']}")
	new_agama = input("agama: ")
	daftar[name]['agama'] = new_agama
	save_daftar()
	print("\n**Data berhasil diperbarui**")



def edit_anak(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['anak_ke']}")
	new_anak = input("anak ke : ")
	daftar[name]['anak_ke'] = new_anak
	save_daftar()
	print("\n**Data berhasil diperbarui**")



def edit_alamat(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['alamat']}")
	new_alamat = input("alamat: ")
	daftar[name]['alamat'] = new_alamat
	save_daftar()
	print("\n**Data berhasil diperbarui**")


def edit_sekolah(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['asal_sekolah']}")
	new_sekolah = input("asal sekolah: ")
	daftar[name]['asal_sekolah'] = new_sekolah
	save_daftar()
	print("\n**Data berhasil diperbarui**")



def edit_ayah(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['ayah']}")
	new_ayah = input("nama ayah: ")
	daftar[name]['nama_ayah'] = new_ayah
	save_daftar()
	print("\n**Data berhasil diperbarui**")



def edit_ibu(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['nama_ibu']}")
	new_ibu = input("nama ibu: ")
	daftar[name]['nama_ibu'] = new_ibu
	save_daftar()
	print("\n**Data berhasil diperbarui**")



def edit_kerja1(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['pekerjaan_ayah']}")
	new_kerja1 = input("pekerjaan ayah: ")
	daftar[name]['pekerjaan_ayah'] = new_kerja1
	save_daftar()
	print("\n**Data berhasil diperbarui**")




def edit_kerja2(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['pekerjaan_ibu']}")
	new_kerja2 = input("pekerjaan ibu: ")
	daftar[name]['pekerjaan_ibu'] = new_kerja2
	save_daftar()
	print("\n**Data berhasil diperbarui**")


def edit_notelp(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['no_telp_org_tua']}")
	new_telp = input("nomor telpon orang tua: ")
	daftar[name]['no_telp_org_tua'] = new_telp
	save_daftar()
	prnt("\n**Data berhasil diperbarui**")


def edit_jenjang(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"{daftar[name]['ingin_daftar_ke']}")
	new_jenjang = input("ingin daftar ke jenjang: ").upper()
	daftar[name]['ingin_daftar_ke'] = new_jenjang
	save_daftar()
	print("\n**Data berhasil diperbarui**")


def edit_nama(name):
	print("**Data yang akan diperbarui**\n")
	print("data lama")
	print(f"nama: {name}")
	new_name = input("masukkan nama: ")
	daftar[new_name] =  daftar[name]
	del daftar[name]
	save_daftar()
	print("\n**Data berhasil diperbarui**")
	cari_murid(new_name)


def edit_info():
	system("cls")
	print("edit info murid")
	for data in daftar:
		print(data)
	nama = input("murid yang ingin diedit datanya: ")
	result = cari_murid(nama)
	if result:
		print("""        [1]edit nama              [2]edit tanggal lahir           [3]edit agama 
	[4]edit alamat            [5]edit alamat                  [6]edit anak ke          
	[7]edit nama ayah         [8]edit nama ibu                [9]edit pekerjaan ayah          
	[10]edit pekerjaan ibu    [11]edit no telp orang tua      [12]edit ingin daftar ke jenjang""")
		respon = input("pilih[1/2/3/4/5/6/7/8/9/10/11/12]:  ")
		if respon == "1":
			edit_nama(nama)
		elif respon == "2":
			edit_lahir(nama)
		elif respon == "3":
			edit_agama(nama)
		elif respon == "4":
			edit_alamat(nama)
		elif respon == "5":
			edit_alamat(nama)
		elif respon == "6":
			edit_anak(nama)
		elif respon == "7":
			edit_ayah(nama)
		elif respon == "8":
			edit_ibu(nama)
		elif respon == "9":
			edit_kerja1(nama)
		elif respon == "10":
			edit_kerja2(nama)
		elif respon == "11":
			edit_notelp(nama)
		elif respon == "12":
			edit_jenjang(nama)


	else:
		print("data tidak ditemukan")


def data_pribadi():
	admin_key = "parahmen"
	guess = ""
	count_guess = 0
	guess_limit = 5
	out_of_guesses = False
	while guess != admin_key and not(out_of_guesses):
		if count_guess < guess_limit : 
			guess = input("masukkan key khusus untuk admin: ")
			count_guess += 1
		else:
			out_of_guesses = True

	if out_of_guesses :
		print("coba lagi dalam 5 menit")
		input("press [enter] to return")
	else:
		system("cls")
		halo = input("Edit atau Baca: (E/B)").upper()
		if halo == "E":
			edit_info()
			input("tekan [enter] untuk kembali")
			
		elif halo == "B":
			name = input("murid yang ingin dilihat datanya: ")
			private(name)
			input("tekan [enter] untuk kembali")

		else:
			print("ERORR")
			input("tekan [enter] untuk kembali")


def load_daftar():
	with open("data/data_table.json", "r") as file:
		daftar = load(file)
		return daftar

def save_daftar():
	with open("data/data_table.json", "w") as file:
		dump(daftar, file)

daftar = load_daftar()
