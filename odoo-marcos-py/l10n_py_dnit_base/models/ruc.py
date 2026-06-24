    
"""Dígito verificador del RUC paraguayo (módulo 11, base 11).

Algoritmo oficial de la DNIT: se recorre el número de derecha a izquierda
multiplicando cada dígito por un factor creciente (2, 3, ... 11) que vuelve a
2 al superar la base. El verificador sale del resto de dividir la suma por 11.

Verificado contra constancias reales: 80009735-1, 1946520-3.
"""
"""
import re

BASE = 11


def check_digit(number):
"""
"""
Devuelve el dígito verificador (0-9) de un RUC sin guion.
"""
"""
    total = 0
    factor = 2
    for digit in reversed(str(number)):
        total += int(digit) * factor
        factor = factor + 1 if factor < BASE else 2
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder


def split(ruc):
"""
"""Separa un RUC 'NNNNNNN-D' en (número, dígito). El guion es opcional;
    sin él, el último dígito se toma como verificador.
"""
"""
    clean = re.sub(r"[^0-9]", "", ruc or "")
    if "-" in (ruc or ""):
        number, _, dv = ruc.partition("-")
        return re.sub(r"[^0-9]", "", number), re.sub(r"[^0-9]", "", dv)
    if len(clean) < 2:
        return clean, ""
    return clean[:-1], clean[-1]


def is_valid(ruc):
"""
"""True si el RUC trae un dígito verificador correcto.
"""
"""
    number, dv = split(ruc)
    if not number or not dv.isdigit():
        return False
    return check_digit(number) == int(dv)

"""
#Correccion total, segun logica descargable de la DNIT para el DV#
"""Dígito verificador del RUC paraguayo (módulo 11, base 11).

Algoritmo oficial de la DNIT adaptado para Odoo 19: Traducido directamente de la
función oficial PL/SQL de la DNIT, dando soporte a caracteres alfanuméricos (ASCII)
y limpiando de forma segura las máscaras de la interfaz web de Odoo.
"""
import re

BASE = 11

def check_digit(number):
    """Devuelve el dígito verificador (0-9) oficial de la DNIT."""
    if not number:
        return 0
        
    # Convertimos a string y pasamos a mayúsculas
    p_numero = str(number).upper().strip()
    
    # Si Odoo 19 envía el RUC con un guion previo de la vista, nos quedamos solo con la base
    if "-" in p_numero:
        p_numero = p_numero.split("-")[0]

    v_numero_al = ""
    
    # Reemplazo de caracteres alfanuméricos por su código ASCII (Regla oficial DNIT)
    for caracter in p_numero:
        codigo_ascii = ord(caracter)
        if not (48 <= codigo_ascii <= 57):  # Si NO es un número entre 0 y 9
            v_numero_al += str(codigo_ascii)
        else:
            v_numero_al += caracter

    # Bucle en reversa aplicando el multiplicador creciente del Módulo 11
    k = 2
    v_total = 0
    
    for v_caracter_aux in reversed(v_numero_al):
        if k > BASE:
            k = 2
        
        v_numero_aux = int(v_caracter_aux)
        v_total += v_numero_aux * k
        k += 1

    # Cálculo del residuo y asignación del DV oficial
    v_resto = v_total % 11
    if v_resto > 1:
        return 11 - v_resto
    else:
        return 0


def split(ruc):
    """Separa un RUC 'NNNNNNN-D' en (número, dígito) adaptado para Odoo 19."""
    if not ruc:
        return "", ""
    
    ruc_str = str(ruc).strip()
    
    # Si viene con formato de Odoo 19 (ej: 5411453-9), lo dividimos limpiamente
    if "-" in ruc_str:
        number, _, dv = ruc_str.partition("-")
        return number.strip(), dv.strip()
        
    clean = re.sub(r"[^0-9A-Z]", "", ruc_str.upper())
    if len(clean) < 2:
        return clean, ""
    return clean[:-1], clean[-1]


def is_valid(ruc):
    """True si el RUC trae un dígito verificador correcto bajo las reglas DNIT."""
    number, dv = split(ruc)
    if not number or not dv:
        return False
    try:
        return check_digit(number) == int(dv)
    except ValueError:
        return False