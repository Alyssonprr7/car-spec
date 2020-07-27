json_to_portuguese = {
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


def translate_to_portuguese(all_attributes):
    attributes_in_portuguese = []
    for attribute_from_first_iteration in all_attributes:
        if is_not_dict_and_not_ID(all_attributes, attribute_from_first_iteration):
            attributes_in_portuguese.append(json_to_portuguese[attribute_from_first_iteration])
        elif is_object_and_type_value(all_attributes, attribute_from_first_iteration):
            attributes_in_portuguese.append(json_to_portuguese[attribute_from_first_iteration])
        elif is_not_object_type_value_but_not_mongoId(all_attributes, attribute_from_first_iteration):
            for attribute_from_second_iteration in all_attributes[attribute_from_first_iteration]:
                if is_not_dict_and_not_ID(all_attributes[attribute_from_first_iteration],
                                          attribute_from_second_iteration):
                    attributes_in_portuguese.append(
                        json_to_portuguese[attribute_from_first_iteration][attribute_from_second_iteration])
                elif is_object_and_type_value(all_attributes[attribute_from_first_iteration],
                                              attribute_from_second_iteration):
                    attributes_in_portuguese.append(
                        json_to_portuguese[attribute_from_first_iteration][attribute_from_second_iteration])
                elif is_not_object_type_value_but_not_mongoId(all_attributes[attribute_from_first_iteration],
                                                              attribute_from_second_iteration):
                    for attribute_from_third_iteration in all_attributes[attribute_from_first_iteration][
                        attribute_from_second_iteration]:
                        attributes_in_portuguese.append(
                            json_to_portuguese[attribute_from_first_iteration][attribute_from_second_iteration][
                                attribute_from_third_iteration])

    return attributes_in_portuguese


def get_values(all_attributes):
    values = []
    for attribute_from_first_iteration in all_attributes:
        if (all_attributes[attribute_from_first_iteration]) is None:
            values.append("Nulo")
        elif is_not_dict_and_not_ID(all_attributes, attribute_from_first_iteration):
            values.append(all_attributes[attribute_from_first_iteration])
        elif is_object_and_type_value(all_attributes, attribute_from_first_iteration):
            order_unit_value(all_attributes[attribute_from_first_iteration], values)
        elif is_not_object_type_value_but_not_mongoId(all_attributes, attribute_from_first_iteration):
            for attribute_from_second_iteration in all_attributes[attribute_from_first_iteration]:
                if all_attributes[attribute_from_first_iteration][attribute_from_second_iteration] is None:
                    values.append("Nulo")
                elif isinstance(all_attributes[attribute_from_first_iteration][attribute_from_second_iteration],
                                dict) is False:
                    if isinstance(all_attributes[attribute_from_first_iteration][attribute_from_second_iteration],
                                  list):
                        concat_a_list_of_string_values(
                            all_attributes[attribute_from_first_iteration][attribute_from_second_iteration], values)
                    else:
                        values.append(all_attributes[attribute_from_first_iteration][attribute_from_second_iteration])
                elif is_object_and_type_value(all_attributes[attribute_from_first_iteration],
                                              attribute_from_second_iteration):
                    order_unit_value(all_attributes[attribute_from_first_iteration][attribute_from_second_iteration],
                                     values)
                elif is_not_object_type_value_but_not_mongoId(all_attributes[attribute_from_first_iteration],
                                                              attribute_from_second_iteration):
                    for attribute_from_fourth_iteration in all_attributes[attribute_from_first_iteration][
                        attribute_from_second_iteration]:
                        if (all_attributes[attribute_from_first_iteration]) is None:
                            values.append("Nulo")
                        elif isinstance(all_attributes[attribute_from_first_iteration][attribute_from_second_iteration][
                                            attribute_from_fourth_iteration], dict) is False:
                            if isinstance(
                                    all_attributes[attribute_from_first_iteration][attribute_from_second_iteration][
                                        attribute_from_fourth_iteration], list):
                                concat_a_list_of_string_values(
                                    all_attributes[attribute_from_first_iteration][attribute_from_second_iteration][
                                        attribute_from_fourth_iteration], values)
                            else:
                                values.append(
                                    all_attributes[attribute_from_first_iteration][attribute_from_second_iteration][
                                        attribute_from_fourth_iteration])

                        elif is_object_and_type_value(
                                all_attributes[attribute_from_first_iteration][attribute_from_second_iteration],
                                attribute_from_fourth_iteration):
                            order_unit_value(
                                all_attributes[attribute_from_first_iteration][attribute_from_second_iteration][
                                    attribute_from_fourth_iteration], values)
    return values


def is_type_value_object(param_object):
    array_keys = param_object.keys()
    if "value" in array_keys and "unit" in array_keys:
        return True
    else:
        return False


def order_unit_value(param_object, list_values):
    if param_object["unit"] == "R$":
        list_values.append("{} {}".format(param_object["unit"], param_object["value"]))
    else:
        list_values.append("{} {}".format(param_object["value"], param_object["unit"]))


def concat_a_list_of_string_values(list_string, list_values):
    if "rpm" in list_string:
        list_values.append("{}: {}{}, {}: {}{}, {}rpm".format(list_string[0]["type"],
                                                              list_string[0]["value"],
                                                              list_string[0]["unit"],
                                                              list_string[1]["type"],
                                                              list_string[1]["value"],
                                                              list_string[1]["unit"],
                                                              list_string[2]["rpm"],
                                                              ))
    else:
        list_values.append("{}: {}{}, {}: {}{}".format(list_string[0]["type"],
                                                       list_string[0]["value"],
                                                       list_string[0]["unit"],
                                                       list_string[1]["type"],
                                                       list_string[1]["value"],
                                                       list_string[1]["unit"],
                                                       ))


def is_not_dict_and_not_ID(iteractor_attribute, attribute):
    if (isinstance(iteractor_attribute[attribute], dict) is False) and attribute != "id":
        return True
    else:
        return False


def is_object_and_type_value(iteractor_attribute, attribute):
    if isinstance(iteractor_attribute[attribute], dict) and is_type_value_object(
            iteractor_attribute[attribute]):
        return True
    else:
        return False


def is_not_object_type_value_but_not_mongoId(iteractor_attribute, attribute):
    if isinstance(iteractor_attribute[attribute], dict) and attribute != "_id" and (
            is_type_value_object(iteractor_attribute[attribute]) is False):
        return True
    else:
        return False

