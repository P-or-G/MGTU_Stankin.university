from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import unicodedata
import emoji

tips = ['критическое мышление', 'физическая подготовка', 'креативность', 'эмоциональная устойчивость', 'трудолюбие']

nokb = ReplyKeyboardRemove()

menu_btn = InlineKeyboardButton('Вернуться к выбору специальности', callback_data='menu')

btn1 = InlineKeyboardButton('Архитектура и строительство 🏛', callback_data='arch')
btn2 = InlineKeyboardButton('Военное дело, безопасность, охрана ⚔️', callback_data='mil')
btn3 = InlineKeyboardButton('Дипломатия 🕊', callback_data='dip')
btn4 = InlineKeyboardButton('Лингвистика 🈳', callback_data='ling')
btn5 = InlineKeyboardButton('IT ‍💻', callback_data='it')
btn6 = InlineKeyboardButton('Искусство 🎨', callback_data='pnt')
btn7 = InlineKeyboardButton('Спорт 🏈', callback_data='pe')
btn8 = InlineKeyboardButton('Медицина 💊', callback_data='med')
btn9 = InlineKeyboardButton('Физико-математические науки ♾️', callback_data='eng')
btn10 = InlineKeyboardButton('Химико-биологические науки ⚗️', callback_data='chem')
st_but = InlineKeyboardMarkup(row_width=3)
st_but.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)


