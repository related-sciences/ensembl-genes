SELECT
  gene.stable_id AS ensembl_gene_id,
  gene.version AS ensembl_gene_version,
  -- gene symbol methods https://github.com/cogent3/ensembldb3/issues/7
  -- Release 104 retired clone-based gene symbols,
  -- leading to ensembl genes without a symbol. Fill with the stable ID,
  -- as per https://www.ensembl.info/2021/03/15/retirement-of-clone-based-gene-names/
  COALESCE(xref.display_label, gene.stable_id) AS gene_symbol,
  external_db.db_name AS gene_symbol_source_db,
  xref.dbprimary_acc AS gene_symbol_source_id,
  gene.biotype AS gene_biotype,
  gene.description AS gene_description,
  gene.source AS ensembl_source,
  gene.created_date AS ensembl_created_date,
  gene.modified_date AS ensembl_modified_date,
  coord_system.version AS coord_system_version,
  coord_system.name AS coord_system,
  -- get chromosome: refs internal Related Sciences issue 606.
  CASE WHEN coord_system.name = "chromosome"
       THEN COALESCE(exc_seq_region.name, seq_region.name)
       END AS chromosome,
  assembly_exception.exc_type AS seq_region_exc_type,
  seq_region.name AS seq_region,
  gene.seq_region_start AS seq_region_start,
  gene.seq_region_end AS seq_region_end,
  gene.seq_region_strand AS seq_region_strand,
  assembly_exception.exc_seq_region_id IS NULL AS primary_assembly
FROM gene
LEFT JOIN xref ON xref.xref_id = gene.display_xref_id
LEFT JOIN external_db ON xref.external_db_id = external_db.external_db_id
LEFT JOIN seq_region ON gene.seq_region_id = seq_region.seq_region_id
LEFT JOIN coord_system ON seq_region.coord_system_id = coord_system.coord_system_id
LEFT JOIN assembly_exception ON seq_region.seq_region_id = assembly_exception.seq_region_id
  -- keep exc_type in (PATCH_FIX, PATCH_NOVEL, HAP)
  -- refs internal Related Sciences issue 606.
  AND NOT assembly_exception.exc_type <=> "PAR"
LEFT JOIN seq_region AS exc_seq_region ON assembly_exception.exc_seq_region_id = exc_seq_region.seq_region_id
WHERE
  -- all genes were current when query was written, ensure this is always the case
  gene.is_current AND
  -- refs internal Related Sciences issue 289.
  gene.biotype != "LRG_gene"
ORDER BY ensembl_gene_id
-- LIMIT 1000
