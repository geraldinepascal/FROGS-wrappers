# v3.2.1 [DEV]

This release corresponds to the FROGS 3.2.1 release.

### Tools added:
  * DESeq2 preprocess : Compute differential abundancy analysis
  * DESeq2 visualization : Create table and plots to explore and illustrate the differential abundant OTUs
  * Filters has been splitted into to new tools : FROGS OTU Filters and FROGS Affiliations Filters. 
      * FROGS OTU Filters filters OTU on presence/absence, abundances and contamination as Filters did. For contamination research, user may now use a personnal multifasta contaminant reference.
      * FROGS Affiliation Filters delete OTU or mask affiliation that do not respect affiliation metrics criteria, or affiliated to undesirable (partial) taxon.
  * FROGS datamanager is now available to manage affiliation reference database (frogs_db.loc for affiliation_OTU tool) and hyper variable in length amplicon reference (HVL_db.loc for affiliation_postprocess tool) thanks to @davidchristiany.

### Contaminant database added
  * add Arabidopsis thaliana chroloroplast sequence 

### Modifications:

  * rename phix_db.loc in contaminant_db.loc

# v3.1 [2018-01-08]

This release corresponds to the FROGS 3.1.0 release.

* ### Tools added:

  - ITSx : tool available for selecting and trimming ITS sequences based on ITSx tool
  - Affiliation Postprocess : resolve ambiguities due to inclusiv ITS, and aggregated OTU based on 
    taxonomic affiliations

* ### Modifications:

  - use tool data table instead of simple loc files for filters, affiliation_OTU and affiliation_postprocess
  - Tree do no longer support Pynast alignment thanks to a template file

# v2.0.0  [2018-12-11]

  First package.

This release corresponds to the FROGS 2.0.0 release
