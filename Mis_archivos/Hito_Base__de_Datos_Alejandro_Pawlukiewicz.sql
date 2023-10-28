DROP DATABASE organización;
CREATE DATABASE organización;
USE organización;

-- Crear la tabla de calles
CREATE TABLE calles (
    id_calle INT PRIMARY KEY,
    nombre_calle VARCHAR(255)
);

-- Crear la tabla de barrios
CREATE TABLE barrios (
    id_barrio INT PRIMARY KEY,
    nombre_barrio VARCHAR(255)
);

-- Crear la tabla de tramos
CREATE TABLE tramos (
    id_tramo INT PRIMARY KEY,
    id_calle_inicio INT,
    id_calle_fin INT,
    id_barrio INT,
    FOREIGN KEY (id_calle_inicio) REFERENCES calles(id_calle),
    FOREIGN KEY (id_calle_fin) REFERENCES calles(id_calle),
    FOREIGN KEY (id_barrio) REFERENCES barrios(id_barrio)
);

-- Crear la tabla de líneas de autobuses
CREATE TABLE lineas_autobuses (
    id_linea_autobus INT PRIMARY KEY,
    nombre_linea_autobus VARCHAR(255)
);

-- Crear la tabla de relaciones entre líneas de autobuses y tramos
CREATE TABLE lineas_autobuses_tramos (
    id_linea_autobus INT,
    id_tramo_inicio INT,
    id_tramo_fin INT,
    FOREIGN KEY (id_linea_autobus) REFERENCES lineas_autobuses(id_linea_autobus),
    FOREIGN KEY (id_tramo_inicio) REFERENCES tramos(id_tramo),
    FOREIGN KEY (id_tramo_fin) REFERENCES tramos(id_tramo)
);

-- Crear la tabla de líneas de metro
CREATE TABLE lineas_metro (
    id_linea_metro INT PRIMARY KEY,
    nombre_linea_metro VARCHAR(255)
);

-- Crear la tabla de estaciones
CREATE TABLE estaciones (
    id_estacion INT PRIMARY KEY,
    nombre_estacion VARCHAR(255)
);

-- Crear la tabla de relaciones entre líneas de metro y estaciones
CREATE TABLE lineas_metro_estaciones (
    id_linea_metro INT,
    id_estacion_inicio INT,
    id_estacion_fin INT,
    FOREIGN KEY (id_linea_metro) REFERENCES lineas_metro(id_linea_metro),
    FOREIGN KEY (id_estacion_inicio) REFERENCES estaciones(id_estacion),
    FOREIGN KEY (id_estacion_fin) REFERENCES estaciones(id_estacion)
);

-- Crear la tabla de puntos de interés
CREATE TABLE puntos_interes (
    id_punto_interes INT PRIMARY KEY,
    nombre_punto_interes VARCHAR(255),
    tipo_punto_interes VARCHAR(255)
);

-- Crear la tabla de localizaciones
CREATE TABLE localizaciones (
    id_localizacion INT PRIMARY KEY,
    latitud_localizacion FLOAT(10, 6),
    longitud_localizacion FLOAT(10, 6)
);

-- Crear la tabla de relaciones entre puntos de interés y localizaciones
CREATE TABLE puntos_interes_localizaciones (
    id_punto_interes INT,
    id_localizacion INT,
    FOREIGN KEY (id_punto_interes) REFERENCES puntos_interes(id_punto_interes),
    FOREIGN KEY (id_localizacion) REFERENCES localizaciones(id_localizacion)
);

-- Insertar datos en la tabla de calles
INSERT INTO calles (id_calle, nombre_calle)
VALUES (1, 'Calle Mayor'),
       (2, 'Calle del Sol'),
       (3, 'Calle de la Luna'),
       (4, 'Calle Menor'),
       (5, 'Calle Andalucia'),
       (6, 'Calle de Sevilla'),
       (7, 'Calle del Pastor'),
       (8, 'Calle de la Princesa');

