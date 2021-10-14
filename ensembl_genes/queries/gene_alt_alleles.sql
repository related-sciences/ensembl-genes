SELECT
  gene.stable_id AS ensembl_gene_id,
  alt_allele.alt_allele_group_id,
  alt_allele_attrib.attrib = "IS_REPRESENTATIVE" AS alt_allele_is_representative,
  assembly_exception.exc_seq_region_id IS NULL AS primary_assembly,
  seq_region.name AS seq_region,
  alt_allele_attrib.attrib AS alt_allele_attrib,
  gene.created_date AS ensembl_created_date
FROM alt_allele
INNER JOIN gene
  ON gene.gene_id = alt_allele.gene_id
INNER JOIN alt_allele_attrib
  ON alt_allele.alt_allele_id = alt_allele_attrib.alt_allele_id
INNER JOIN seq_region
  ON gene.seq_region_id = seq_region.seq_region_id
LEFT JOIN assembly_exception
  ON seq_region.seq_region_id = assembly_exception.seq_region_id
  -- keep exc_type in (PATCH_FIX, PATCH_NOVEL, HAP)
  -- refs internal Related Sciences issue 606.
  AND NOT assembly_exception.exc_type <=> "PAR"
-- all genes were current when query was written, ensure this is always the case
WHERE gene.is_current
ORDER BY alt_allele_group_id, alt_allele_is_representative DESC, primary_assembly DESC, ensembl_created_date, ensembl_gene_id
-- LIMIT 5
