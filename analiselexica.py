
import ply.lex as lex

states = (
    ('ptsearch','exclusive'),
)

# List of token names. 

tokens = (
    'initial_letter', #is when we have a letter wihch finishes with '\n', example: A
    'baseword', #is the +base word, always appears in the beggining of a new line followed by the character ':'
    'baseword_error', #example: worth
    'prefix_word', #is the type of the base word, always appears in a new line if the line contains the character '-' before the word
    'prefix_word_error', # -, insurance and freight
    'prefix_word_error_2', #  - volume ratio (P/V)\n
    'middle1_word', #is the type of the base word, always appears in a new line if the line contains the character '-' in the middle the word
    'middle1_word_error', #example:  sales -\n
    'middle1_word_error_2', #example: down.the -
    'middle2_word', #is the type of the base word, always appears in a new line if the line contains the character '-' in the middle the word
    'middle2_word_error', # example:  management information -\n
    'middle_word_5', # source and - of funds
    'suffix_word', #is the type of the base word, always appears in a new line if the line contains the character '-' after the word
    'suffix_error', #automatic data (ADP)-
    'double_word', #example: - base -
    'prefix_error_word', # example: -structuring
    'middle_error_word', #exameple: semi-costs
    'suffix_error_word', # example: shift-
    'abbreviation', #sigla ex: (PMTS)
    'no_hifen', #example: engineering
    'no_hifen_paragraph', # return on capital\n
    'normalword', # an english word to be translated (doesn't have a type)
    'a_parenteses', # CWM (clerical work
    'f_parenteses', # measurement)
    'portugueseTranslation', #the portuguese sentence appears after more than \t before the end of the current line  
    'portugueseTranslationError', # example: treinamento (mj dentro da indústria
    'paragraph',
)

def t_paragraph(t):
    r'\n'
    t.lexer.lineno += 1
    pass

def t_initial_letter(t): #example: A\n
    r'\w[ \r\t\f]*\n'
    t.lexer.lineno += 1
    t.value = t.value.strip()[0]
    return t

def t_normalword(t):#example: dole (do ot lex example)     OU    yearly report      OU     I.O.U. (I owe you)      OU    buyers's market    OU    cost-volume-analysis
    r'\(?\w[\w\'\-\.\']*([ \r\t\f]\w[\w\-]*)*([ \r\t\f]\([^\)]*\))?\)?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

def t_baseword(t): #example: automatic data: \n  OU  administration:         administração (f)
    r'[ \r\t\f]*\w[ \r\t\f\w\-]*:'
    t.lexer.push_state('ptsearch')
    return t

# Falta os : no final
def t_baseword_error(t): #example: worth\n   
    r'[ \r\t\f]*\w\w+\n'
    t.lexer.push_state('ptsearch')
    t.lexer.lineno += 1
    return t

# The third word is facultative!!!!!
# Pode incluir outros casos como:    to-rule   (to -)

def t_prefix_word(t): #example:   - of responsibilities (ROF)   OR   - of responsibilities rof (ROFR)
    r'[ \r\t\f]*-[ \r\t\f]+\w[\w\-\,]*([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

# ERRO de FORMATO
def t_prefix_word_error(t): # example: -, insurance and freight
    r'[ \r\t\f]*\-\,[ \r\t\f]\w[\w\-\,]*([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

def t_prefix_word_error_2(t): #  - volume ratio (P/V)\n
    r'[ \r\t\f]*-[ \r\t\f]\w[\w\,]*([ \r\t\f]\w[\w\-\,]*)*([ \r\t\f]\([^\)]*\))?\n'
    t.lexer.lineno += 1
    return t 

def t_middle1_word(t): #example:  value - tax (VAT)         OR        value - (VA)   OR    value - Tax tax (VATT)      OR       buyers'
    r'[ \r\t\f]*\w[\w\-\,\']*[ \r\t\f]-([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

def t_middle1_word_error(t): #example:  sales -\n
    r'[ \r\t\f]*\w[\w\-\,]*[ \r\t\f]-([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\([^\)]*\))?\n'
    t.lexer.lineno += 1
    return t

def t_middle1_word_error_2(t): # down.the -
    r'[ \r\t\f]*\w[\w\-\,\.]*[ \r\t\f]-([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

def t_middle2_word(t): #example:  value tax - (VAT)         OR    value Tax - tax (VTAT)    OU    quality (QC) -
    r'[ \r\t\f]*\w[\w\-\,]*[ \r\t\f][\w\(\)][\w\-\,\)]*[ \r\t\f]-([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t


''' middle2_word_error + abreviattion + translation   ----> VER NA ANALISE SINTÁTICA
 management information -
  (MIS)                       sistema (m) de dados para gestão

middle2_word_error + no_hifen + translation  

 return on -
   employed (ROCE)      rendimento (m) do capital investido
'''

def t_middle2_word_error(t): # example:  management information -\n    OU     #  return on -\n
    r'[ \r\t\f]*\w[\w\-\,]*[ \r\t\f]\w[\w\-\,]*[ \r\t\f]-([ \r\t\f]\w[\w\-\,]*)?([ \r\t\f]\([^\)]*\))?\n'
    t.lexer.lineno += 1
    return t

def t_middle_word_5(t): # source and - of funds
    r'[ \r\t\f]*\w[\w\-\,]*[ \r\t\f]\w[\w\-\,]*[ \r\t\f]-[ \r\t\f]\w[\w\-\,]*[ \r\t\f]\w[\w\-\,]*[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