VUZ2 = ['МАСИ', 'arch', ['Золотой значок ГТО', 5, [3, 7, 1, 5, 7]], ['Волонтерская (добровольческая) деятельность', 10, [5, 3, 4, 7, 8]],['Золотая медаль', 10, [8, 1, 9, 10, 10]]]
VUZ3 = ['МАРХИ', 'arch', ['Золотой значок ГТО', 2, [3, 7, 1, 5, 7]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Золотая медаль',10, [8, 1, 9, 10, 10]]]
VUZ4 = ['НИУ МГСУ', 'arch', ['Золотая медаль', 3, [8, 1, 9, 10, 10]], ['СПО с отличием', 3, [4, 6, 7, 9, 9]], ['Портфолио',5, [7, 1, 10, 7, 9]]]
arch_uni1 = InlineKeyboardButton('МАСИ', callback_data='V2')
arch_uni2 = InlineKeyboardButton('МАРХИ', callback_data='V3')
arch_uni3 = InlineKeyboardButton('НИУ МГСУ', callback_data='V4')
arch_but = InlineKeyboardMarkup(row_width=2)
arch_but.add(arch_uni1, arch_uni2, arch_uni3, menu_btn)

VUZ5 = ['РАНХиГС', 'mil', ['Золотой значок ГТО', 3, [3, 7, 1, 5, 7]], ['СПО с отличием', 5, [4, 6, 7, 9, 9]], ['Золотая медаль',5, [8, 1, 9, 10, 10]]]
mil_uni1 = InlineKeyboardButton('РАНХиГС', callback_data='V5')
mil_but = InlineKeyboardMarkup(row_width=2)
mil_but.add(mil_uni1, menu_btn)

VUZ6 = ['РГУНиГ', 'dip', ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио',10, [7, 1, 10, 7, 9]]]
VUZ7 = ['МГЛУ', 'dip', ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио',2, [7, 1, 10, 7, 9]]]
VUZ8 = ['ВАВТ', 'dip', ['Золотой значок ГТО', 2, [3, 7, 1, 5, 7]], ['СПО с отличием', 5, [4, 6, 7, 9, 9]], ['Золотая медаль',5, [8, 1, 9, 10, 10]]]
dip_uni1 = InlineKeyboardButton('РГУНиГ', callback_data='V6')
dip_uni2 = InlineKeyboardButton('МГЛУ', callback_data='V7')
dip_uni3 = InlineKeyboardButton('ВАВТ', callback_data='V8')
dip_but = InlineKeyboardMarkup(row_width=2)
dip_but.add(dip_uni1, dip_uni2, dip_uni3, menu_btn)

VUZ9 = ['РГСУ', 'ling', ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио',5, [7, 1, 10, 7, 9]]]
VUZ10 = ['МГИМО', 'ling', ['Золотая медаль',4, [8, 1, 9, 10, 10]], ['СПО с отличием', 4, [4, 6, 7, 9, 9]], ['Портфолио',3, [7, 1, 10, 7, 9]]]
VUZ11 = ['РГГУ', 'ling', ['Золотая медаль',4, [8, 1, 9, 10, 10]], ['СПО с отличием', 4, [4, 6, 7, 9, 9]], ['Портфолио',3, [7, 1, 10, 7, 9]]]
ling_uni1 = InlineKeyboardButton('РГСУ', callback_data='V9')
ling_uni2 = InlineKeyboardButton('МГИМО', callback_data='V10')
ling_uni3 = InlineKeyboardButton('РГГУ', callback_data='V11')
ling_but = InlineKeyboardMarkup(row_width=2)
ling_but.add(ling_uni1, ling_uni2, ling_uni3, menu_btn)

VUZ12 = ['МТУСИ', 'it', ['Золотой значок ГТО', 2, [3, 7, 1, 5, 7]], ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио',10, [7, 1, 10, 7, 9]]]
VUZ13 = ['МИСИС', 'it', ['Золотой значок ГТО', 2, [3, 7, 1, 5, 7]], ['Золотая медаль',5, [8, 1, 9, 10, 10]], ['СПО с отличием', 5, [4, 6, 7, 9, 9]], ['Портфолио',5, [7, 1, 10, 7, 9]]]
VUZ14 = ['МГТУ "СТАНКИН"', 'it', ['Золотой значок ГТО', 6, [3, 7, 1, 5, 7]], ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио', 10, [7, 1, 10, 7, 9]]]
it_uni1 = InlineKeyboardButton('МТУСИ', callback_data='V12')
it_uni2 = InlineKeyboardButton('МИСИС', callback_data='V13')
it_uni3 = InlineKeyboardButton('МГТУ', callback_data='V14')
it_but = InlineKeyboardMarkup(row_width=2)
it_but.add(it_uni1, it_uni2, it_uni3, menu_btn)

VUZ15 = ['МГОУ', 'pnt', ['Золотой значок ГТО', 2, [3, 7, 1, 5, 7]], ['Золотая медаль',3, [8, 1, 9, 10, 10]], ['СПО с отличием', 3, [4, 6, 7, 9, 9]], ['Портфолио',8, [7, 1, 10, 7, 9]]]
VUZ16 = ['ММУ', 'pnt', ['Золотой значок ГТО', 4, [3, 7, 1, 5, 7]], ['Золотая медаль',5, [8, 1, 9, 10, 10]], ['СПО с отличием', 5, [4, 6, 7, 9, 9]], ['Портфолио',4, [7, 1, 10, 7, 9]]]
VUZ17 = ['МГАХИ', 'pnt', ['Золотой значок ГТО', 2, [3, 7, 1, 5, 7]], ['Золотая медаль',3, [8, 1, 9, 10, 10]], ['СПО с отличием', 4, [4, 6, 7, 9, 9]], ['Портфолио',1, [7, 1, 10, 7, 9]]]
pnt_uni1 = InlineKeyboardButton('МГОУ', callback_data='V15')
pnt_uni2 = InlineKeyboardButton('ММУ', callback_data='V16')
pnt_uni3 = InlineKeyboardButton('МГАХИ', callback_data='V17')
pnt_but =InlineKeyboardMarkup(row_width=2)
pnt_but.add(pnt_uni1, pnt_uni2, pnt_uni3, menu_btn)

VUZ1 = ['РГУФКСМиТ', 'pe', ['Золотой значок ГТО', 5, [3, 7, 1, 5, 7]], ['Золотая медаль',5, [8, 1, 9, 10, 10]], ['СПО с отличием', 1, [4, 6, 7, 9, 9]], ['Волонтерская (добровольческая) деятельность', 1, [5, 3, 4, 7, 8]]]
VUZ19 = ['МГУСиТ', 'pe', ['Золотой значок ГТО', 5, [3, 7, 1, 5, 7]], ['Золотая медаль',5, [8, 1, 9, 10, 10]], ['СПО с отличием', 5, [4, 6, 7, 9, 9]], ['Волонтерская (добровольческая) деятельность',2, [5, 3, 4, 7, 8]]]
VUZ20 = ['МГАФК', 'pe', ['Золотой значок ГТО', 4, [3, 7, 1, 5, 7]], ['Золотая медаль',5, [8, 1, 9, 10, 10]], ['СПО с отличием', 5, [4, 6, 7, 9, 9]], ['Волонтерская (добровольческая) деятельность',4, [5, 3, 4, 7, 8]]]
pe_uni1 = InlineKeyboardButton('РГУФКСМиТ', callback_data='V1')
pe_uni2 = InlineKeyboardButton('МГУСиТ', callback_data='V19')
pe_uni3 = InlineKeyboardButton('МГАФК', callback_data='V20')
pe_but = InlineKeyboardMarkup(row_width=2)
pe_but.add(pe_uni1, pe_uni2, pe_uni3, menu_btn)

VUZ21 = ['РНИМУ', 'med', ['Золотой значок ГТО', 3, [3, 7, 1, 5, 7]], ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио',10, [7, 1, 10, 7, 9]]]
VUZ22 = ['РХТУ', 'med',['Золотая медаль',5, [8, 1, 9, 10, 10]], ['Портфолио',10, [7, 1, 10, 7, 9]], ['СПО с отличием', 5, [4, 6, 7, 9, 9]], ['Волонтерская (добровольческая) деятельность',2, [5, 3, 4, 7, 8]]]
VUZ23 = ['РОСБИОТЕХ', 'med', ['Золотой значок ГТО', 3, [3, 7, 1, 5, 7]], ['Золотая медаль',5, [8, 1, 9, 10, 10]], ['СПО с отличием', 5, [4, 6, 7, 9, 9]], ['Портфолио',5, [7, 1, 10, 7, 9]]]
med_uni1 = InlineKeyboardButton('РНИМУ', callback_data='V21')
med_uni2 = InlineKeyboardButton('РХТУ', callback_data='V22')
med_uni3 = InlineKeyboardButton('РОСБИОТЕХ', callback_data='V23')
med_but = InlineKeyboardMarkup(row_width=2)
med_but.add(med_uni1, med_uni2, med_uni3, menu_btn)

VUZ27 = ['НИУ МГСУ', 'chem', ['Золотой значок ГТО', 3, [3, 7, 1, 5, 7]], ['СПО с отличием', 3, [4, 6, 7, 9, 9]], ['Портфолио',5, [7, 1, 10, 7, 9]]]
VUZ28 = ['МГУТУ', 'chem', ['Золотой значок ГТО', 5, [3, 7, 1, 5, 7]], ['Золотая медаль',7, [8, 1, 9, 10, 10]], ['СПО с отличием', 7, [4, 6, 7, 9, 9]], ['Портфолио',10, [7, 1, 10, 7, 9]]]
VUZ29 = ['РГАУ-МСХА', 'chem', ['Золотой значок ГТО', 2, [3, 7, 1, 5, 7]], ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио',5, [7, 1, 10, 7, 9]]]
chem_uni1 = InlineKeyboardButton('МГСУ', callback_data='V27')
chem_uni2 = InlineKeyboardButton('МГУТУ', callback_data='V28')
chem_uni3 = InlineKeyboardButton('РГАУ-МСХА', callback_data='V29')
chem_but = InlineKeyboardMarkup(row_width=2)
chem_but.add(chem_uni1, chem_uni2, chem_uni3, menu_btn)

VUZ24 = ['МГУ', 'eng', ['Золотой значок ГТО', 2, [3, 7, 1, 5, 7]], ['Золотая медаль',6, [8, 1, 9, 10, 10]], ['СПО с отличием', 6, [4, 6, 7, 9, 9]], ['Сочинение',2, [7, 1, 10, 7, 9]]]
VUZ25 = ['МГТУ', 'eng', ['Золотой значок ГТО', 5, [3, 7, 1, 5, 7]], ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио',10, [7, 1, 10, 7, 9]]]
VUZ26 = ['РУДН', 'eng', ['Золотой значок ГТО', 3, [3, 7, 1, 5, 7]], ['Золотая медаль',10, [8, 1, 9, 10, 10]], ['СПО с отличием', 10, [4, 6, 7, 9, 9]], ['Портфолио',5, [7, 1, 10, 7, 9]]]
eng_uni1 = InlineKeyboardButton('МГУ', callback_data='V24')
eng_uni2 = InlineKeyboardButton('МГТУ', callback_data='V25')
eng_uni3 = InlineKeyboardButton('РУДН', callback_data='V26')
eng_but = InlineKeyboardMarkup(row_width=2)
eng_but.add(eng_uni1, eng_uni2, eng_uni3, menu_btn)

