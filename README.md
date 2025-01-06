# output/mus_musculus_core_113_39



- common name: mouse
- species: mus_musculus
- database: `mus_musculus_core_113_39`
- release: 113
- assembly: 39
- export date: 2025-01-06T21:09:39.993315
- source commit: `d2ecc10a2484d783db01f9760ce669e7be8416eb
`
- created in action: <https://github.com/related-sciences/ensembl-genes/actions/runs/12640243149>



## Table heads

The first 10 rows of each exported table is shown below.


### genes

Primary table of ensembl genes with IDs, symbols, and genomic location information. Most users will want to filter this dataset to representative genes only by taking rows where `ensembl_gene_id == ensembl_representative_gene_id`.
Contains 78,298 rows.

| ensembl_gene_id    |   ensembl_gene_version | gene_symbol   | gene_symbol_source_db   | gene_symbol_source_id   | gene_biotype   | ensembl_source   | ensembl_created_date   | ensembl_modified_date   | coord_system_version   | coord_system   | chromosome   | seq_region   |   seq_region_start |   seq_region_end |   seq_region_strand | primary_assembly   | lrg_gene_id   | mhc   | gene_description                               | gene_description_source_db   | gene_description_source_id   | ensembl_representative_gene_id   |
|:-------------------|-----------------------:|:--------------|:------------------------|:------------------------|:---------------|:-----------------|:-----------------------|:------------------------|:-----------------------|:---------------|:-------------|:-------------|-------------------:|-----------------:|--------------------:|:-------------------|:--------------|:------|:-----------------------------------------------|:-----------------------------|:-----------------------------|:---------------------------------|
| ENSMUSG00000000001 |                      5 | Gnai3         | MGI                     | MGI:95773               | protein_coding | ensembl_havana   | 2004-11-18 15:05:57    | 2020-08-10 14:30:16     | GRCm39                 | chromosome     | 3            | 3            |          108014596 |        108053462 |                  -1 | True               |               |       | G protein subunit alpha i3                     | MGI Symbol                   | MGI:95773                    | ENSMUSG00000000001               |
| ENSMUSG00000000003 |                     16 | Pbsn          | MGI                     | MGI:1860484             | protein_coding | ensembl_havana   | 2006-06-28 13:29:12    | 2020-08-10 14:24:33     | GRCm39                 | chromosome     | X            | X            |           76881507 |         76897229 |                  -1 | True               |               |       | probasin                                       | MGI Symbol                   | MGI:1860484                  | ENSMUSG00000000003               |
| ENSMUSG00000000028 |                     16 | Cdc45         | MGI                     | MGI:1338073             | protein_coding | ensembl_havana   | 2007-06-26 09:54:29    | 2020-08-10 14:17:14     | GRCm39                 | chromosome     | 16           | 16           |           18599197 |         18630737 |                  -1 | True               |               |       | cell division cycle 45                         | MGI Symbol                   | MGI:1338073                  | ENSMUSG00000000028               |
| ENSMUSG00000000031 |                     20 | H19           | MGI                     | MGI:95891               | lncRNA         | ensembl_havana   | 2006-02-02 11:27:21    | 2024-05-06 19:10:14     | GRCm39                 | chromosome     | 7            | 7            |          142129262 |        142133957 |                  -1 | True               |               |       | H19, imprinted maternally expressed transcript | MGI Symbol                   | MGI:95891                    | ENSMUSG00000000031               |
| ENSMUSG00000000037 |                     18 | Scml2         | MGI                     | MGI:1340042             | protein_coding | ensembl_havana   | 2006-08-18 16:16:32    | 2020-08-10 14:22:47     | GRCm39                 | chromosome     | X            | X            |          159865521 |        160041209 |                   1 | True               |               |       | Scm polycomb group protein like 2              | MGI Symbol                   | MGI:1340042                  | ENSMUSG00000000037               |
| ENSMUSG00000000049 |                     12 | Apoh          | MGI                     | MGI:88058               | protein_coding | ensembl_havana   | 2004-07-23 17:00:05    | 2020-08-10 14:33:14     | GRCm39                 | chromosome     | 11           | 11           |          108234180 |        108305222 |                   1 | True               |               |       | apolipoprotein H                               | MGI Symbol                   | MGI:88058                    | ENSMUSG00000000049               |
| ENSMUSG00000000056 |                      8 | Narf          | MGI                     | MGI:1914858             | protein_coding | ensembl_havana   | 2004-08-24 16:51:12    | 2020-08-10 14:25:34     | GRCm39                 | chromosome     | 11           | 11           |          121128079 |        121146682 |                   1 | True               |               |       | nuclear prelamin A recognition factor          | MGI Symbol                   | MGI:1914858                  | ENSMUSG00000000056               |
| ENSMUSG00000000058 |                      7 | Cav2          | MGI                     | MGI:107571              | protein_coding | ensembl_havana   | 2007-03-22 17:53:51    | 2020-08-10 14:11:15     | GRCm39                 | chromosome     | 6            | 6            |           17281184 |         17289114 |                   1 | True               |               |       | caveolin 2                                     | MGI Symbol                   | MGI:107571                   | ENSMUSG00000000058               |
| ENSMUSG00000000078 |                      8 | Klf6          | MGI                     | MGI:1346318             | protein_coding | ensembl_havana   | 2016-11-15 10:19:54    | 2020-08-10 14:14:26     | GRCm39                 | chromosome     | 13           | 13           |            5911481 |          5920393 |                   1 | True               |               |       | Kruppel-like transcription factor 6            | MGI Symbol                   | MGI:1346318                  | ENSMUSG00000000078               |
| ENSMUSG00000000085 |                     17 | Scmh1         | MGI                     | MGI:1352762             | protein_coding | ensembl_havana   | 2005-02-25 17:38:45    | 2020-08-10 14:31:48     | GRCm39                 | chromosome     | 4            | 4            |          120262478 |        120387383 |                   1 | True               |               |       | sex comb on midleg homolog 1                   | MGI Symbol                   | MGI:1352762                  | ENSMUSG00000000085               |




