# output/homo_sapiens_core_112_38



- common name: human
- species: homo_sapiens
- database: `homo_sapiens_core_112_38`
- release: 112
- assembly: 38
- export date: 2024-05-20T20:19:28.722454
- source commit: `d2ecc10a2484d783db01f9760ce669e7be8416eb
`
- created in action: <https://github.com/related-sciences/ensembl-genes/actions/runs/9164353715>



## Table heads

The first 10 rows of each exported table is shown below.


### genes

Primary table of ensembl genes with IDs, symbols, and genomic location information. Most users will want to filter this dataset to representative genes only by taking rows where `ensembl_gene_id == ensembl_representative_gene_id`.
Contains 70,611 rows.

| ensembl_gene_id   |   ensembl_gene_version | gene_symbol   | gene_symbol_source_db   | gene_symbol_source_id   | gene_biotype   | ensembl_source   | ensembl_created_date   | ensembl_modified_date   | coord_system_version   | coord_system   | chromosome   | seq_region   |   seq_region_start |   seq_region_end |   seq_region_strand | primary_assembly   | lrg_gene_id   | mhc   | gene_description                                            | gene_description_source_db   | gene_description_source_id   | ensembl_representative_gene_id   |
|:------------------|-----------------------:|:--------------|:------------------------|:------------------------|:---------------|:-----------------|:-----------------------|:------------------------|:-----------------------|:---------------|:-------------|:-------------|-------------------:|-----------------:|--------------------:|:-------------------|:--------------|:------|:------------------------------------------------------------|:-----------------------------|:-----------------------------|:---------------------------------|
| ENSG00000000003   |                     16 | TSPAN6        | HGNC                    | HGNC:11858              | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2022-12-27 00:10:08     | GRCh38                 | chromosome     | X            | X            |          100627108 |        100639991 |                  -1 | True               | <NA>          | no    | tetraspanin 6                                               | HGNC Symbol                  | HGNC:11858                   | ENSG00000000003                  |
| ENSG00000000005   |                      6 | TNMD          | HGNC                    | HGNC:17757              | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2018-11-21 17:23:49     | GRCh38                 | chromosome     | X            | X            |          100584936 |        100599885 |                   1 | True               | <NA>          | no    | tenomodulin                                                 | HGNC Symbol                  | HGNC:17757                   | ENSG00000000005                  |
| ENSG00000000419   |                     14 | DPM1          | HGNC                    | HGNC:3005               | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2020-12-11 08:28:43     | GRCh38                 | chromosome     | 20           | 20           |           50934867 |         50959140 |                  -1 | True               | <NA>          | no    | dolichyl-phosphate mannosyltransferase subunit 1, catalytic | HGNC Symbol                  | HGNC:3005                    | ENSG00000000419                  |
| ENSG00000000457   |                     14 | SCYL3         | HGNC                    | HGNC:19285              | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2018-11-21 17:23:49     | GRCh38                 | chromosome     | 1            | 1            |          169849631 |        169894267 |                  -1 | True               | <NA>          | no    | SCY1 like pseudokinase 3                                    | HGNC Symbol                  | HGNC:19285                   | ENSG00000000457                  |
| ENSG00000000460   |                     17 | FIRRM         | HGNC                    | HGNC:25565              | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2018-11-21 17:23:49     | GRCh38                 | chromosome     | 1            | 1            |          169662007 |        169854080 |                   1 | True               | <NA>          | no    | FIGNL1 interacting regulator of recombination and mitosis   | HGNC Symbol                  | HGNC:25565                   | ENSG00000000460                  |
| ENSG00000000938   |                     13 | FGR           | HGNC                    | HGNC:3697               | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2018-11-21 17:23:49     | GRCh38                 | chromosome     | 1            | 1            |           27612064 |         27635185 |                  -1 | True               | <NA>          | no    | FGR proto-oncogene, Src family tyrosine kinase              | HGNC Symbol                  | HGNC:3697                    | ENSG00000000938                  |
| ENSG00000000971   |                     17 | CFH           | HGNC                    | HGNC:4883               | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2021-09-14 13:12:43     | GRCh38                 | chromosome     | 1            | 1            |          196651754 |        196752476 |                   1 | True               | LRG_47        | no    | complement factor H                                         | HGNC Symbol                  | HGNC:4883                    | ENSG00000000971                  |
| ENSG00000001036   |                     14 | FUCA2         | HGNC                    | HGNC:4008               | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2019-06-15 05:41:31     | GRCh38                 | chromosome     | 6            | 6            |          143494812 |        143511720 |                  -1 | True               | <NA>          | no    | alpha-L-fucosidase 2                                        | HGNC Symbol                  | HGNC:4008                    | ENSG00000001036                  |
| ENSG00000001084   |                     13 | GCLC          | HGNC                    | HGNC:4311               | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2019-03-13 17:05:15     | GRCh38                 | chromosome     | 6            | 6            |           53497341 |         53616970 |                  -1 | True               | LRG_1166      | no    | glutamate-cysteine ligase catalytic subunit                 | HGNC Symbol                  | HGNC:4311                    | ENSG00000001084                  |
| ENSG00000001167   |                     15 | NFYA          | HGNC                    | HGNC:7804               | protein_coding | ensembl_havana   | 2008-04-29 11:17:41    | 2020-12-11 08:28:43     | GRCh38                 | chromosome     | 6            | 6            |           41072974 |         41102403 |                   1 | True               | <NA>          | no    | nuclear transcription factor Y subunit alpha                | HGNC Symbol                  | HGNC:7804                    | ENSG00000001167                  |




