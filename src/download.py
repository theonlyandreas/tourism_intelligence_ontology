import os
import requests

base_url = "https://dataestur.azure-api.net/API-SEGITTUR-v1/"

# paises
paises_paths = {
    'eoac': {
        'path': "../eoac/pais/eoac_pais_",
        'start': "EOAC_PAIS_DL?Pa%C3%ADs=",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eoal': {
        'path': "../eoal/pais/eoal_pais_",
        'start': "EOAL_PAIS_DL?Pa%C3%ADs=",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eoap': {
        'path': "../eoap/pais/eoap_pais_",
        'start': "EOAP_PAIS_DL?Pa%C3%ADs=",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eoh': {
        'path': "../eoh/pais/eoh_pais_",
        'start': "EOH_PAIS_DL?Pa%C3%ADs=",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eotr': {
        'path': "../eotr/pais/eotr_pais_",
        'start': "EOTR_PAIS_DL?Pa%C3%ADs=",
        'end': "&Lugar%20de%20residencia=Todos",
    }
}

paises = [
    "%C3%81frica",
    "Alemania",
    "Am%C3%A9rica%20%28sin%20EEUU%29",
    "Austria",
    "B%C3%A9lgica",
    "Dinamarca",
    "Estados%20Unidos%20de%20Am%C3%A9rica",
    "Finlandia",
    "Francia",
    "Grecia",
    "Irlanda",
    "Italia",
    "Luxemburgo",
    "Noruega",
    "Otros%20Pa%C3%ADses%20Europeos",
    "Pa%C3%ADses%20Bajos",
    "Polonia",
    "Portugal",
    "Reino%20Unido",
    "Rep%C3%BAblica%20Checa",
    "Residentes%20en%20Espa%C3%B1a",
    "Resto%20de%20la%20U.E.",
    "Resto%20del%20Mundo",
    "Rusia",
    "Suecia",
    "Suiza",
]

# provincia
provincias_paths = {
    'eoac': {
        'path': "../eoac/provincia/eoac_provincia_",
        'start': "EOAC_PROVINCIA_DL?Lugar%20de%20residencia=Todos",
        'end': "",
    },
    'eoap': {
        'path': "../eoap/provincia/eoap_provincia_",
        'start': "EOAP_PROVINCIA_DL?Lugar%20de%20residencia=Todos",
        'end': "",
    },
    'eotr': {
        'path': "../eotr/provincia/eotr_provincia_",
        'start': "EOTR_PROVINCIA_DL?Lugar%20de%20residencia=Todos",
        'end': "",
    }
}

provincias = [
    "Araba%2F%C3%81lava",
    "Albacete",
    "Alicante%2FAlacant",
    "Almer??a",
    "??vila",
    "Badajoz",
    "Balears",
    "Illes",
    "Barcelona",
    "Burgos",
    "C??ceres",
    "C??diz",
    "Castell??n%2FCastell??",
    "Ciudad Real",
    "C??rdoba",
    "Coru??a%2C%20A",
    "Cuenca",
    "Girona",
    "Granada",
    "Guadalajara",
    "Gipuzkoa",
    "Huelva",
    "Huesca",
    "Ja??n",
    "Le??n",
    "Lleida",
    "Rioja%2C%20La",
    "Lugo",
    "Madrid",
    "M??laga",
    "Murcia",
    "Navarra",
    "Ourense",
    "Asturias",
    "Palencia",
    "Palmas%2C%20Las",
    "Pontevedra",
    "Salamanca",
    "Santa Cruz de Tenerife",
    "Cantabria",
    "Segovia",
    "Sevilla",
    "Soria",
    "Tarragona",
    "Teruel",
    "Toledo",
    "Valencia%2FVal??ncia",
    "Valladolid",
    "Bizkaia",
    "Zamora",
    "Zaragoza",
    "Ceuta",
    "Melilla",
]

# eoac punto turistico
punto_turistico_paths = {
    'eoac': {
        'path': "../eoac/punto_turistico/eoac_punto_turistico_",
        'start': "EOAC_PUNT_TUR_DL?Punto%20tur%C3%ADstico=%20",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eoap': {
        'path': "../eoap/punto_turistico/eoap_punto_turistico_",
        'start': "EOAP_PUNT_TUR_DL?Punto%20tur%C3%ADstico=%20",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eoh': {
        'path': "../eoh/punto_turistico/eoh_punto_turistico_",
        'start': "EOH_PUNT_TUR_DL?Punto%20tur%C3%ADstico=%20",
        'end': "&Lugar%20de%20residencia=Todos",
    }
}

