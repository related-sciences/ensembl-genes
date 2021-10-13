SELECT
  old_stable_id AS old_ensembl_gene_id,
  new_stable_id AS new_ensembl_gene_id
FROM stable_id_event
WHERE
  NOT (old_stable_id IS NULL OR new_stable_id IS NULL)
  AND type="gene"
  AND old_stable_id != new_stable_id