### alt_alleles

This is an intermediate table that groups genes if they are alternate alleles of each other. A representative gene is selected from each group.
Contains 71,935 rows.

|   rs_allele_group | ensembl_gene_id   | gene_symbol   | ensembl_created_date   | seq_region    | primary_assembly   |   alt_allele_group_id | alt_allele_attrib      | alt_allele_is_representative   | ensembl_representative_gene_id   | is_representative_gene   |
|------------------:|:------------------|:--------------|:-----------------------|:--------------|:-------------------|----------------------:|:-----------------------|:-------------------------------|:---------------------------------|:-------------------------|
|             44430 | ENSG00000273644   | <NA>          | 2014-06-09 10:49:07    | 7             | True               |                 44430 | IS_REPRESENTATIVE      | True                           | ENSG00000273644                  | True                     |
|             44430 | ENSG00000282333   | <NA>          | 2015-06-01 18:57:05    | HSCHR7_2_CTG1 | False              |                 44430 | AUTOMATICALLY_ASSIGNED | False                          | ENSG00000273644                  | False                    |
|             44431 | ENSG00000232325   | <NA>          | 2009-05-19 09:47:17    | 7             | True               |                 44431 | IS_REPRESENTATIVE      | True                           | ENSG00000232325                  | True                     |
|             44431 | ENSG00000281993   | <NA>          | 2015-06-01 18:57:05    | HSCHR7_1_CTG1 | False              |                 44431 | AUTOMATICALLY_ASSIGNED | False                          | ENSG00000232325                  | False                    |
|             44431 | ENSG00000282645   | <NA>          | 2015-06-01 18:57:05    | HSCHR7_2_CTG1 | False              |                 44431 | AUTOMATICALLY_ASSIGNED | False                          | ENSG00000232325                  | False                    |
|             44431 | ENSG00000288372   | <NA>          | 2019-06-15 05:41:31    | HG1309_PATCH  | False              |                 44431 | AUTOMATICALLY_ASSIGNED | False                          | ENSG00000232325                  | False                    |
|             44432 | ENSG00000242611   | <NA>          | 2009-08-05 14:27:16    | 7             | True               |                 44432 | IS_REPRESENTATIVE      | True                           | ENSG00000242611                  | True                     |
|             44432 | ENSG00000282155   | <NA>          | 2015-06-01 18:57:05    | HSCHR7_1_CTG1 | False              |                 44432 | AUTOMATICALLY_ASSIGNED | False                          | ENSG00000242611                  | False                    |
|             44432 | ENSG00000282557   | <NA>          | 2015-06-01 18:57:05    | HSCHR7_2_CTG1 | False              |                 44432 | AUTOMATICALLY_ASSIGNED | False                          | ENSG00000242611                  | False                    |
|             44432 | ENSG00000288288   | <NA>          | 2019-06-15 05:41:31    | HG1309_PATCH  | False              |                 44432 | AUTOMATICALLY_ASSIGNED | False                          | ENSG00000242611                  | False                    |




### old_to_newest

This table maps outdated gene symbols to their newest gene symbol, traversing multiple levels of replacement if necessary. When `is_current` is False, then the newest replacement is not a current gene.
Contains 19,493 rows.

