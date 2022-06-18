coef_1 = 1
coef_2 = 2
algo_dev = float(input("Note algo devoir: "))
algo_exam = float(input("Note algo exam: "))
eng_dev = float(input("Note anglais devoir: "))
eng_exam = float(input("Note anglais exam: "))
cms_dev = float(input("Note wordpress devoir: "))
cms_exam = float(input("Note wordpress exam: "))
cg_dev = float(input("Note conception graphique devoir: "))
cg_exam = float(input("Note conception graphique  exam: "))
eco_dev = float(input("Note economie d'entreprise devoir: "))
eco_exam = float(input("Note economie d'entreprise exam: "))
elec_exam = float(input("Note electricite exam: "))
math_exam = float(input("Note maths exam: "))
python_dev = float(input("Note python devoir: "))
python_exam = float(input("Note python exam: "))
ccna_exam = float(input("Note ccna exam: "))
html_dev = float(input("Note html devoir: "))
html_exam = float(input("Note html exam: "))
english = (eng_dev * 0.4 + eng_exam * 0.6) * coef_1
algo = (algo_dev * 0.4 + algo_exam * 0.6) * coef_2
cms = (cms_dev * 0.4 + cms_exam * 0.6) * coef_2
cg = (cms_dev * 0.4 + cms_exam * 0.6) * coef_1
eco = (eco_dev * 0.4 + eco_exam * 0.6) * coef_2
electricite = (elec_exam * 0.6) * coef_2
maths = (math_exam * 0.6) * coef_2
python = (python_dev * 0.4 + python_exam * 0.6) * coef_2
ccna = (ccna_exam * 0.6) * coef_2
html= (html_dev * 0.4 + html_exam * 0.6) * coef_2
moyenne = algo + english + cms + cg + eco + electricite + maths + python + ccna + html 
while algo_dev < 0 or algo_dev > 20 and algo_exam < 0 or algo_exam > 20:
    while eng_dev < 0 or eng_dev > 20 and eng_exam < 0 or eng_exam > 20:
        while cms_dev < 0 or cms_dev > 20 and cms_exam < 0 or cms_exam > 20:
            while cg_dev < 0 or cg_dev > 20 and cg_exam < 0 or cg_exam > 20:
                while eco_dev < 0 or eco_dev > 20 and eco_exam < 0 or eco_exam > 20:
                    while elec_exam < 0 or elec_exam > 20:
                        while math_exam < 0 or math_exam > 20:
                            while python_dev < 0 or python_dev > 20 and python_exam < 0 or python_exam > 20:
                                while ccna_exam < 0 or ccna_exam > 20:
                                    while html_dev < 0 or html_dev > 20 and html_exam < 0 or html_exam > 20:
                                        print("erreur de saisi de note")
                                        break 
if moyenne / 18 > 180:
    print(f"moyenne: {moyenne}; {moyenne / 18}")
else:
    print(f"moyenne: {moyenne}; {moyenne / 18}")
