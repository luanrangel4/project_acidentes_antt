import pandas as pd
import re
import unidecode


def normalize_columns(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
        .str.replace(" ", "_")
    )
    return df


def limpar(txt):
    if not isinstance(txt, str):
        return ""
    txt = unidecode.unidecode(txt).lower().strip()
    txt = re.sub(r"\s+", " ", txt)
    return txt


def corrigir_residuos(t):
    t = t.lower()

   
    if "saï¿½da" in t or "saÃ¯Â¿Â½da" in t or "saã¯¿½da" in t:
        return "saida de pista"

    corrigir = {
        "sa da de pista": "saida de pista",
        "sa da de pist": "saida de pista",
        "sa da pista": "saida de pista",
        "sa da": "saida",
        "sa da de": "saida de",
        "sa da de p": "saida de pista",
        "saïda": "saida",
        "saïda de pista": "saida de pista",
        "saÃda": "saida",
        "saÃda de pista": "saida de pista",
        "elemento d": "elemento de drenagem",
        "elemento ": "elemento de drenagem",
        "veiculo pa": "veiculo parado",
        "veiculo par": "veiculo parado",
        "objeto so": "objeto sobre a pista",
        "objeto sob": "objeto sobre a pista",
        "submarino": "praca submarino",
        "cabine de pedagio": "praca cabine",
    }

    for k, v in corrigir.items():
        if k in t:
            return v

    return t

def classificar_choque(t):

    t = corrigir_residuos(t)

    if any(k in t for k in [
        "praca", "cancela", "cabine", "submarino", "pedagio",
        "sinaliza", "placa", "suporte", "painel", "call box",
        "elemento de drenagem", "drenag", "caixa de captacao",
    ]):
        return "Choque com Infraestrutura"

  
    if any(k in t for k in [
        "arvore", "poste", "pilar", "talude", "barranco",
        "meio fio", "new jersey", "defensa", "objeto fixo",
        "obstaculo fixo", "barreira"
    ]):
        return "Choque com Objeto Fixo"

   
    if any(k in t for k in [
        "objeto na pista", "objeto sobre", "obstaculo",
        "objeto nao identificado", "carga"
    ]):
        return "Choque com Objeto Móvel"

   
    if any(k in t for k in [
        "veiculo parado", "estacionado", "acostamento"
    ]):
        return "Choque com Veículo Parado"

    return "Choque – Não Classificado"