| old_ensembl_gene_id   | newest_ensembl_gene_id   | is_current   |
|:----------------------|:-------------------------|:-------------|
| ASMPATCHG00000000170  | ENSG00000256229          | True         |
| ASMPATCHG00000000174  | ENSG00000188171          | True         |
| ASMPATCHG00000000175  | ENSG00000237440          | True         |
| ASMPATCHG00000000190  | ENSG00000263181          | True         |
| ASMPATCHG00000000202  | ENSG00000262684          | False        |
| ASMPATCHG00000000222  | ENSG00000262907          | False        |
| ASMPATCHG00000000241  | ENSG00000264490          | True         |
| ASMPATCHG00000000243  | ENSG00000262549          | False        |
| ASMPATCHG00000000255  | ENSG00000262607          | True         |
| ASMPATCHG00000000258  | ENSG00000262349          | True         |




### updates

This dataset updates ensembl genes to current, representative ensembl genes. We refer to it as the 'omni-updater'. When ingesting external datasets that use Ensembl gene IDs, we recommend joining with this table. Current, representative genes map to themselves.
Contains 79,226 rows.

| input_ensembl_gene_id   | ensembl_gene_id   | input_current   | input_representative   |   input_maps_to_n_genes |   n_inputs_map_to_gene |
|:------------------------|:------------------|:----------------|:-----------------------|------------------------:|-----------------------:|
| ASMPATCHG00000000170    | ENSG00000256229   | False           | True                   |                       1 |                      3 |
| ASMPATCHG00000000174    | ENSG00000188171   | False           | True                   |                       1 |                      3 |
| ASMPATCHG00000000175    | ENSG00000237440   | False           | True                   |                       1 |                      3 |
| ASMPATCHG00000000190    | ENSG00000205702   | False           | False                  |                       1 |                      5 |
| ASMPATCHG00000000241    | ENSG00000264490   | False           | True                   |                       1 |                      3 |
| ASMPATCHG00000000255    | ENSG00000120645   | False           | False                  |                       1 |                      4 |
| ASMPATCHG00000000258    | ENSG00000257698   | False           | False                  |                       1 |                      3 |
| ASMPATCHG00000000268    | ENSG00000006530   | False           | False                  |                       1 |                      3 |
| ASMPATCHG00000000277    | ENSG00000256694   | False           | False                  |                       1 |                      4 |
| ASMPATCHG00000000281    | ENSG00000150261   | False           | False                  |                       1 |                      4 |




### xrefs

This dataset contains cross-references (xrefs) from Ensembl genes to various external gene resources.
Contains 508,584 rows.

| ensembl_representative_gene_id   | ensembl_gene_id   | gene_symbol   | xref_source   | xref_accession   | xref_label                      | xref_description                                                     | xref_info_type   | xref_linkage_annotation   | xref_curie                   |
|:---------------------------------|:------------------|:--------------|:--------------|:-----------------|:--------------------------------|:---------------------------------------------------------------------|:-----------------|:--------------------------|:-----------------------------|
| ENSG00000000003                  | ENSG00000000003   | TSPAN6        | ArrayExpress  | ENSG00000000003  | ENSG00000000003                 | <NA>                                                                 | DIRECT           |                           | arrayexpress:ENSG00000000003 |
| ENSG00000000003                  | ENSG00000000003   | TSPAN6        | EntrezGene    | 7105             | TSPAN6                          | tetraspanin 6                                                        | DEPENDENT        |                           | ncbigene:7105                |
| ENSG00000000003                  | ENSG00000000003   | TSPAN6        | GeneCards     | 11858            | TSPAN6                          | tetraspanin 6                                                        | DEPENDENT        |                           | genecards:11858              |
| ENSG00000000003                  | ENSG00000000003   | TSPAN6        | HGNC          | HGNC:11858       | TSPAN6                          | tetraspanin 6                                                        | DIRECT           |                           | hgnc:11858                   |
| ENSG00000000003                  | ENSG00000000003   | TSPAN6        | MIM_GENE      | 300191           | TETRASPANIN 6; TSPAN6 [*300191] | TETRASPANIN 6; TSPAN6;;TRANSMEMBRANE 4 SUPERFAMILY, MEMBER 6; TM4SF6 | DEPENDENT        |                           | omim:300191                  |
| ENSG00000000003                  | ENSG00000000003   | TSPAN6        | Uniprot_gn    | A0A087WYV6       | TSPAN6                          | <NA>                                                                 | DEPENDENT        |                           | uniprot:A0A087WYV6           |
| ENSG00000000003                  | ENSG00000000003   | TSPAN6        | Uniprot_gn    | O43657           | TSPAN6                          | <NA>                                                                 | DEPENDENT        |                           | uniprot:O43657               |
| ENSG00000000003                  | ENSG00000000003   | TSPAN6        | WikiGene      | 7105             | TSPAN6                          | tetraspanin 6                                                        | DEPENDENT        |                           | wikigenes:7105               |
| ENSG00000000005                  | ENSG00000000005   | TNMD          | ArrayExpress  | ENSG00000000005  | ENSG00000000005                 | <NA>                                                                 | DIRECT           |                           | arrayexpress:ENSG00000000005 |
| ENSG00000000005                  | ENSG00000000005   | TNMD          | EntrezGene    | 64102            | TNMD                            | tenomodulin                                                          | DEPENDENT        |                           | ncbigene:64102               |