### alt_alleles

This is an intermediate table that groups genes if they are alternate alleles of each other. A representative gene is selected from each group.
Contains 78,298 rows.

| rs_allele_group   | ensembl_gene_id    | gene_symbol   | ensembl_created_date   |   seq_region | primary_assembly   | alt_allele_group_id   | alt_allele_attrib   | alt_allele_is_representative   | ensembl_representative_gene_id   | is_representative_gene   |
|:------------------|:-------------------|:--------------|:-----------------------|-------------:|:-------------------|:----------------------|:--------------------|:-------------------------------|:---------------------------------|:-------------------------|
| 0610005C13Rik     | ENSMUSG00000109644 | 0610005C13Rik | 2007-12-11 14:58:31    |            7 | True               |                       |                     | False                          | ENSMUSG00000109644               | True                     |
| 0610006L08Rik     | ENSMUSG00000108652 | 0610006L08Rik | 2015-07-06 11:47:18    |            7 | True               |                       |                     | False                          | ENSMUSG00000108652               | True                     |
| 0610009E02Rik     | ENSMUSG00000086714 | 0610009E02Rik | 2005-06-29 11:35:32    |            2 | True               |                       |                     | False                          | ENSMUSG00000086714               | True                     |
| 0610009L18Rik     | ENSMUSG00000043644 | 0610009L18Rik | 2004-08-20 10:27:42    |           11 | True               |                       |                     | False                          | ENSMUSG00000043644               | True                     |
| 0610010K14Rik     | ENSMUSG00000020831 | 0610010K14Rik | 2003-12-09 12:39:50    |           11 | True               |                       |                     | False                          | ENSMUSG00000020831               | True                     |
| 0610012D04Rik     | ENSMUSG00000089755 | 0610012D04Rik | 2007-09-11 21:59:10    |           17 | True               |                       |                     | False                          | ENSMUSG00000089755               | True                     |
| 0610025J13Rik     | ENSMUSG00000046683 | 0610025J13Rik | 2005-02-14 17:10:21    |            4 | True               |                       |                     | False                          | ENSMUSG00000046683               | True                     |
| 0610030E20Rik     | ENSMUSG00000058706 | 0610030E20Rik | 2015-06-08 10:16:34    |            6 | True               |                       |                     | False                          | ENSMUSG00000058706               | True                     |
| 0610031O16Rik     | ENSMUSG00000099146 | 0610031O16Rik | 2013-07-02 16:06:07    |            3 | True               |                       |                     | False                          | ENSMUSG00000099146               | True                     |
| 0610033M10Rik     | ENSMUSG00000108236 | 0610033M10Rik | 2015-05-18 15:01:09    |            6 | True               |                       |                     | False                          | ENSMUSG00000108236               | True                     |




