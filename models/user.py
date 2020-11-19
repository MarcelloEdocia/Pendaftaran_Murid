from . import isi
import views

def check_respon(char):
	if char == "a":
		isi.pendaftaran_sekolah()
	elif char == "b":
		isi.tampilan_nama_murid()
	elif char == "c":
		isi.tampilan_cari_murid()
	elif char == "d":
		views.informasi_sekolah()
	elif char == "e":
		isi.data_pribadi()