punto_turisticos = [
    "Benidorm",
    "Campello%2C%20el",
    "Elche%2FElx",
    "Villajoyosa%2FVila Joiosa%2C%20la",
    "Moj??car",
    "Conil de la Frontera",
    "Tarifa",
    "Benicasim%2FBenic??ssim",
    "Oropesa del Mar%2FOrpesa",
    "Pen??scola%2FPe????scola",
    "Blanes",
    "Castell?? d'Emp??ries",
    "Castell-Platja d'Aro",
    "Sant Pere Pescador",
    "Torroella de Montgr??",
    "Motril",
    "Isla Cristina",
    "Santiago-Pontones",
    "Marbella",
    "V??lez-M??laga",
    "Cartagena",
    "Fortuna",
    "Mazarr??n",
    "Llanes",
    "Cambrils",
    "Mont-roig del Camp",
    "Tarragona",
    "Oliva",
]

punto_turisticos_2 = [
    'Vitoria-Gasteiz',
    'Alf??s del Pi, l\'',
    'Alicante/Alacant',
    'Benidorm',
    'Calp',
    'D??nia',
    'J??vea/X??bia',
    'Teulada',
    'Torrevieja',
    'Roquetas de Mar',
    'Calvi??',
    'Palma',
    'Barcelona',
    'Castelldefels',
    'C??ceres',
    'Tarifa',
    'C??rdoba',
    'Cuenca',
    'Almu????car',
    'Capileira',
    'Granada',
    'Alpujarra de la Sierra',
    'Iruela, La',
    'Segura de la Sierra',
    'Ezcaray',
    'Madrid',
    'Benalm??dena',
    'Fuengirola',
    'M??laga',
    'Marbella',
    'Mijas',
    'Nerja',
    'Torremolinos',
    'Cartagena',
    'Mazarr??n',
    'San Javier',
    'Pamplona/Iru??a',
    'Cudillero',
    'Antigua',
    'Mog??n',
    'Oliva, La',
    'P??jara',
    'San Bartolom?? de Tirajana',
    'Teguise',
    'T??as',
    'Yaiza',
    'Adeje',
    'Alajer??',
    'Arona',
    'Bre??a Baja',
    'Frontera',
    'Granadilla de Abona',
    'Llanos de Aridane, Los',
    'Paso, El',
    'Puerto de la Cruz',
    'San Miguel de Abona',
    'San Sebasti??n de la Gomera',
    'Santa Cruz de la Palma',
    'Santiago del Teide, Tazacorte',
    'Valle Gran Rey',
    'Sevilla',
    'Cullera',
    'Val??ncia',
    'Zaragoza',
]

punto_turisticos_final = list(set(punto_turisticos + punto_turisticos_2))

# eoac zona turistica
zona_turistica_paths = {
    'eoac': {
        'path': "../eoac/zona_turistica/eoac_zona_turistica_",
        'start': "EOAC_ZONA_TUR_DL?Lugar%20de%20residencia=Todos&Zona%20tur%C3%ADstica=",
        'end': "",
    },
    'eoap': {
        'path': "../eoap/zona_turistica/eoap_zona_turistica_",
        'start': "EOAP_ZONA_TUR_DL?Lugar%20de%20residencia=Todos&Zona%20tur%C3%ADstica=",
        'end': "",
    },
    'eoh': {
        'path': "../eoh/zona_turistica/eoh_zona_turistica_",
        'start': "EOH_ZONA_TUR_DL?CCAA=Todos&Lugar%20de%20residencia=Todos&Zona%20tur%C3%ADstica=",
        'end': "",
    },
    'eotr': {
        'path': "../eotr/zona_turistica/eotr_zona_turistica_",
        'start': "EOTR_ZONA_TUR_DL?CCAA=Todos&Lugar%20de%20residencia=Todos&Zona%20tur%C3%ADstica=",
        'end': "",
    },
}

