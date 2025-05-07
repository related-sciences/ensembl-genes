# output/rattus_norvegicus_core_114_1



- common name: rat
- species: rattus_norvegicus
- database: `rattus_norvegicus_core_114_1`
- release: 114
- assembly: 1
- export date: 2025-05-07T18:21:43.663065
- source commit: `f23429f80b7704bac6eab7b4b0c857b5168cc1ac
`
- created in action: <https://github.com/related-sciences/ensembl-genes/actions/runs/14890256280>



## Table heads

The first 10 rows of each exported table is shown below.


### genes

Primary table of ensembl genes with IDs, symbols, and genomic location information. Most users will want to filter this dataset to representative genes only by taking rows where `ensembl_gene_id == ensembl_representative_gene_id`.
Contains 43,360 rows.

| ensembl_gene_id    |   ensembl_gene_version | gene_symbol   | gene_symbol_source_db   |   gene_symbol_source_id | gene_biotype   | ensembl_source   | ensembl_created_date   | ensembl_modified_date   | coord_system_version   | coord_system     |   chromosome |   seq_region |   seq_region_start |   seq_region_end |   seq_region_strand | primary_assembly   | lrg_gene_id   | mhc   | gene_description                              | gene_description_source_db   |   gene_description_source_id | ensembl_representative_gene_id   |
|:-------------------|-----------------------:|:--------------|:------------------------|------------------------:|:---------------|:-----------------|:-----------------------|:------------------------|:-----------------------|:-----------------|-------------:|-------------:|-------------------:|-----------------:|--------------------:|:-------------------|:--------------|:------|:----------------------------------------------|:-----------------------------|-----------------------------:|:---------------------------------|
| ENSRNOG00000000001 |                      7 | Arsj          | RGD                     |                 1307640 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |            2 |            2 |          217449147 |        217529142 |                   1 | True               |               |       | arylsulfatase family, member J                | RGD Symbol                   |                      1307640 | ENSRNOG00000000001               |
| ENSRNOG00000000007 |                      9 | Gad1          | RGD                     |                    2652 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |            3 |            3 |           75777534 |         75818759 |                   1 | True               |               |       | glutamate decarboxylase 1                     | RGD Symbol                   |                         2652 | ENSRNOG00000000007               |
| ENSRNOG00000000008 |                      9 | Alx4          | RGD                     |                 1310201 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |            3 |            3 |          100067052 |        100103624 |                   1 | True               |               |       | ALX homeobox 4                                | RGD Symbol                   |                      1310201 | ENSRNOG00000000008               |
| ENSRNOG00000000009 |                      7 | Tmco5b        | RGD                     |                 1561237 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |            3 |            3 |          120519323 |        120537501 |                   1 | True               |               |       | transmembrane and coiled-coil domains 5B      | RGD Symbol                   |                      1561237 | ENSRNOG00000000009               |
| ENSRNOG00000000010 |                      7 | Cbln1         | RGD                     |                 1562813 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |           19 |           19 |           35781952 |         35785960 |                   1 | True               |               |       | cerebellin 1 precursor                        | RGD Symbol                   |                      1562813 | ENSRNOG00000000010               |
| ENSRNOG00000000012 |                      7 | Tcf15         | RGD                     |                 1308464 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |            3 |            3 |          161099301 |        161105083 |                   1 | True               |               |       | transcription factor 15                       | RGD Symbol                   |                      1308464 | ENSRNOG00000000012               |
| ENSRNOG00000000017 |                      9 | Steap1        | RGD                     |                 1311543 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |            4 |            4 |           29231753 |         29242317 |                   1 | True               |               |       | STEAP family member 1                         | RGD Symbol                   |                      1311543 | ENSRNOG00000000017               |
| ENSRNOG00000000024 |                      9 | Hebp1         | RGD                     |                 1304581 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |            4 |            4 |          169705668 |        169735199 |                  -1 | True               |               |       | heme binding protein 1                        | RGD Symbol                   |                      1304581 | ENSRNOG00000000024               |
| ENSRNOG00000000033 |                      7 | Tmcc2         | RGD                     |                 1311960 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |           13 |           13 |           46346177 |         46383862 |                  -1 | True               |               |       | transmembrane and coiled-coil domain family 2 | RGD Symbol                   |                      1311960 | ENSRNOG00000000033               |
| ENSRNOG00000000034 |                      8 | Nuak2         | RGD                     |                 1359167 | protein_coding | ensembl          | 2009-07-29 15:36:02    | 2024-05-09 12:20:34     | GRCr8                  | primary_assembly |           13 |           13 |           46305975 |         46322748 |                   1 | True               |               |       | NUAK family kinase 2                          | RGD Symbol                   |                      1359167 | ENSRNOG00000000034               |




