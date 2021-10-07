SELECT
  gene.stable_id AS ensembl_gene_id,
  external_db.db_name AS xref_source,
  xref.dbprimary_acc AS xref_accession,
  xref.display_label AS xref_label,
  xref.description AS xref_description,
  xref.info_type AS xref_info_type,
  object_xref.linkage_annotation AS xref_linkage_annotation
FROM gene
INNER JOIN object_xref
  ON gene.gene_id = object_xref.ensembl_id
  AND object_xref.ensembl_object_type = "Gene"
INNER JOIN xref
  ON xref.xref_id = object_xref.xref_id
INNER JOIN external_db
  ON xref.external_db_id = external_db.external_db_id
WHERE
  -- all genes were current when query was written, ensure this is always the case
  gene.is_current AND
  -- -- Refs internal Related Sciences issue 289
  gene.biotype != "LRG_gene"
ORDER BY ensembl_gene_id, xref_source, xref_accession
-- LIMIT 10
