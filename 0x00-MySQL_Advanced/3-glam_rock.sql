-- A script that lists all bands with glam rick as their style ranked by longevity
SELECT band_name, IFNULL(split, YEAR(CURRENT_DATE())) - formed AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC;