### alt_alleles

This is an intermediate table that groups genes if they are alternate alleles of each other. A representative gene is selected from each group.
Contains 43,360 rows.

| rs_allele_group   | ensembl_gene_id    | gene_symbol    | ensembl_created_date   | seq_region   | primary_assembly   | alt_allele_group_id   | alt_allele_attrib   | alt_allele_is_representative   | ensembl_representative_gene_id   | is_representative_gene   |
|:------------------|:-------------------|:---------------|:-----------------------|:-------------|:-------------------|:----------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| 1700001K19Rikl    | ENSRNOG00000007184 | 1700001K19Rikl | 2009-07-29 15:36:02    | 6            | True               |                       |                     | False                          | ENSRNOG00000007184               | True                     |
| 1700006A11Rikl    | ENSRNOG00000024928 | 1700006A11Rikl | 2009-07-29 15:36:02    | 2            | True               |                       |                     | False                          | ENSRNOG00000024928               | True                     |
| 1700009N14Rikl    | ENSRNOG00000031013 | 1700009N14Rikl | 2005-03-02 00:00:00    | 5            | True               |                       |                     | False                          | ENSRNOG00000031013               | True                     |
| 1700012A03Rikl    | ENSRNOG00000027055 | 1700012A03Rikl | 2009-07-29 15:36:02    | 4            | True               |                       |                     | False                          | ENSRNOG00000027055               | True                     |
| 1700012B07Rkl     | ENSRNOG00000024233 | 1700012B07Rkl  | 2009-07-29 15:36:02    | 10           | True               |                       |                     | False                          | ENSRNOG00000024233               | True                     |
| 1700013D24Rik     | ENSRNOG00000042494 | 1700013D24Rik  | 2009-07-29 15:36:02    | 4            | True               |                       |                     | False                          | ENSRNOG00000042494               | True                     |
| 1700013G24Rikl    | ENSRNOG00000013566 | 1700013G24Rikl | 2009-07-29 15:36:02    | 5            | True               |                       |                     | False                          | ENSRNOG00000013566               | True                     |
| 1700020N01Rikl    | ENSRNOG00000059251 | 1700020N01Rikl | 2015-04-02 16:53:59    | 1            | True               |                       |                     | False                          | ENSRNOG00000059251               | True                     |
| 1700020N15Rikl    | ENSRNOG00000073787 | 1700020N15Rikl | 2024-05-09 12:20:34    | X            | True               |                       |                     | False                          | ENSRNOG00000073787               | True                     |
| 1700028J19Rikl    | ENSRNOG00000064179 | 1700028J19Rikl | 2021-02-26 12:35:27    | 1            | True               |                       |                     | False                          | ENSRNOG00000064179               | True                     |




### old_to_newest

This table maps outdated gene symbols to their newest gene symbol, traversing multiple levels of replacement if necessary. When `is_current` is False, then the newest replacement is not a current gene.
Contains 94,320 rows.