zona_turisticas = [
    "Andaluc??a: Costa De Almer??a",
    "Andaluc??a: Costa De La Luz (Huelva)",
    "Andaluc??a: Costa De La Luz De C??diz",
    "Andaluc??a: Costa Del Sol (M??laga)",
    "Andaluc??a: Costa Tropical (Granada)",
    "Asturias (Principado De): Costa Verde",
    "Catalu??a: Catalu??a Central",
    "Catalu??a: Costa  Barcelona",
    "Catalu??a: Costa  Barcelona 2015",
    "Catalu??a: Costa  Barcelona 2016",
    "Catalu??a: Costa Barcelona-Maresme",
    "Catalu??a: Costa Brava",
    "Catalu??a: Costa Daurada",
    "Catalu??a: Costa Del Garraf",
    "Catalu??a: Terres de l'Ebre",
    "Comunitat Valenciana: Costa Azahar",
    "Comunitat Valenciana: Costa Blanca",
    "Comunitat Valenciana: Costa de Castell??n",
    "Comunitat Valenciana: Costa Valencia",
    "Extremadura: Norte de Extremadura",
    "Galicia: R??as Altas (A Coru??a)",
    "Galicia: R??as Baixas (Pontevedra y A Coru??a)",
    "Murcia (Regi??n De): Costa C??lida",
    "P. Nacional Aig??estortes ",
    "P. Nacional de Sierra de Guadarrama",
    "P. Nacional Ordesa",
    "P. Nacional Sierra Nevada",
    "P. Natural Alt Pirineu",
    "P. Natural Cad??-Moixer?? ",
    "P. Natural de los Aiguamolls de I'Empord??",
    "P. Natural Do??ana",
    "P. Natural Los Alcornocales ",
    "P. Natural Serra Calderona ",
    "P. Natural Serra Calderon ",
    "P. Natural Sierra de Grazalema",
    "P. Natural Sierra de Hornachuelos",
    "P. Natural Sierra de las Nieves",
    "P. Natural Sierra Nevada ",
    "P. Natural Sierra y Ca??ones de Guara",
    "P. Natural Sierras de Cazorla, Segura y las Villas",
    "P. Natural Zona Volc??nica de la Garrotxa ",
    "Pais Vasco: Costa Bizkaia",
    "Pais Vasco: Costa Guipuzkoa",
    "Pirineo Aragon??s",
    "Pirineo Catal??n",
    "Pirineo Navarro",
    "Pirineus",
]

# ccaa
ccaa_paths = {
    'eoal': {
        'path': "../eoal/ccaa/eoal_ccaa_",
        'start': "EOAL_CCAA_DL?CCAA=",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eoap': {
        'path': "../eoap/ccaa/eoap_ccaa_",
        'start': "EOAP_CCAA_DL?CCAA=",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eoh': {
        'path': "../eoh/ccaa/eoh_ccaa_",
        'start': "EOH_CCAA_PROV_DL?CCAA=",
        'end': "&Lugar%20de%20residencia=Todos",
    },
    'eotr': {
        'path': "../eotr/ccaa/eotr_ccaa_",
        'start': "EOTR_CCAA_DL?CCAA=",
        'end': "&Lugar%20de%20residencia=Todos",
    },
}

ccaa = [
    'Andaluc??a',
    'Arag??n',
    'Asturias, Principado de',
    'Balears, Illes',
    'Canarias',
    'Cantabria',
    'Castilla y Le??n',
    'Castilla-La%20Mancha',
    'Catalu??a',
    'Comunitat Valenciana',
    'Extremadura',
    'Galicia',
    'Madrid, Comunidad de',
    'Murcia, Regi??n de',
    'Navarra, Comunidad Foral de',
    'Pa??s Vasco',
    'Rioja, La',
    'Ceuta',
    'Melilla',
]

# categoria
eoh_categorias_paths = {
    'eoh': {
        'path': "../eoh/categoria/eoh_categoria_",
        'start': "EOH_CATEGORIA_DL?Pa%C3%ADs=",
        'end': "&Lugar%20de%20residencia=Todos",
    }
}
eoh_categorias = [
    'Una estrella de plata',
    'Una estrella de oro',
    'Dos estrellas de oro',
    'Tres y dos estrellas de plata',
    'Tres estrellas de oro',
    'Cuatro estrellas de oro',
    'Cinco estrellas de oro',
]

eoac_categorias_paths = {
    'eoac': {
        'path': "../eoac/categoria/eoac_categoria_",
        'start': "EOAC_CATEGORIA_DL?Pa%C3%ADs=",
        'end': "&Lugar%20de%20residencia=Todos",
    }
}
eoac_categorias = [
    'Lujo%20y%201%C2%AA%20categor%C3%ADa',
    '2%C2%AA%20categor%C3%ADa',
    '3%C2%AA%20categor%C3%ADa',
]


# complete set of paths and values
download_data = {
    'eoac_categoria': (eoac_categorias_paths, eoac_categorias),
    'eoh_categoria': (eoh_categorias_paths, eoh_categorias),
    'pais': (paises_paths, paises),
    'province': (provincias_paths, provincias),
    'ccaa': (ccaa_paths, ccaa),
    'touristic_point': (punto_turistico_paths, punto_turisticos_final),
    'touristic_zone': (zona_turistica_paths, zona_turisticas),
}

# download
for subsurvey, (subsurvey_paths, subsurvey_data) in list(download_data.items()):
    for type, paths in list(subsurvey_paths.items()):
        for element in subsurvey_data:
            url = base_url + paths['start'] + element + paths['end']
            resp = requests.get(url)

            path = paths['path'] + element.lower() + ".xls"
            dir_path, file_path = path.rsplit('/', 1)
            dir_path_start, dir_path_rest = dir_path.split('/', 1)
            dir_path = dir_path_start + '/data/' + dir_path_rest
            path = dir_path + '/' + file_path
            if not os.path.isdir(dir_path):
                os.makedirs(dir_path)

            output = open(path, "wb")
            output.write(resp.content)
            output.close()
