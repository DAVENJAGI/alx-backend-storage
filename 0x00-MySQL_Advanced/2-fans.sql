-- A script that ranks country origin of bands Ordered by number of non unique fans

SELECT origin, fans as nb_fans
FROM holberton.metal_bands
ORDER BY nb_fans DESC;