### xref_ncbigene

This dataset contains cross-references (xrefs) from Ensembl genes to NCBI (Entrez) genes.
Contains 26,899 rows.

| ensembl_representative_gene_id   |   ncbigene_id | gene_symbol   | ncbigene_symbol   |
|:---------------------------------|--------------:|:--------------|:------------------|
| ENSG00000000003                  |          7105 | TSPAN6        | TSPAN6            |
| ENSG00000000005                  |         64102 | TNMD          | TNMD              |
| ENSG00000000419                  |          8813 | DPM1          | DPM1              |
| ENSG00000000457                  |         57147 | SCYL3         | SCYL3             |
| ENSG00000000460                  |         55732 | FIRRM         | FIRRM             |
| ENSG00000000938                  |          2268 | FGR           | FGR               |
| ENSG00000000971                  |          3075 | CFH           | CFH               |
| ENSG00000001036                  |          2519 | FUCA2         | FUCA2             |
| ENSG00000001084                  |          2729 | GCLC          | GCLC              |
| ENSG00000001167                  |          4800 | NFYA          | NFYA              |




### xref_go

This dataset contains cross-references (xrefs) from Ensembl genes to Gene Ontology terms, as asserted by Gene Ontology annotations.
Contains 398,544 rows.

| ensembl_gene_id   | go_id      | go_label                                                                                        | go_evidence_codes   | xref_info_types   | xref_info_texts                                             | ensembl_transcript_ids          | ensembl_representative_gene_id   |
|:------------------|:-----------|:------------------------------------------------------------------------------------------------|:--------------------|:------------------|:------------------------------------------------------------|:--------------------------------|:---------------------------------|
| ENSG00000000003   | GO:0005515 | protein binding                                                                                 | IPI                 | DIRECT            | UniProt                                                     | ENST00000373020                 | ENSG00000000003                  |
| ENSG00000000003   | GO:0016020 | membrane                                                                                        | IEA                 | DEPENDENT,DIRECT  | ,InterPro,UniProt                                           | ENST00000373020,ENST00000612152 | ENSG00000000003                  |
| ENSG00000000003   | GO:0039532 | negative regulation of viral-induced cytoplasmic pattern recognition receptor signaling pathway | IMP                 | DIRECT            | UniProt                                                     | ENST00000373020                 | ENSG00000000003                  |
| ENSG00000000003   | GO:0043123 | positive regulation of I-kappaB kinase/NF-kappaB signaling                                      | HMP                 | DIRECT            | UniProt                                                     | ENST00000373020                 | ENSG00000000003                  |
| ENSG00000000003   | GO:0043124 | negative regulation of I-kappaB kinase/NF-kappaB signaling                                      | IDA                 | DIRECT            | UniProt                                                     | ENST00000373020                 | ENSG00000000003                  |
| ENSG00000000003   | GO:0070062 | extracellular exosome                                                                           | HDA                 | DIRECT            | UniProt                                                     | ENST00000373020                 | ENSG00000000003                  |
| ENSG00000000005   | GO:0001886 | endothelial cell morphogenesis                                                                  | IEA                 | PROJECTION        | from mus_musculus translation ENSMUSP00000033602            | ENST00000373031                 | ENSG00000000005                  |
| ENSG00000000005   | GO:0001937 | negative regulation of endothelial cell proliferation                                           | IBA,IEA             | PROJECTION,DIRECT | from mus_musculus translation ENSMUSP00000033602,GO_Central | ENST00000373031                 | ENSG00000000005                  |
| ENSG00000000005   | GO:0005515 | protein binding                                                                                 | IPI                 | DIRECT            | IntAct                                                      | ENST00000373031                 | ENSG00000000005                  |
| ENSG00000000005   | GO:0005634 | nucleus                                                                                         | IEA                 | DIRECT            | UniProt                                                     | ENST00000373031                 | ENSG00000000005                  |