-- Insertar datos en la tabla de barrios
INSERT INTO barrios (id_barrio, nombre_barrio)
VALUES (1, 'Barrio de Salamanca'),
       (2, 'Barrio de Chamberí'),
       (3, 'Barrio de Lavapiés'),
       (4, 'Barrio de Bilbao'),
       (5, 'Barrio de Pamplona'),
       (6, 'Barrio de Vallegrande'),
       (7, 'Barrio de Seseña'),
       (8, 'Barrio de Valdemoro');

-- Insertar datos en la tabla de tramos
INSERT INTO tramos (id_tramo, id_calle_inicio, id_calle_fin, id_barrio)
VALUES (1, 1, 2, 1),
       (2, 2, 3, 2),
       (3, 3, 4, 3),
       (4, 4, 5, 4),
       (5, 5, 6, 5),
       (6, 6, 7, 6),
       (7, 7, 8, 7),
       (8, 8, 1, 8);

-- Insertar datos en la tabla de líneas de autobuses
INSERT INTO lineas_autobuses (id_linea_autobus, nombre_linea_autobus)
VALUES (1, 'Línea 1'),
       (2, 'Línea 2'),
       (3, 'Línea 3'),
       (4, 'Línea 4'),
       (5, 'Línea 5'),
       (6, 'Línea 6'),
       (7, 'Línea 7'),
       (8, 'Línea 8');

-- Insertar datos en la tabla de relaciones entre líneas de autobuses y tramos
INSERT INTO lineas_autobuses_tramos (id_linea_autobus, id_tramo_inicio, id_tramo_fin)
VALUES (1, 1, 2),
       (2, 2, 3),
       (3, 3, 4),
       (4, 4, 5),
       (5, 5, 6),
       (6, 6, 7),
       (7, 7, 8),
       (8, 8, 1);

-- Insertar datos en la tabla de líneas de metro
INSERT INTO lineas_metro (id_linea_metro, nombre_linea_metro)
VALUES (1, 'Línea A'),
       (2, 'Línea B'),
       (3, 'Línea C'),
       (4, 'Línea D'),
       (5, 'Línea E'),
       (6, 'Línea F'),
       (7, 'Línea G'),
       (8, 'Línea H');

-- Insertar datos en la tabla de estaciones
INSERT INTO estaciones (id_estacion, nombre_estacion)
VALUES (1, 'Estación A'),
       (2, 'Estación B'),
       (3, 'Estación C'),
       (4, 'Estación D'),
       (5, 'Estación E'),
       (6, 'Estación F'),
       (7, 'Estación G'),
       (8, 'Estación H');

-- Insertar datos en la tabla de relaciones entre líneas de metro y estaciones
INSERT INTO lineas_metro_estaciones (id_linea_metro, id_estacion_inicio, id_estacion_fin)
VALUES (1, 1, 2),
       (2, 2, 3),
       (3, 3, 4),
       (4, 4, 5),
       (5, 5, 6),
       (6, 6, 7),
       (7, 7, 8),
       (8, 8, 1);

-- Insertar datos en la tabla de puntos de interés
INSERT INTO puntos_interes (id_punto_interes,nombre_punto_interes)
VALUES(1,'Museo del Prado'),
      (2,'Parque del Retiro'),
      (3,'Palacio Real'),
      (4,'Templo de Debod'),
      (5,'Museo Reina Sofía'),
      (6,'Mercado de San Miguel'),
      (7,'Teleférico de Madrid'),
      (8,'Catedral de la Almudena');


SELECT *
FROM calles
WHERE id_calle = "1";

SELECT nombre_linea_autobus
FROM lineas_autobuses
WHERE id_linea_autobus IN (1,5,8);

SELECT nombre_punto_interes
FROM puntos_interes
WHERE id_punto_interes BETWEEN 2 AND 6;

SELECT nombre_calle
FROM calles
ORDER BY id_calle DESC;

SELECT *
FROM barrios
WHERE nombre_barrio LIKE 'B%' 'S%';

SELECT nombre_estacion
FROM estaciones
LIMIT 4;

SELECT DISTINCT nombre_linea_metro
FROM lineas_metro
WHERE id_linea_metro BETWEEN 1 AND 4;

SELECT
FROM

SELECT
FROM

SELECT
FROM