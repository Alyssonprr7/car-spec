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
        "cylinder": {
            "compressionRatio": "Razão de Compressão",
            "pistonStroke": "Curso dos Pistões",
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
        "value": "eqweqw",
        "unit": "dasdas"
    },
    "doors": "Portas",
    "generation": "Geração",
    "platform": "Plataforma",
    "indexCNW": "Índice CNW",
    "origin": [
        "fala",
        "ae"
    ],
    "rankingCNW": "Ranking CNW",

    "engine": {
        "installation": "Instalação",
        "aspiration": "Aspiração",
        "layout": "Disposição",
        "powerSupply": "Alimentação",
        "cylinders": {
            "capacity": {
                "unit": "dsaas",
                "value": "dasda"
            },
            "quantity": ["dasdsas", "dasas", "dasdas"],
            "diameter": {
                "unit": "dasdas",
                "value": "dassdas"
            },
            "pistonStroke": {
                "unit": "dasd",
                "value": "dsadsa"
            }
        }
    }
}

document = {"_id": {"$oid": "5f1750bd4319b19808fff1d9"}, "name": "Fiat Strada Working 1.4 CS", "brand": "Fiat", "model": "Strada Working 1.4 CS", "year": 2013, "price": {"unit": "R$", "value": 26479}, "fuel": "Flex", "IPVA": {"unit": "R$", "value": 530}, "insurance": {"unit": "R$", "value": 1599}, "checkUpPrice": {"unit": "R$", "value": 2324}, "origin": "Nacional", "guarantee": [1, "ano"], "configuration": "Picape", "bodySize": "Compacto", "capacity": 2, "doors": 2, "generation": 1, "platform": "178", "indexCNW": 119.69, "rankingCNW": 7694, "engine": {"installation": "Dianteiro", "aspiration": "Natural", "layout": "Transversal", "powerSupply": "Inje\u00e7\u00e3o multiponto", "valves": {"control": "\u00danico no cabe\u00e7ote, correia dentada", "perCylinder": 2}, "cylinder": {"capacity": {"value": 1368.0, "unit": "cm3"}, "quantity": [4, "em", "linha"], "diameter": {"value": 72.0, "unit": "mm"}, "pistonStroke": {"value": 84.0, "unit": "mm"}, "compressionRatio": [10.35, 1]}, "power": {"max": [{"type": "alcool", "value": 86.0, "unit": "cv"}, {"type": "gasolina", "value": 85.0, "unit": "cv"}, {"rpm": 5750.0}], "specific": {"value": 62.87, "unit": "cv/litro"}, "weight": {"value": 12.22, "unit": "kg/cv"}}, "torque": {"max": [{"type": "alcool", "value": 12.5, "unit": "kgfm"}, {"type": "gasolina", "value": 12.4, "unit": "kgfm"}, {"rpm": 3500.0}], "specific": {"value": 9.14, "unit": "kgfm/litro"}, "weight": {"value": 84.08, "unit": "kg/kgfm"}}, "engineCode": "Fire"}, "transmission": {"traction": "Dianteira", "gear": "Manual", "gearCode": "C513", "coupling": "Embreagem monodisco a seco"}, "suspension": {"front": "Independente, McPherson", "frontElasticElement": "Mola helicoidal", "back": "Eixo r\u00edgido", "backElasticElement": "Mola parab\u00f3lica de l\u00e2mina \u00fanica"}, "brakes": {"front": "Disco ventilado", "back": "Tambor"}, "steering": {"assistance": "N\u00e3o assistida", "minRotateDiameter": "10,7 m"}, "tires": {"front": "175/70 R14", "frontSidewallHeight": {"value": 122.5, "unit": "mm"}, "back": "175/70 R14", "backSidewallHeight": {"value": 122.5, "unit": "mm"}}, "dimensions": {"lenght": {"value": 4409.0, "unit": "mm"}, "width": {"value": 1664.0, "unit": "mm"}, "axesDistance": {"value": 2718.0, "unit": "mm"}, "height": {"value": 1525.0, "unit": "mm"}, "frontGauge": None, "backGauge": None, "trunkVolume": {"value": 1100.0, "unit": "litros"}, "fuelTank": {"value": 58.0, "unit": "litros"}, "weight": {"value": 1051.0, "unit": "kg"}, "payload": {"value": 705.0, "unit": "kg"}, "freeSpanGround": {"value": 175.0, "unit": "mm"}}, "aerodynamics": {"frontArea": None, "dragCoefficient": None, "frontAreaCorrected": None}, "performance": {"maxSpeed": {"value": 164.0, "unit": "km/h"}, "acceleration-0-100-km/h": {"value": 12.5, "unit": "s"}}, "fuelUse": {"urban": [{"value": 6.3, "unit": "km/l", "type": "alcool"}, {"value": 9.2, "unit": "km/l", "type": "gasolina"}], "road": [{"value": 8.4, "unit": "km/l", "type": "alcool"}, {"value": 12.2, "unit": "km/l", "type": "gasolina"}]}, "drivingRange": {"urban": [{"value": 365.4, "unit": "km", "type": "alcool"}, {"value": 533.6, "unit": "km", "type": "gasolina"}], "road": [{"value": 487.2, "unit": "km", "type": "alcool"}, {"value": 707.6, "unit": "km", "type": "gasolina"}]}, "source": {"url": "https://www.carrosnaweb.com.br/fichadetalhe.asp?codigo=1441", "carId": "1441", "domain": "www.carrosnaweb.com.br"}}


