# output/rattus_norvegicus_core_104_6



- common name: rat
- species: rattus_norvegicus
- database: `rattus_norvegicus_core_104_6`
- release: 104
- assembly: 6
- export date: 2021-10-15T02:34:40.046127
- source commit: `9738939452a679998591583f47ce0403bb4aea50
`
- created in action: <https://github.com/related-sciences/ensembl-genes/actions/runs/1344344511>



## Table heads

The first 10 rows of each exported table is shown below.


### genes

Primary table of ensembl genes with IDs, symbols, and genomic location information. Most users will want to filter this dataset to representative genes only, via the `is_representative_gene` column.

| ensembl_gene_id    |   ensembl_gene_version | gene_symbol    | gene_symbol_source_db    | gene_symbol_source   | gene_biotype   | gene_description                                                              | ensembl_source   | ensembl_created_date   | ensembl_modified_date   | coord_system_version   | coord_system   |   chromosome | seq_region_exc_type   |   seq_region |   seq_region_start |   seq_region_end |   seq_region_strand | primary_assembly   | lrg_gene_id   | mhc   | ensembl_representative_gene_id   |
|:-------------------|-----------------------:|:---------------|:-------------------------|:---------------------|:---------------|:------------------------------------------------------------------------------|:-----------------|:-----------------------|:------------------------|:-----------------------|:---------------|-------------:|:----------------------|-------------:|-------------------:|-----------------:|--------------------:|:-------------------|:--------------|:------|:---------------------------------|
| ENSRNOG00000000001 |                      5 | AABR07013255.1 | Clone_based_ensembl_gene | AABR07013255.1       | pseudogene     | <NA>                                                                          | ensembl          | 2009-07-29 15:36:02    | 2015-04-02 16:53:59     | Rnor_6.0               | chromosome     |            2 |                       |            2 |          230660664 |        230662084 |                   1 | True               |               |       | ENSRNOG00000000001               |
| ENSRNOG00000000007 |                      7 | Gad1           | RGD                      | 2652                 | protein_coding | glutamate decarboxylase 1 [Source:RGD Symbol;Acc:2652]                        | ensembl          | 2009-07-29 15:36:02    | 2015-04-02 16:53:59     | Rnor_6.0               | chromosome     |            3 |                       |            3 |           56861396 |         56902157 |                   1 | True               |               |       | ENSRNOG00000000007               |
| ENSRNOG00000000008 |                      7 | Alx4           | RGD                      | 1310201              | protein_coding | ALX homeobox 4 [Source:RGD Symbol;Acc:1310201]                                | ensembl          | 2009-07-29 15:36:02    | 2015-04-02 16:53:59     | Rnor_6.0               | chromosome     |            3 |                       |            3 |           82548959 |         82585531 |                   1 | True               |               |       | ENSRNOG00000000008               |
| ENSRNOG00000000009 |                      5 | Tmco5b         | RGD                      | 1561237              | protein_coding | transmembrane and coiled-coil domains 5B [Source:RGD Symbol;Acc:1561237]      | ensembl          | 2009-07-29 15:36:02    | 2015-04-02 16:53:59     | Rnor_6.0               | chromosome     |            3 |                       |            3 |          104749051 |        104765436 |                   1 | True               |               |       | ENSRNOG00000000009               |
| ENSRNOG00000000010 |                      5 | Cbln1          | RGD                      | 1562813              | protein_coding | cerebellin 1 precursor [Source:RGD Symbol;Acc:1562813]                        | ensembl          | 2009-07-29 15:36:02    | 2009-07-29 15:36:02     | Rnor_6.0               | chromosome     |           19 |                       |           19 |           20607507 |         20611316 |                   1 | True               |               |       | ENSRNOG00000000010               |
| ENSRNOG00000000012 |                      5 | Tcf15          | RGD                      | 1308464              | protein_coding | transcription factor 15 [Source:RGD Symbol;Acc:1308464]                       | ensembl          | 2009-07-29 15:36:02    | 2012-11-09 06:35:19     | Rnor_6.0               | chromosome     |            3 |                       |            3 |          147643250 |        147649504 |                   1 | True               |               |       | ENSRNOG00000000012               |
| ENSRNOG00000000017 |                      7 | Steap1         | RGD                      | 1311543              | protein_coding | STEAP family member 1 [Source:RGD Symbol;Acc:1311543]                         | ensembl          | 2009-07-29 15:36:02    | 2015-04-02 16:53:59     | Rnor_6.0               | chromosome     |            4 |                       |            4 |           25435873 |         25446461 |                   1 | True               |               |       | ENSRNOG00000000017               |
| ENSRNOG00000000021 |                      3 | AABR07061902.1 | Clone_based_ensembl_gene | AABR07061902.1       | pseudogene     | <NA>                                                                          | ensembl          | 2009-07-29 15:36:02    | 2012-11-09 06:35:19     | Rnor_6.0               | chromosome     |            4 |                       |            4 |          151987078 |        151988279 |                   1 | True               |               |       | ENSRNOG00000000021               |
| ENSRNOG00000000024 |                      7 | Hebp1          | RGD                      | 1304581              | protein_coding | heme binding protein 1 [Source:RGD Symbol;Acc:1304581]                        | ensembl          | 2009-07-29 15:36:02    | 2015-04-02 16:53:59     | Rnor_6.0               | chromosome     |            4 |                       |            4 |          168903565 |        168933079 |                  -1 | True               |               |       | ENSRNOG00000000024               |
| ENSRNOG00000000033 |                      5 | Tmcc2          | RGD                      | 1311960              | protein_coding | transmembrane and coiled-coil domain family 2 [Source:RGD Symbol;Acc:1311960] | ensembl          | 2009-07-29 15:36:02    | 2015-04-02 16:53:59     | Rnor_6.0               | chromosome     |           13 |                       |           13 |           49132667 |         49169918 |                  -1 | True               |               |       | ENSRNOG00000000033               |