| old_ensembl_gene_id   | newest_ensembl_gene_id   | is_current   |
|:----------------------|:-------------------------|:-------------|
| ENSRNOG00000000132    | ENSRNOG00000031425       | True         |
| ENSRNOG00000000194    | ENSRNOG00000031589       | False        |
| ENSRNOG00000000194    | ENSRNOG00000045940       | False        |
| ENSRNOG00000000194    | ENSRNOG00000073140       | True         |
| ENSRNOG00000000194    | ENSRNOG00000073343       | True         |
| ENSRNOG00000000194    | ENSRNOG00000075209       | True         |
| ENSRNOG00000000194    | ENSRNOG00000075742       | True         |
| ENSRNOG00000000194    | ENSRNOG00000079834       | True         |
| ENSRNOG00000000194    | ENSRNOG00000081716       | True         |
| ENSRNOG00000000194    | ENSRNOG00000084448       | True         |




### updates

This dataset updates ensembl genes to current, representative ensembl genes. We refer to it as the 'omni-updater'. When ingesting external datasets that use Ensembl gene IDs, we recommend joining with this table. Current, representative genes map to themselves.
Contains 86,256 rows.

| input_ensembl_gene_id   | ensembl_gene_id    | input_current   | input_representative   |   input_maps_to_n_genes |   n_inputs_map_to_gene |
|:------------------------|:-------------------|:----------------|:-----------------------|------------------------:|-----------------------:|
| ENSRNOG00000000001      | ENSRNOG00000000001 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000007      | ENSRNOG00000000007 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000008      | ENSRNOG00000000008 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000009      | ENSRNOG00000000009 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000010      | ENSRNOG00000000010 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000012      | ENSRNOG00000000012 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000017      | ENSRNOG00000000017 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000024      | ENSRNOG00000000024 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000033      | ENSRNOG00000000033 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000034      | ENSRNOG00000000034 | True            | True                   |                       1 |                      1 |




### xrefs

This dataset contains cross-references (xrefs) from Ensembl genes to various external gene resources.
Contains 281,710 rows.

| ensembl_representative_gene_id   | ensembl_gene_id    | gene_symbol   | xref_source   | xref_accession     | xref_label         | xref_description                                                                 | xref_info_type   | xref_linkage_annotation   | xref_curie                      |
|:---------------------------------|:-------------------|:--------------|:--------------|:-------------------|:-------------------|:---------------------------------------------------------------------------------|:-----------------|:--------------------------|:--------------------------------|
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | ArrayExpress  | ENSRNOG00000000001 | ENSRNOG00000000001 | <NA>                                                                             | DIRECT           |                           | arrayexpress:ENSRNOG00000000001 |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | EntrezGene    | 311013             | Arsj               | arylsulfatase family, member J                                                   | DEPENDENT        |                           | ncbigene:311013                 |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | HGNC          | HGNC:26286         | ARSJ               | arylsulfatase family member J                                                    | NONE             |                           | hgnc:26286                      |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | RGD           | 1307640            | Arsj               | arylsulfatase family, member J                                                   | DIRECT           |                           | rgd:1307640                     |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | RGD           | 15003202           | AABR07013255.1     | <NA>                                                                             | DIRECT           |                           | rgd:15003202                    |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | Reactome_gene | R-RNO-1430728      | R-RNO-1430728      | Metabolism                                                                       | DIRECT           |                           | reactome:R-RNO-1430728          |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | Reactome_gene | R-RNO-163841       | R-RNO-163841       | Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation | DIRECT           |                           | reactome:R-RNO-163841           |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | Reactome_gene | R-RNO-1660662      | R-RNO-1660662      | Glycosphingolipid metabolism                                                     | DIRECT           |                           | reactome:R-RNO-1660662          |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | Reactome_gene | R-RNO-1663150      | R-RNO-1663150      | The activation of arylsulfatases                                                 | DIRECT           |                           | reactome:R-RNO-1663150          |
| ENSRNOG00000000001               | ENSRNOG00000000001 | Arsj          | Reactome_gene | R-RNO-392499       | R-RNO-392499       | Metabolism of proteins                                                           | DIRECT           |                           | reactome:R-RNO-392499           |




### xref_ncbigene

