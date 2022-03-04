-- get Gene Ontology annotations for genes
-- GO xrefs in ensembl are linked to transcripts not genes.
-- Refs internal Related Sciences issue 316.
SELECT
  gene.stable_id AS ensembl_gene_id,
  -- external_db.db_name AS xref_source,
  xref.dbprimary_acc AS go_id,
  -- xref.display_label AS xref_label,
  xref.description AS go_label,
  GROUP_CONCAT(DISTINCT object_xref.linkage_annotation ORDER BY object_xref.linkage_annotation) AS go_evidence_codes,
  GROUP_CONCAT(DISTINCT xref.info_type ORDER BY xref.info_type) AS xref_info_types,
  GROUP_CONCAT(DISTINCT xref.info_text ORDER BY xref.info_text) AS xref_info_texts,
  GROUP_CONCAT(DISTINCT transcript.stable_id ORDER BY transcript.stable_id) AS ensembl_transcript_ids
FROM gene
INNER JOIN transcript 
  ON gene.gene_id = transcript.gene_id 
INNER JOIN object_xref 
  ON transcript.transcript_id = object_xref.ensembl_id 
  AND object_xref.ensembl_object_type = 'Transcript'
INNER JOIN xref 
  ON xref.xref_id = object_xref.xref_id
INNER JOIN external_db 
  ON xref.external_db_id = external_db.external_db_id 
  AND external_db.db_name = 'GO'
WHERE
  -- all genes were current when query was written, ensure this is always the case
  gene.is_current AND
  -- refs internal Related Sciences issue 289.
  gene.biotype != "LRG_gene"
GROUP BY gene.stable_id, external_db.db_name, xref.dbprimary_acc
ORDER BY ensembl_gene_id, go_id
-- LIMIT 10