### old_to_newest

This table maps outdated gene symbols to their newest gene symbol, traversing multiple levels of replacement if necessary. When `is_current` is False, then the newest replacement is not a current gene.
Contains 71,734 rows.

| old_ensembl_gene_id   | newest_ensembl_gene_id   | is_current   |
|:----------------------|:-------------------------|:-------------|
| ENSMUSG00000000700    | ENSMUSG00000066358       | False        |
| ENSMUSG00000000700    | ENSMUSG00000068941       | False        |
| ENSMUSG00000001417    | ENSMUSG00000103766       | True         |
| ENSMUSG00000001417    | ENSMUSG00000104445       | True         |
| ENSMUSG00000001429    | ENSMUSG00000066108       | True         |
| ENSMUSG00000003673    | ENSMUSG00000071503       | False        |
| ENSMUSG00000003673    | ENSMUSG00000071837       | False        |
| ENSMUSG00000003676    | ENSMUSG00000071499       | False        |
| ENSMUSG00000003676    | ENSMUSG00000071841       | False        |
| ENSMUSG00000003678    | ENSMUSG00000071510       | True         |




### updates

This dataset updates ensembl genes to current, representative ensembl genes. We refer to it as the 'omni-updater'. When ingesting external datasets that use Ensembl gene IDs, we recommend joining with this table. Current, representative genes map to themselves.
Contains 137,189 rows.

| input_ensembl_gene_id   | ensembl_gene_id    | input_current   | input_representative   |   input_maps_to_n_genes |   n_inputs_map_to_gene |
|:------------------------|:-------------------|:----------------|:-----------------------|------------------------:|-----------------------:|
| ENSMUSG00000000001      | ENSMUSG00000000001 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000003      | ENSMUSG00000000003 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000028      | ENSMUSG00000000028 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000031      | ENSMUSG00000000031 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000037      | ENSMUSG00000000037 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000049      | ENSMUSG00000000049 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000056      | ENSMUSG00000000056 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000058      | ENSMUSG00000000058 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000078      | ENSMUSG00000000078 | True            | True                   |                       1 |                      1 |
| ENSMUSG00000000085      | ENSMUSG00000000085 | True            | True                   |                       1 |                      1 |




### xrefs

This dataset contains cross-references (xrefs) from Ensembl genes to various external gene resources.
Contains 335,057 rows.

| ensembl_representative_gene_id   | ensembl_gene_id    | gene_symbol   | xref_source   | xref_accession     | xref_label         | xref_description                                                | xref_info_type   | xref_linkage_annotation   | xref_curie                      |
|:---------------------------------|:-------------------|:--------------|:--------------|:-------------------|:-------------------|:----------------------------------------------------------------|:-----------------|:--------------------------|:--------------------------------|
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | ArrayExpress  | ENSMUSG00000000001 | ENSMUSG00000000001 | <NA>                                                            | DIRECT           |                           | arrayexpress:ENSMUSG00000000001 |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | EntrezGene    | 14679              | Gnai3              | G protein subunit alpha i3                                      | DEPENDENT        |                           | ncbigene:14679                  |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | MGI           | MGI:95773          | Gnai3              | G protein subunit alpha i3                                      | DIRECT           |                           | mgi:95773                       |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | Reactome_gene | R-MMU-109582       | R-MMU-109582       | Hemostasis                                                      | DIRECT           |                           | reactome:R-MMU-109582           |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | Reactome_gene | R-MMU-111885       | R-MMU-111885       | Opioid Signalling                                               | DIRECT           |                           | reactome:R-MMU-111885           |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | Reactome_gene | R-MMU-112040       | R-MMU-112040       | G-protein mediated events                                       | DIRECT           |                           | reactome:R-MMU-112040           |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | Reactome_gene | R-MMU-112314       | R-MMU-112314       | Neurotransmitter receptors and postsynaptic signal transmission | DIRECT           |                           | reactome:R-MMU-112314           |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | Reactome_gene | R-MMU-112315       | R-MMU-112315       | Transmission across Chemical Synapses                           | DIRECT           |                           | reactome:R-MMU-112315           |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | Reactome_gene | R-MMU-112316       | R-MMU-112316       | Neuronal System                                                 | DIRECT           |                           | reactome:R-MMU-112316           |
| ENSMUSG00000000001               | ENSMUSG00000000001 | Gnai3         | Reactome_gene | R-MMU-162582       | R-MMU-162582       | Signal Transduction                                             | DIRECT           |                           | reactome:R-MMU-162582           |




