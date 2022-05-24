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


-- 100% progreso abecedario y numeros usuario 1
INSERT INTO progresos (id_usuario,id_sena) VALUES (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,12),
(1,13), (1,14), (1,15), (1,16), (1,17), (1,18), (1,19), (1,20), (1,21), (1,22), (1,23), (1,24), (1,25), (1,26), (1,27), (1,28), (1,29),
(1,30), (1,31), (1,32), (1,33), (1,34), (1,35), (1,36), (1,37), (1,38), (1,39), (1,40), (1,41), (1,42), (1,43), (1,44), (1,45), (1,46);

-- 100% progreso cuerpo y días usuario 2
INSERT INTO progresos (id_usuario,id_sena) VALUES (2,47), (2,48), (2,49), (2,50), (2,51), (2,52), (2,53), (2,54), (2,55), (2,56), (2,57),
(2,58), (2,59), (2,60), (2,61), (2,62), (2,63), (2,64), (2,65), (2,66), (2,67), (2,68), (2,69), (2,70);

-- 100% progreso colores usuario 3
INSERT INTO progresos (id_usuario,id_sena) VALUES (3,71), (3,72), (3,73), (3,74), (3,75), (3,76), (3,77), (3,78), (3,79), (3,80), (3,81);

-- 100% progreso todas las categorías usuario 4
INSERT INTO progresos (id_usuario,id_sena) VALUES (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9), (4,10), (4,11), (4,12),
    (4,13), (4,14), (4,15), (4,16), (4,17), (4,18), (4,19), (4,20), (4,21), (4,22), (4,23), (4,24), (4,25), (4,26), (4,27), (4,28), (4,29),
    (4,30), (4,31), (4,32), (4,33), (4,34), (4,35), (4,36), (4,37), (4,38), (4,39), (4,40), (4,41), (4,42), (4,43), (4,44), (4,45), (4,46),
    (4,47), (4,48), (4,49), (4,50), (4,51), (4,52), (4,53), (4,54), (4,55), (4,56), (4,57), (4,58), (4,59), (4,60), (4,61), (4,62), (4,63),
    (4,64), (4,65), (4,66), (4,67), (4,68), (4,69), (4,70), (4,71), (4,72), (4,73), (4,74), (4,75), (4,76), (4,77), (4,78), (4,79), (4,80),
    (4,81);

-- .headers ON
-- SELECT
--     s.nombre_sena AS Seña,
--     c.nombre_cat AS Categoria
--     FROM senas s
--     INNER JOIN categorias c
--     ON s.id_categoria = c.id_categoria;