### alt_alleles

This is an intermediate table that groups genes if they are alternate alleles of eachother. A representative gene is selected from each group.

| ensembl_gene_id   | alt_allele_group_id   | alt_allele_is_representative   | primary_assembly   | seq_region   | alt_allele_attrib   | ensembl_created_date   | ensembl_representative_gene_id   | is_representative_gene   | representative_gene_method   |
|-------------------|-----------------------|--------------------------------|--------------------|--------------|---------------------|------------------------|----------------------------------|--------------------------|------------------------------|




### old_to_newest

This table maps outdated gene symbols to their newest gene symbol, traversing multiple levels of replacement if necessary. When `is_current` is False, then the newest replacement is not a current gene.

| old_ensembl_gene_id   | newest_ensembl_gene_id   | is_current   |
|:----------------------|:-------------------------|:-------------|
| ENSRNOG00000000132    | ENSRNOG00000031425       | True         |
| ENSRNOG00000000194    | ENSRNOG00000031589       | False        |
| ENSRNOG00000000194    | ENSRNOG00000045932       | True         |
| ENSRNOG00000000194    | ENSRNOG00000045940       | True         |
| ENSRNOG00000000194    | ENSRNOG00000046072       | True         |
| ENSRNOG00000000194    | ENSRNOG00000046182       | True         |
| ENSRNOG00000000194    | ENSRNOG00000046425       | True         |
| ENSRNOG00000000194    | ENSRNOG00000047636       | True         |
| ENSRNOG00000000194    | ENSRNOG00000047749       | True         |
| ENSRNOG00000000194    | ENSRNOG00000048331       | True         |




### updates

This dataset updates ensembl genes to current, representative ensembl genes. We refer to it as the 'omni-updater'. When ingesting external datasets that use Ensembl gene IDs, we recommend joining with this table. Current, representative genes map to themselves.

| input_ensembl_gene_id   | ensembl_gene_id    | input_current   | input_representative   |   input_maps_to_n_genes |   n_inputs_map_to_gene |
|:------------------------|:-------------------|:----------------|:-----------------------|------------------------:|-----------------------:|
| ENSRNOG00000000001      | ENSRNOG00000000001 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000007      | ENSRNOG00000000007 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000008      | ENSRNOG00000000008 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000009      | ENSRNOG00000000009 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000010      | ENSRNOG00000000010 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000012      | ENSRNOG00000000012 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000017      | ENSRNOG00000000017 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000021      | ENSRNOG00000000021 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000024      | ENSRNOG00000000024 | True            | True                   |                       1 |                      1 |
| ENSRNOG00000000033      | ENSRNOG00000000033 | True            | True                   |                       1 |                      1 |




### xrefs

This dataset contains cross-references (xrefs) from Ensembl genes to various external gene resources.

