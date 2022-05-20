PRAGMA foreign_keys = ON;

DROP TABLE senas;
DROP TABLE progresos;
DROP TABLE usuarios;
DROP TABLE categorias;

CREATE TABLE usuarios(
    id_usuario INTEGER PRIMARY KEY ASC,
    nombre VARCHAR(30),
    progreso_pnt DECIMAL(5,2),
    senas_completadas INTEGER
);

CREATE TABLE categorias(
    id_categoria INTEGER PRIMARY KEY ASC,
    nombre_cat VARCHAR(30)
);

CREATE TABLE senas(
    id_sena INTEGER PRIMARY KEY ASC,
    nombre_sena VARCHAR(30),
    tipo_sena INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    FOREIGN KEY (id_categoria)
        REFERENCES categorias (id_categoria)
        ON DELETE CASCADE
);

CREATE TABLE progresos(
    id_status INTEGER PRIMARY KEY ASC,
    id_usuario INTEGER NOT NULL,
    id_sena INTEGER NOT NULL,
    UNIQUE(id_usuario,id_sena),
    FOREIGN KEY (id_usuario)
        REFERENCES usuarios (id_usuario)
        ON DELETE CASCADE,
    FOREIGN KEY (id_sena)
        REFERENCES senas (id_sena)
        ON DELETE CASCADE
);

-- Categorias
INSERT INTO categorias (nombre_cat) VALUES ("letras"),("numeros"),("cuerpo"),("dias"),("colores");

-- Señas - letras
INSERT INTO senas (nombre_sena,tipo_sena,id_categoria) VALUES ("a",0,1),("b",0,1),("c",0,1),("d",0,1),("e",0,1),("f",0,1),
            ("g",0,1),("h",0,1),("i",0,1),("j",1,1),("k",1,1),("l",0,1),("m",0,1),("n",0,1),("ñ",1,1),("o",0,1),("p",0,1),
            ("q",1,1),("r",0,1),("s",0,1),("t",0,1),("u",0,1),("v",0,1),("w",0,1),("x",1,1),("y",0,1),("z",1,1);

-- Señas - numeros
INSERT INTO senas (nombre_sena,tipo_sena,id_categoria) VALUES ("1",0,2),("2",0,2),("3",0,2),("4",0,2),("5",0,2),("6",0,2),
        ("7",0,2),("8",0,2),("9",1,2),("10",1,2),("20",1,2),("30",1,2),("40",1,2),("50",1,2),("60",1,2),("70",1,2),("80",1,2),
        ("90",1,2),("100",1,2);

-- Señas - cuerpo
INSERT INTO senas (nombre_sena,tipo_sena,id_categoria) VALUES ("boca",1,3),("brazo",1,3),("codo",1,3),("cuello",0,3),("diente",0,3),
    ("espalda",0,3),("estómago",0,3),("hombro",0,3),("lengua",0,3),("mano",0,3),("muñeca",0,3),("nariz",0,3),("ojo",0,3),("oreja",1,3),
    ("pelo",0,3),("pulgar",0,3),("uña",0,3);

-- Señas - dias
INSERT INTO senas (nombre_sena,tipo_sena,id_categoria) VALUES ("lunes",1,4),("martes",1,4),("miércoles",1,4),("jueves",1,4),
    ("viernes",1,4),("sábado",1,4),("domingo",1,4);

-- Señas - colores
INSERT INTO senas (nombre_sena,tipo_sena,id_categoria) VALUES ("amarillo",1,5),("azul",1,5),("rojo",1,5),("verde",1,5),
    ("rosa",1,5),("café",1,5),("morado",1,5),("naranja",1,5),("gris",1,5),("blanco",1,5),("negro",1,5);

--  Usuarios
INSERT INTO usuarios (nombre,progreso_pnt,senas_completadas) VALUES ("Usuario 1", 0, 0),
    ("Usuario 2", 0, 0),("Usuario 3", 0, 0),("Usuario 4", 0, 0);



-- .headers ON
-- SELECT
--     s.nombre_sena AS Seña,
--     c.nombre_cat AS Categoria
--     FROM senas s
--     INNER JOIN categorias c
--     ON s.id_categoria = c.id_categoria;