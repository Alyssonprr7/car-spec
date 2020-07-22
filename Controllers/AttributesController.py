portuguese_dictionary = {
    "name": "Nome",
    "brand": "Marca",
    "model": "Modelo",
    "year": "Ano",
    "price": "Preço",
    "fuel": "Combustível",
    "IPVA": "IPVA",
    "insurance": "Seguro",
    "checkUpPrice": "Revisões",
    "origin": "Procedência",
    "guarantee": "Garantia",
    "configuration": "Configuração",
    "bodySize": "Porte",
    "capacity": "Lugares",
    "doors": "Portas",
    "generation": "Geração",
    "platform": "Plataforma",
    "indexCNW": "Índice CNW",
    "rankingCNW": "Ranking CNW",

    "engine": {
        "installation": "Instalação",
        "aspiration": "Aspiração",
        "layout": "Disposição",
        "powerSupply": "Alimentação",
        "valves": {
            "control": "Comando de Válvulas",
            "perCylinder": "Válvulas por Cilindro"
        },
        "cylinders": {
            "compressionRatio": "Razão de Compressão",
            "pistonStroke": "Curso dos Pistões  ",
            "diameter": "Diâmetro do Cilindro",
            "capacity": "Cilindrada",
            "quantity": "Cilindros"
        },
        "power": {
            "max": "Potência Máxima",
            "specific": "Potência Específica",
            "weight": "Peso/Potência"
        },
        "torque": {
            "max": "Torque Máximo",
            "specific": "Torque Específico",
            "weight": "Peso/Torque",
        },
        "engineCode": "Código do Motor",
    },
    "transmission": {
        "traction": "Tração",
        "gear": "Câmbio",
        "gearCode": "Código de Câmbio",
        "coupling": "Acoplamento"
    },

    "suspension": {
        "front": "Suspensão dianteira",
        "frontElasticElement": "Elemento Elástico Dianteiro",
        "back": "Suspensão Traseira",
        "backElasticElement": "Elemento Elástico Traseiro"
    },

    "brakes": {
        "front": "Freios Dianteiros",
        "back": "Freios Traseiros"
    },

    "steering": {
        "assistance": "Assistência",
        "minRotateDiameter": "Diâmetro Mínimo de Giro"
    },

    "tires": {
        "front": "Pneus Dianteiros",
        "frontSidewallHeight": "Altura do flanco dianteiro",
        "back": "Pneus Traseiros",
        "backSidewallHeight": "Altura do flanco traseiro"
    },

    "dimensions": {
        "lenght": "Comprimento",
        "width": "Largura",
        "axesDistance": "Distância Entre os Eixos",
        "height": "Altura",
        "frontGauge": "Bitola Dianteira",
        "backGauge": "Bitola Traseira",
        "trunkVolume": "Porta-malas",
        "fuelTank": "Tanque de Combustível",
        "weight": "Peso",
        "payload": "Carga Útil",
        "freeSpanGround": "Vão Livre de Solo"
    },

    "aerodynamics": {
        "frontArea": "Área Frontal(A)",
        "dragCoefficient": "Coeficiente de Arrasto(cx)",
        "frontAreaCorrected": "Área Frontal Corrigida"
    },

    "performance": {
        "maxSpeed": "Velocidade Máxima",
        "acceleration-0-100-km/h": "Aceleração 0-100km/h"
    },

    "fuelUse": {
        "urban": "Consumo Urbano",
        "road": "Consumo Rodoviário"
    },

    "drivingRange": {
        "urban": "Autonomia Urbana",
        "road": "Autonomia Rodoviária"
    },

    "source": {
        "url": "url",
        "carId": "carId",
        "domain": "Domínio"
    }
}
data_test = {
    "capacity": {
        "value":"eqweqw",
        "unity": "dasdas"
    },
    "doors": "Portas",
    "generation": "Geração",
    "platform": "Plataforma",
    "indexCNW": "Índice CNW",
    "capacity": [
        "fala",
        "ae"
    ],
    "rankingCNW": "Ranking CNW",

    "engine": {
        "installation": "Instalação",
        "aspiration": "Aspiração",
        "layout": "Disposição",
        "powerSupply": "Alimentação",
        "cylinders": "Cilindros"
    }
}


def translate_to_portuguese(attributes):  # TODO Implementar exceções para quando não tiver no dicionário
    attributes_in_portuguese = []

    for attribute in attributes:
        if (isinstance(attributes[attribute], str) and attribute != "id") or (isinstance(attributes[attribute], list)):
            attributes_in_portuguese.append(portuguese_dictionary[attribute])
        elif isinstance(attributes[attribute], dict) and check_if_is_type_value_objetc(attributes[attribute]):
            for item in attributes[attribute]:
                attributes_in_portuguese.append(portuguese_dictionary[attribute][item])

    return attributes_in_portuguese


def get_values(attributes):
    values = []
    for attribute in attributes:
        if isinstance(attributes[attribute], str) and attribute != "id":
            values.append(attributes[attribute])
        elif isinstance(attributes[attribute], dict):
            for item in attributes[attribute]:
                values.append(attributes[attribute][item])
    return values

objeto={
    "ola": {
        "value": "DASDSD",
        "unit": "asdasdas"
    },
    "hi":{
        "unit": "dasdas",
        "value": "dadasdas"
    },
    "hallo": {
        "unit": "Dasdsad",
        "dasda": "Fajsndsad",
        "dsadas": "dasdas"
    }
}


def check_if_is_type_value_objetc(object):
    array_keys = object.keys()
    if "value" in array_keys and "unit" in array_keys:
        return True
    else:
        return False




print(translate_to_portuguese(data_test))