### xref_ncbigene

This dataset contains cross-references (xrefs) from Ensembl genes to NCBI (Entrez) genes.
Contains 28,204 rows.

| ensembl_representative_gene_id   |   ncbigene_id | gene_symbol   | ncbigene_symbol   |
|:---------------------------------|--------------:|:--------------|:------------------|
| ENSMUSG00000000001               |         14679 | Gnai3         | Gnai3             |
| ENSMUSG00000000003               |         54192 | Pbsn          | Pbsn              |
| ENSMUSG00000000028               |         12544 | Cdc45         | Cdc45             |
| ENSMUSG00000000031               |         14955 | H19           | H19               |
| ENSMUSG00000000037               |        107815 | Scml2         | Scml2             |
| ENSMUSG00000000049               |         11818 | Apoh          | Apoh              |
| ENSMUSG00000000056               |         67608 | Narf          | Narf              |
| ENSMUSG00000000058               |         12390 | Cav2          | Cav2              |
| ENSMUSG00000000078               |         23849 | Klf6          | Klf6              |
| ENSMUSG00000000085               |         29871 | Scmh1         | Scmh1             |




### xref_go

This dataset contains cross-references (xrefs) from Ensembl genes to Gene Ontology terms, as asserted by Gene Ontology annotations.
Contains 349,665 rows.

| ensembl_gene_id    | go_id      | go_label                           | go_evidence_codes   | xref_info_types             | xref_info_texts                                                                | ensembl_transcript_ids   | ensembl_representative_gene_id   |
|:-------------------|:-----------|:-----------------------------------|:--------------------|:----------------------------|:-------------------------------------------------------------------------------|:-------------------------|:---------------------------------|
| ENSMUSG00000000001 | GO:0000139 | Golgi membrane                     | IEA                 | PROJECTION                  | from homo_sapiens translation ENSP00000358867                                  | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0001664 | G protein-coupled receptor binding | IBA                 | DIRECT                      | GO_Central                                                                     | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0003924 | GTPase activity                    | IBA,IEA,ISS,TAS     | PROJECTION,DEPENDENT,DIRECT | ,from homo_sapiens translation ENSP00000358867,GO_Central,InterPro,MGI,UniProt | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0005515 | protein binding                    | IPI                 | DIRECT                      | IntAct,MGI                                                                     | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0005525 | GTP binding                        | IEA                 | DEPENDENT,DIRECT            | ,InterPro,UniProt                                                              | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0005654 | nucleoplasm                        | IEA                 | PROJECTION                  | from homo_sapiens translation ENSP00000358867                                  | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0005730 | nucleolus                          | IEA                 | PROJECTION                  | from homo_sapiens translation ENSP00000358867                                  | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0005737 | cytoplasm                          | IBA,IDA,IEA         | PROJECTION,DIRECT           | from homo_sapiens translation ENSP00000358867,GO_Central,MGI,UniProt           | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0005789 | endoplasmic reticulum membrane     | IEA                 | PROJECTION                  | from homo_sapiens translation ENSP00000358867                                  | ENSMUST00000000001       | ENSMUSG00000000001               |
| ENSMUSG00000000001 | GO:0005794 | Golgi apparatus                    | IDA                 | DIRECT                      | MGI                                                                            | ENSMUST00000000001       | ENSMUSG00000000001               |