| ensembl_gene_id    | xref_source              | xref_accession     | xref_label         | xref_description                                  | xref_info_type   | xref_linkage_annotation   |
|:-------------------|:-------------------------|:-------------------|:-------------------|:--------------------------------------------------|:-----------------|:--------------------------|
| ENSRNOG00000000001 | ArrayExpress             | ENSRNOG00000000001 | ENSRNOG00000000001 | <NA>                                              | DIRECT           |                           |
| ENSRNOG00000000001 | Clone_based_ensembl_gene | AABR07013255.1     | AABR07013255.1     | <NA>                                              | MISC             |                           |
| ENSRNOG00000000007 | ArrayExpress             | ENSRNOG00000000007 | ENSRNOG00000000007 | <NA>                                              | DIRECT           |                           |
| ENSRNOG00000000007 | EntrezGene               | 24379              | Gad1               | glutamate decarboxylase 1                         | DEPENDENT        |                           |
| ENSRNOG00000000007 | Reactome_gene            | R-RNO-112310       | R-RNO-112310       | Neurotransmitter release cycle                    | DIRECT           |                           |
| ENSRNOG00000000007 | Reactome_gene            | R-RNO-112315       | R-RNO-112315       | Transmission across Chemical Synapses             | DIRECT           |                           |
| ENSRNOG00000000007 | Reactome_gene            | R-RNO-112316       | R-RNO-112316       | Neuronal System                                   | DIRECT           |                           |
| ENSRNOG00000000007 | Reactome_gene            | R-RNO-888568       | R-RNO-888568       | GABA synthesis                                    | DIRECT           |                           |
| ENSRNOG00000000007 | Reactome_gene            | R-RNO-888590       | R-RNO-888590       | GABA synthesis, release, reuptake and degradation | DIRECT           |                           |
| ENSRNOG00000000007 | RGD                      | 2652               | Gad1               | glutamate decarboxylase 1                         | DIRECT           |                           |




### xref_ncbigene

This dataset contains cross-references (xrefs) from Ensembl genes to NCBI (Entrez) genes.

| ensembl_representative_gene_id   |   ncbigene_id |
|:---------------------------------|--------------:|
| ENSRNOG00000000007               |         24379 |
| ENSRNOG00000000008               |        296511 |
| ENSRNOG00000000009               |        366158 |
| ENSRNOG00000000010               |        498922 |
| ENSRNOG00000000012               |        296272 |
| ENSRNOG00000000017               |        297738 |
| ENSRNOG00000000024               |        362454 |
| ENSRNOG00000000033               |        305095 |
| ENSRNOG00000000034               |        289419 |
| ENSRNOG00000000035               |        689712 |




### xref_go

This dataset contains cross-references (xrefs) from Ensembl genes to Gene Ontology terms, as asserted by Gene Ontology annotations.

| ensembl_gene_id    | go_id      | go_label                                     | go_evidence_codes   | xref_info_types   | ensembl_transcript_ids                                                      | ensembl_representative_gene_id   |
|:-------------------|:-----------|:---------------------------------------------|:--------------------|:------------------|:----------------------------------------------------------------------------|:---------------------------------|
| ENSRNOG00000000007 | GO:0003824 | catalytic activity                           | IEA                 | DEPENDENT,DIRECT  | ENSRNOT00000000008,ENSRNOT00000087134,ENSRNOT00000087712                    | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0004351 | glutamate decarboxylase activity             | IEA,ISO,ISS         | PROJECTION,DIRECT | ENSRNOT00000000008,ENSRNOT00000084375,ENSRNOT00000087712                    | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0005737 | cytoplasm                                    | IEA,ISO             | PROJECTION,DIRECT | ENSRNOT00000000008,ENSRNOT00000087712                                       | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0005938 | cell cortex                                  | IEA,ISO             | PROJECTION,DIRECT | ENSRNOT00000000008,ENSRNOT00000087712                                       | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0009449 | gamma-aminobutyric acid biosynthetic process | IDA                 | DIRECT            | ENSRNOT00000000008,ENSRNOT00000087712                                       | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0016595 | glutamate binding                            | IDA                 | DIRECT            | ENSRNOT00000000008,ENSRNOT00000087712                                       | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0016829 | lyase activity                               | IEA                 | DIRECT            | ENSRNOT00000000008,ENSRNOT00000084375,ENSRNOT00000087134,ENSRNOT00000087712 | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0016831 | carboxy-lyase activity                       | IEA                 | DEPENDENT,DIRECT  | ENSRNOT00000000008,ENSRNOT00000084375,ENSRNOT00000087134,ENSRNOT00000087712 | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0019752 | carboxylic acid metabolic process            | IEA                 | DEPENDENT,DIRECT  | ENSRNOT00000000008,ENSRNOT00000084375,ENSRNOT00000087134,ENSRNOT00000087712 | ENSRNOG00000000007               |
| ENSRNOG00000000007 | GO:0030170 | pyridoxal phosphate binding                  | IDA,IEA             | DEPENDENT,DIRECT  | ENSRNOT00000000008,ENSRNOT00000084375,ENSRNOT00000087134,ENSRNOT00000087712 | ENSRNOG00000000007               |


