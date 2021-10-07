SELECT
  attrib_type.attrib_type_id,
  attrib_type.code,
  attrib_type.name,
  attrib_type.description,
  IFNULL(attrib_type_counts.attrib_type_count, 0) AS attrib_type_count,
  attrib_type_counts.attrib_type_examples
FROM attrib_type
LEFT JOIN
(
  SELECT
    attrib_type_id,
    COUNT(*) AS attrib_type_count,
    LEFT(GROUP_CONCAT(DISTINCT gene_attrib.value SEPARATOR ', '), 200) AS attrib_type_examples
  FROM gene_attrib
  GROUP BY attrib_type_id
) AS attrib_type_counts
  ON attrib_type_counts.attrib_type_id = attrib_type.attrib_type_id
ORDER BY attrib_type_count DESC
-- LIMIT 15
