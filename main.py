from os import system

import views
from models import user, isi

isi.load_daftar()



user_respon = ""
while user_respon != "f":
	views.print_menu()
	user_respon = input("pilih [a/b/c/d/e]:")
	user.check_respon(user_respon)

else:
	system("cls")
	print("""goodbye and have a nice day!
		XOXO""")
