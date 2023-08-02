from function import *
from constants import *

if __name__ == "__main__":
	while True:
		print(hello)
		start = input('Введите команду... ')
		if start in 'proverka':
			print(comand5)
			parametr = input('... ')
			if proverca1(parametr):
				table5(parametr.upper())
				table6(parametr.upper())
				print(comand6)
				break
			else:
				print(bad2)

		elif start in 'start':
			print(comand1)
			tabl1 = input(yes_no)
			if tabl1 in 'yes':
				print(comand2)
				tabl2 = input(yes_no)
				if tabl2 in 'yes':
					pass

				elif tabl2 in 'no':
					print(comand4)
					create_table_time = input('... ')
					if create_table_time in 'go':
						try:
							table2()
							table4()
							print(create_table_complite)
						except Exception:
							print(error2)
							break
				else:
					print(bad)

			elif tabl1 in 'no':
				print(comand3)
				create_table_time = input('... ')
				if create_table_time in 'go':
					try:
						table1()
						table3()
						print(create_table_complite)
					except Exception:
						print(error1)
						break

			else:
				print(bad)
		else:
			print(bad)