This dataset contains cross-references (xrefs) from Ensembl genes to NCBI (Entrez) genes.
Contains 22,527 rows.

| ensembl_representative_gene_id   |   ncbigene_id | gene_symbol   | ncbigene_symbol   |
|:---------------------------------|--------------:|:--------------|:------------------|
| ENSRNOG00000000001               |        311013 | Arsj          | Arsj              |
| ENSRNOG00000000007               |         24379 | Gad1          | Gad1              |
| ENSRNOG00000000008               |        296511 | Alx4          | Alx4              |
| ENSRNOG00000000009               |        366158 | Tmco5b        | Tmco5b            |
| ENSRNOG00000000010               |        498922 | Cbln1         | Cbln1             |
| ENSRNOG00000000012               |        296272 | Tcf15         | Tcf15             |
| ENSRNOG00000000017               |        297738 | Steap1        | Steap1            |
| ENSRNOG00000000024               |        362454 | Hebp1         | Hebp1             |
| ENSRNOG00000000033               |        305095 | Tmcc2         | Tmcc2             |
| ENSRNOG00000000034               |        289419 | Nuak2         | Nuak2             |




### xref_go

This dataset contains cross-references (xrefs) from Ensembl genes to Gene Ontology terms, as asserted by Gene Ontology annotations.
Contains 210,063 rows.

| ensembl_gene_id    | go_id      | go_label                                     | go_evidence_codes   | xref_info_types   | xref_info_texts                                                                                | ensembl_transcript_ids                                                                         | ensembl_representative_gene_id   |
|:-------------------|:-----------|:---------------------------------------------|:--------------------|:------------------|:-----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|:---------------------------------|
| ENSRNOG00000000001 | GO:0008484 | sulfuric ester hydrolase activity            | <NA>                | DEPENDENT         |                                                                                                | ENSRNOT00000055633                                                                             | ENSRNOG00000000001               |
| ENSRNOG00000000001 | GO:0015629 | actin cytoskeleton                           | IEA                 | PROJECTION        | from homo_sapiens translation ENSP00000320219                                                  | ENSRNOT00000055633                                                                             | ENSRNOG00000000001               |
| ENSRNOG00000000007 | GO:0004351 | glutamate decarboxylase activity             | IEA                 | PROJECTION        | from homo_sapiens translation ENSP00000350928,from mus_musculus translation ENSMUSP00000092539 | ENSRNOT00000087134                                                                             | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0005737 | cytoplasm                                    | IEA                 | PROJECTION        | from mus_musculus translation ENSMUSP00000092539                                               | ENSRNOT00000087134                                                                             | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0005938 | cell cortex                                  | IEA                 | PROJECTION        | from mus_musculus translation ENSMUSP00000092539                                               | ENSRNOT00000087134                                                                             | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0006538 | glutamate catabolic process                  | IEA                 | PROJECTION        | from homo_sapiens translation ENSP00000350928                                                  | ENSRNOT00000087134                                                                             | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0009449 | gamma-aminobutyric acid biosynthetic process | IEA                 | PROJECTION        | from homo_sapiens translation ENSP00000350928,from mus_musculus translation ENSMUSP00000092539 | ENSRNOT00000087134                                                                             | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0016830 | carbon-carbon lyase activity                 | <NA>                | DEPENDENT         |                                                                                                | ENSRNOT00000000008,ENSRNOT00000084375,ENSRNOT00000087134,ENSRNOT00000164935,ENSRNOT00000166434 | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0016831 | carboxy-lyase activity                       | <NA>                | DEPENDENT         |                                                                                                | ENSRNOT00000000008,ENSRNOT00000087134,ENSRNOT00000164935,ENSRNOT00000166434                    | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0019752 | carboxylic acid metabolic process            | <NA>                | DEPENDENT         |                                                                                                | ENSRNOT00000000008,ENSRNOT00000084375,ENSRNOT00000087134,ENSRNOT00000164935,ENSRNOT00000166434 | ENSRNOG00000000007               |


