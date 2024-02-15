-- Get alt allele groups: genes with multiple alleles.
-- Includes all genes, even if they are in a group of only themselves.
-- Use gene symbols to group genes, because the alt_allele table alone is incomplete.
-- https://github.com/related-sciences/ensembl-genes/issues/9.
SELECT
  COALESCE(
    xref.display_label,
    CAST(alt_allele_group_id AS CHAR),
    gene.stable_id
  ) AS rs_allele_group,
  gene.stable_id AS ensembl_gene_id,
  xref.display_label AS gene_symbol,
  gene.created_date AS ensembl_created_date,
  seq_region.name AS seq_region,
  -- we used to use assembly_exception to determine primary assembly, but this table is now empty
  -- https://github.com/related-sciences/ensembl-genes/issues/22#issuecomment-1664197773
  -- instead just look for a short seq_region name (e.g. '19' instead of 'HSCHR19LRC_PGF1_CTG3_1'),
  -- even though this is a flawed method that would miss scaffolds that are primary assemblies.
  LENGTH(seq_region.name) <= 3 AS primary_assembly,
  alt_allele.alt_allele_group_id AS alt_allele_group_id,
  -- WARNING: alt_allele_attrib can introduce multiple rows per gene!
  alt_allele_attrib.attrib AS alt_allele_attrib,
  IFNULL(alt_allele_attrib.attrib = "IS_REPRESENTATIVE", FALSE) AS alt_allele_is_representative
FROM gene
LEFT JOIN seq_region USING (seq_region_id)
LEFT JOIN xref ON xref.xref_id = gene.display_xref_id
LEFT JOIN alt_allele USING (gene_id)
LEFT JOIN alt_allele_attrib USING (alt_allele_id)
WHERE gene.is_current
ORDER BY rs_allele_group, alt_allele_is_representative DESC, primary_assembly DESC, ensembl_created_date, ensembl_gene_id

-- it would be nice to identify the representative gene from a group in this query,
-- but window functions like the following are not supported:
-- ROW_NUMBER() OVER (
--   PARTITION BY rs_allele_group
--   ORDER BY
--     alt_allele_is_representative DESC NULLS LAST,
--     primary_assembly DESC NULLS LAST,
--     ensembl_created_date ASC NULLS LAST,
--     ensembl_gene_id ASC NULLS LAST
-- ) AS representative_gene_rank
