coef_1 = 1
coef_2 = 2
coef_3 = 3

windows_dev = float(input("Note devoir windows: "))
windows_exam = float(input("Note exam windows: "))

algo_dev = float(input("Note algo devoir: "))
algo_exam = float(input("Note algo exam: "))

math_dev = float(input("Note maths devoir: "))
math_exam = float(input("Note maths exam: "))

uml_dev = float(input("Note UML devoir: "))
uml_exam = float(input("Note UML exam: "))

ccna_dev = float(input("Note cisco devoir: "))
ccna_exam = float(input("Note cisco exam: "))

bus_engl_dev = float(input("Note anglais devoir: "))
bus_engl_exam = float(input("Note anglais exam: "))

elc_digit_dev = float(input("Note devoir Electrronique digitale: "))
elc_digit_exam = float(input("Note exam Electrronique digitale: "))

byb_dev = float(input("Note BYB devoir: "))
byb_exam = float(input("Note BYB exam: "))

langage_C_dev = float(input("Note devoir Langage C: "))
langage_C_exam = float(input("Note examen Langage C: "))

python_dev = float(input("Note python devoir: "))
python_exam = float(input("Note python exam: "))

php_dev = float(input("Note php devoir: "))
php_exam = float(input("Note php exam: "))

sgbd_dev = float(input("Note sgbd devoir: "))
sgbd_exam = float(input("Note sgbd exam: "))


windows = (windows_dev * 0.4 + windows_exam * 0.6) * coef_1
algo = (algo_dev * 0.4 + algo_exam * 0.6) * coef_2
maths = (math_dev * 0.4 + math_exam * 0.6) * coef_2
uml = (uml_dev * 0.4 + algo_dev * 0.6) * coef_2
cisco = (ccna_dev * 0.4 + ccna_exam * 0.6) * coef_2
anglais = (bus_engl_dev * 0.4 + bus_engl_exam * 0.6) * coef_2
elec_dig = (elc_digit_dev* 0.4 + elc_digit_exam * 0.6) * coef_1
byb = (byb_dev* 0.4 + byb_exam * 0.6) * coef_2
L_c = (langage_C_dev * 0.4 + langage_C_exam * 0.6) * coef_2
python = (python_dev * 0.4 + python_exam * 0.6) * coef_2
php = (php_dev * 0.4 + php_exam * 0.6) * coef_1
sgbd = (sgbd_dev * 0.4 + sgbd_exam * 0.6) * coef_2


moyenne = windows + algo + maths + uml + cisco + anglais + elec_dig + byb + L_c + python + php + sgbd   

print("Resultat: \n ") 
print(f"moyenne: {moyenne}; {moyenne / 21}")