def t_suffix_word(t): #example:  value tax final - (VTFA)
    r'[ \r\t\f]*\w[\w\-\,]*[ \r\t\f]\w[\w\-\,]*[ \r\t\f]\w[\w\-\,]*[ \r\t\f]-([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

# ERRO de FORMATO
def t_suffix_error(t): #automatic data (ADP)-
    r'[ \r\t\f]*\w[\w\-\,]*[ \r\t\f]\w[\w\-\,]*[ \r\t\f]\(\w[\w\-\,]*\)-([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

def t_double_word(t): #example: - base -     OU           price - earnings - (PIE)
    r'[ \r\t\f]*(\w[\w\-\,]*[ \r\t\f])?\-[ \r\t\f]\w[\w\-\,]*[ \r\t\f]\-([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

# ERRO DE FORMATO
def t_prefix_error_word(t) : # example: -structuring
    # r'[ \r\t\f]+-\w[\w-]*([ \r\t\f]\w[\w-]*)?([ \r\t\f]\([^\)]*\))?[ \r\t\f]{2}[ \r\t\f]*'
    r'[ \r\t\f]*\-\w[\w\,]*([ \r\t\f]\w[\w\-\,]*)*([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

# ERRO DE FORMATO
def t_middle_error_word(t): #exameple: semi-costs
    r'[ \r\t\f]*\w[\w\,]*\-\w[\w\,]*([ \r\t\f]\w[\w\-\,]*)*([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

# ERRO DE FORMATO
def t_suffix_error_word(t): #example:  shift-       OU     resale price-(RPM)
    r'[ \r\t\f]*(\w[\w\,]*[ \r\t\f])?\w[\w\,]*-([ \r\t\f]\w[\w\-,]*)*(\(\w*\))*([ \r\t\f]\([^\)]*\))?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

# Sigla - Acronim
def t_abbreviation(t): # (PMTS)
    r'[ \r\t\f]*\(\w[\w,]*\)[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return 


# abrir parenteses
def t_a_parenteses(t): # CWM (clerical work     OU     EEC (European Economic Com-            OU    R and D (research and
    r'[ \r\t\f]*(\w+[ \r\t\f])+\((\w[\w\,]*([ \r\t\f\-])?)+[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

# fechar parenteses
def t_f_parenteses(t): # measurement)
    r'[ \r\t\f]*\w+(([ \r\t\f]\w+)*)?\)[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

# às vezes pode n
def t_no_hifen(t): # diferença em relação ao normalword: contém espaço no início        OU     (O and M)
    r'[ \r\t\f]+\(?\w[\w\,\-]*([ \r\t\f]\w[\w\-\,]*)*([ \r\t\f]\([^\)]*\))?\)?[ \r\t\f]{3}[ \r\t\f]*'
    t.lexer.push_state('ptsearch')
    return t

def t_no_hifen_paragraph(t): # return on capital\n
    r'[ \r\t\f]*\w[\w\,]*([ \r\t\f]\w[\w\-\,]*)*([ \r\t\f]\([^\)]*\))?\n'
    t.lexer.lineno += 1
    return t

'''
 - measurement                medição (f) de trabalho
 clerical-measurement (CWM)   medição (f) de trabalho administrativo
'''
'''
def t_continue_word(t):
    r''
    t.lexer.push_state('ptsearch')
    return t
'''


def t_ptsearch_portugueseTranslation(t): # includes () í ,
    r'[^\n]*\n([ \r\t\f]{10}[^\n]*\n)*'
    t.lexer.pop_state()
    t.lexer.lineno += str(t.value).count('\n')
    return t

# ERRO DE FORMATO
def t_ptsearch_portugueseTranslationError(t): # example: treinamento (mj dentro da indústria
    r'[^\n]*\n([ \r\t\f]{10}[^\)\n]*\n)*'
    t.lexer.pop_state()
    t.lexer.lineno += str(t.value).count('\n')
    return t
    
t_ANY_ignore = ""

def t_ANY_error(t):
    print(f"Carácter ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

with open('dic-finance-en.pt.txt', 'r') as file:
    data = file.read()

text = '''A
ADP (automatic data processing)   processamento (m) automático de
                                   dados
absenteeism                       absenteísmo (m)
absorption costing                custeio (f) de absorção
abandonment:
 product -                        retirada (f) de um produto
above par                         com ágio; acima da paridade
acceleration clause               cláusula (f) de aceleração
acceptance:                       aceitação (f)
 brand -                          aceitação (f) de uma marca
 consumer -                       aceitação (f) por parte do consumidor
access:
 multi -                          acesso (m) múltiplo
 random -                         acesso (m) casual
account:
 bank -                           conta (f) bancária
 joint -                          conta (f) conjunta
accountability                    responsabilidade (f) sujeita a
                                   prestação de contas
accountant:

chief                             chefe (m) de contabilidade
'''



lexer.input(data)

print(lexer.token())



#'''
while tok := lexer.token():
    print(tok)
#'''

''' a_parenteses + ptsearch_portugueseTranslation + f_parenteses       ------>  Ver na análise sintática
CWM (clerical work              medição (f) de trabalho
                                   administrativo
measurement)


a_parenteses + ptsearch_portugueseTranslation + f_parenteses + ptsearch_portugueseTranslation

COINS (computerised information
 system)                        sistema (m) computadorizado de dados


'''



#  resale price-(RPM)