def normalizar_tipo_acidente(txt):
    t = limpar(txt)
    
    if "saida de pista" in t or "saidas de pista" in t:
        return "Saída de Pista"

    
    if t == "colisao" or t == "colisão":
        return "Colisão Não Especificada"
    

    if t in ["norte", "sul"]:
        return "Acidente Não Classificado"

   
    if t in ["outros", "outros(especificar)", "outros - sequências", "outros - seguencias"]:
        return "Acidente Não Classificado"

    
    if t == "" or t == "nan":
        return "Acidente Não Classificado"
    
    if t in ["outros", "outros(especificar)"]:
        return "Acidente Não Classificado"

    if "sequ" in t:
        return "Acidente Sequencial"

    if "objeto lan" in t:
        return "Colisão com Objeto Móvel"

    if "soterr" in t:
        return "Soterramento"

    if "atrolement" in t:
        return "Tombamento"

    if "explos" in t:
        return "Explosão"

    if "inc" in t and "nd" in t:
        return "Incêndio / Veículo em Chamas"

    if ("sentido" in t and "oposto" in t) or "sent.oposto" in t:
        return "Colisão Sentido Oposto"

    if "colisao com veiculo da concessionaria" in t:
        return "Colisão com Veículo da Concessionária"


    if "colisao com objeto movel na pista" in t:
        return "Colisão com Objeto Móvel na Pista"

    if t in ["norte", "sul"]:
        return "Acidente Não Classificado"

    if "teste" in t:
        return "Incidente Operacional"

    if "saida de pista" in t or "saída de pista" in t or "Saï¿½da de pista" in t or "saidas de pista" in t:
        return "Saída de Pista"

    
    if "engavet" in t:
        return "Engavetamento"


    if "outra natureza" in t or "outros tipos" in t:
        return "Acidente - Outra Natureza"

    if "sequ" in t:
        return "Acidente Sequencial"

 
    if any(k in t for k in ["objeto sobre", "objeto lanc", "obstaculo", "obstáculo", "pista "]):
        return "Colisão com Objeto Móvel"

   
    if "objeto fixo" in t or "ojeto fixo" in t or "fixo" in t:
        return "Colisão com Objeto Fixo"

    
    if "veiculo parado" in t or "estac" in t or "acostamento" in t:
        return "Colisão com Veículo Parado"

   
    if "derrap" in t or "carreta deu l" in t:
        return "Queda / Derrapagem"

   
    if "submers" in t:
        return "Submersão"


    if "danos eventuais" in t:
        return "Danos Eventuais"

  
    if "nao def" in t or "não def" in t or "evadiu" in t:
        return "Acidente Não Localizado"

  
    if "traves" in t or "canteiro central" in t or "transpos" in t:
        return "Transposição de Pista"

    if "incend" in t:
        return "Incêndio / Veículo em Chamas"

    if "incidente" in t:
        return "Incidente Operacional"

 
    if any(k in t for k in ["praca", "praça", "submarino", "cabine"]):
        return "Colisão em Infraestrutura Viária"

    if "sentido oposto" in t or "sent.oposto" in t:
        return "Colisão Sentido Oposto"

    if "mesmo sentido" in t or "mesmo.sentido" in t:
        return "Colisão Mesmo Sentido"

    if "longitudinal" in t:
        return "Colisão Longitudinal"

    if "transversal" in t or "trarnversal" in t or "traversasl" in t:
        return "Colisão Transversal"

    if "desatrel" in t:
        return "Desatrelamento"

    if "derrama" in t:
        return "Derramamento de Carga"


    if "choque" in t:
        return classificar_choque(t)

    if "traseir" in t:
        return "Colisão Traseira"
    if "frontal" in t:
        return "Colisão Frontal"
    if "lateral" in t and "mesmo sentido" not in t:
        return "Colisão Lateral"
    if "lateral" in t and "mesmo sentido" in t:
        return "Colisão Lateral - Mesmo Sentido"
    if "transversal" in t:
        return "Colisão Transversal"
    if "abalroamento long" in t:
        return "Colisão Longitudinal"
    if "mesmo sentido" in t:
        return "Colisão Mesmo Sentido"
    if "sentido oposto" in t:
        return "Colisão Sentido Oposto"
   
    if "animal" in t:
        return "Atropelamento - Animal"
    if "cicli" in t:
        return "Atropelamento - Ciclista"
    if "pedestr" in t:
        return "Atropelamento - Pedestre"
    if "usu" in t:
        return "Atropelamento - Usuário"
    if "trab" in t or "func" in t:
        return "Atropelamento - Trabalhador"
    if "esportista" in t or "romeiro" in t:
        return "Atropelamento - Esportista"
    if "ambulante" in t:
        return "Atropelamento - Ambulante"
    if "abrigo" in t:
        return "Atropelamento - Em Abrigo"
    if "atropel" in t:
        return "Atropelamento - Outros"

    
    if "queda de moto" in t:
        return "Queda - Moto"
    if "ribanceira" in t:
        return "Queda - Ribanceira"
    if "biciclet" in t:
        return "Queda - Bicicleta"
    if "queda" in t:
        return "Queda - Outros"

   
    if "tomb" in t:
        return "Tombamento"
    if "capot" in t:
        return "Capotamento"

    
    if "chama" in t or "incend" in t:
        return "Incêndio / Veículo em Chamas"
    if "mecanico" in t or "eletrico" in t:
        return "Falha Mecânica"
    if "viaduto" in t or "ponte" in t:
        return "Colisão em Infraestrutura Viária"
    if "sequenc" in t:
        return "Acidente Sequencial"
    if "traves" in t:
        return "Transposição de Pista"

    return "Acidente Não Classificado"
