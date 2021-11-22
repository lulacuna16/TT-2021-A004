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
INSERT INTO categorias (nombre_cat) VALUES ("letras"),("numeros"),("cuerpo"),("colores"),("dias");

-- Señas - letras
INSERT INTO senas (nombre_sena,id_categoria) VALUES ("a",1),("b",1),("c",1),("d",1),("e",1),("f",1),
    ("g",1),("h",1),("i",1),("j",1),("k",1),("l",1),("ll",1),("m",1),("n",1),("ñ",1),("o",1),("p",1),
    ("q",1),("r",1),("rr",1),("s",1),("t",1),("u",1),("v",1),("w",1),("x",1),("y",1),("z",1);

-- Señas - numeros
INSERT INTO senas (nombre_sena,id_categoria) VALUES ("1",2),("2",2),("3",2),("4",2),("5",2),("6",2),
    ("7",2),("8",2),("9",2),("10",2),("20",2),("30",2),("40",2),("50",2),("60",2),("70",2),("80",2),
    ("90",2),("100",2);

-- Señas - cuerpo
INSERT INTO senas (nombre_sena,id_categoria) VALUES ("cuello",3),("espalda",3),("diente",3),("hombro",3),
    ("lengua",3),("mano",3),("muñeca",3),("nariz",3),("ojo",3),("pelo",3),("pulgar",3),("uña",3),("boca",3),
    ("oreja",3),("brazo",3),("codo",3),("estomago",3);

-- Señas - colores
INSERT INTO senas (nombre_sena,id_categoria) VALUES ("amarillo",4),("azul",4),("rojo",4),("verde",4),
    ("rosa",4),("cafe",4),("morado",4),("naranja",4),("gris",4),("blanco",4),("negro",4);

-- Señas - dias
INSERT INTO senas (nombre_sena,id_categoria) VALUES ("lunes",5),("martes",5),("miercoles",5),("jueves",5),
    ("viernes",5),("sabado",5),("domingo",5);

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