def translate_to_portuguese(attributes):  # TODO Implementar exceções para quando não tiver no dicionário
    attributes_in_portuguese = []
    #TODO REFACTORING URGENTE E O QUE FAZER COM OS NULOS?
    for attribute in attributes:
        if ((isinstance(attributes[attribute], dict) is False) and attribute != "_id" and attribute != "id") or (
        isinstance(attributes[attribute], list)):
            attributes_in_portuguese.append(portuguese_dictionary[attribute])
        elif isinstance(attributes[attribute], dict) and (check_if_is_type_value_objetc(attributes[attribute])):
            attributes_in_portuguese.append(portuguese_dictionary[attribute])
        elif isinstance(attributes[attribute], dict) and (
                check_if_is_type_value_objetc(attributes[attribute]) is False):
            for item in attributes[attribute]:
                if ((isinstance(attributes[attribute][item], dict) is False) and attribute != "_id") or (
                isinstance(attributes[attribute][item], list)):
                    attributes_in_portuguese.append(portuguese_dictionary[attribute][item])
                elif isinstance(attributes[attribute][item], dict) and (
                check_if_is_type_value_objetc(attributes[attribute][item])):
                    attributes_in_portuguese.append(portuguese_dictionary[attribute][item])
                elif isinstance(attributes[attribute][item], dict) and (
                        check_if_is_type_value_objetc(attributes[attribute][item]) is False):
                    for new_item in attributes[attribute][item]:
                        attributes_in_portuguese.append(portuguese_dictionary[attribute][item][new_item])

    return attributes_in_portuguese


def get_values(attributes):
    values = []
    for attribute in attributes: # Primeira camada
        if (isinstance(attributes[attribute], dict) is False) and attribute != "id":
            values.append(attributes[attribute])
        elif isinstance(attributes[attribute], dict) and attribute != "_id" and check_if_is_type_value_objetc(attributes[attribute]):
            if attributes[attribute]["unit"] == "R$":
                values.append("{} {}".format(attributes[attribute]["unit"], attributes[attribute]["value"]))
            else:
                values.append("{} {}".format(attributes[attribute]["value"], attributes[attribute]["unit"]))
        elif isinstance(attributes[attribute], dict) and attribute != "_id" and (check_if_is_type_value_objetc(attributes[attribute]) is False):
            for item in attributes[attribute]: #Segunda camada
                if attributes[attribute][item] is None:
                    values.append("Não possuí")
                elif isinstance(attributes[attribute][item], dict) is False:
                    if isinstance(attributes[attribute][item], list):
                        values.append("{}: {}{}, {}: {}{}".format(attributes[attribute][item][0]["type"],
                                                                          attributes[attribute][item][0]["value"],
                                                                          attributes[attribute][item][0]["unit"],
                                                                          attributes[attribute][item][1]["type"],
                                                                          attributes[attribute][item][1]["value"],
                                                                          attributes[attribute][item][1]["unit"],
                                                                          ))
                    else:
                        values.append(attributes[attribute][item])
                elif isinstance(attributes[attribute][item], dict) and (check_if_is_type_value_objetc(attributes[attribute][item])):
                    if attributes[attribute][item]["unit"] == "R$":
                        values.append("{} {}".format(attributes[attribute][item]["unit"], attributes[attribute][item]["value"]))
                    else:
                        values.append("{} {}".format(attributes[attribute][item]["value"], attributes[attribute][item]["unit"]))
                elif isinstance(attributes[attribute][item], dict) and (check_if_is_type_value_objetc(attributes[attribute][item]) is False):
                    for item_four in attributes[attribute][item]:
                        if isinstance(attributes[attribute][item][item_four], dict) is False:
                            if isinstance(attributes[attribute][item][item_four], list):
                                values.append("{}: {}{}, {}: {}{}, {}rpm".format(attributes[attribute][item][item_four][0]["type"],
                                                                                  attributes[attribute][item][item_four][0]["value"],
                                                                                  attributes[attribute][item][item_four][0]["unit"],
                                                                                  attributes[attribute][item][item_four][1]["type"],
                                                                                  attributes[attribute][item][item_four][1]["value"],
                                                                                  attributes[attribute][item][item_four][1]["unit"],
                                                                                  attributes[attribute][item][item_four][2]["rpm"],
                                                                                  ))
                            else:
                                values.append(attributes[attribute][item][item_four])

                        elif isinstance(attributes[attribute][item][item_four], dict) and (check_if_is_type_value_objetc(attributes[attribute][item][item_four])):
                            if attributes[attribute][item][item_four]["unit"] == "R$":
                                values.append("{} {}".format(attributes[attribute][item][item_four]["unit"], attributes[attribute][item][item_four]["value"]))
                            else:
                                values.append("{} {}".format(attributes[attribute][item][item_four]["value"], attributes[attribute][item][item_four]["unit"]))

                        elif isinstance(attributes[attribute][item][item_four], dict) and (check_if_is_type_value_objetc(attributes[attribute][item][item_four]) is False):
                            print("EXCEÇÃO", attributes[attribute][item][item_four])



    return values


objeto = {
    "ola": {
        "value": "DASDSD",
        "unit": "asdasdas"
    },
    "hi": {
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


#print(check_if_is_type_value_objetc(document["year"]))
