# v3.2.3+galaxy2 [2021-06]

This version still refers to FROGS_3.2.3 suit.

## Modifications:

with help of @lecorguille

* clean up xml code by using single quote, or python code following pep8 recommandations

* init macros for version, requirement, logo and help

* setup github actions for automatic galaxy testing 

* precise XML test sections

  

# v3.2.3.1 [2021-06]

This version still refers to FROGS_3.2.3 suit.

## Modifications:

* DESeq2 visualisation : correctly use the reference modality (in the tool conf pannel) as the expected modality2 in the deseq2_visualisation.py command line. Results were correct in the previous version but the reference condition was not the one precised by the user.

  

# v3.2.3 [2021-06]

## Modifications:

* Affiliation_OTU : add a taxonomic rank parameter to correctly take into account taxonomy not defined on commonly used 7 ranks.
* Update R and package dependencies to version 4.0.5 (because of trouble installing DESeq2 version 1.26).
* Rename OTU FIlter and Affiliation Filter output files.



# v3.2.2 [2021-04]

### Tools added:
  * DESeq2 preprocess : Compute differential abundancy analysis
  * DESeq2 visualisation : Create table and plots to explore and illustrate the differential abundant OTUs
  * Filters has been splitted into to new tools : FROGS OTU Filters and FROGS Affiliations Filters. 
      * FROGS OTU Filters filters OTU on presence/absence, abundances and contamination as Filters did. For contamination research, user may now use a personnal multifasta contaminant reference.
      * FROGS Affiliation Filters delete OTU or mask affiliation that do not respect affiliation metrics criteria, or affiliated to undesirable (partial) taxon.
  * FROGS datamanager is now available to manage affiliation reference database (frogs_db.loc for affiliation_OTU tool) thanks to @davidchristiany.

### Contaminant database added
  * add Arabidopsis thaliana chroloroplast sequence 

### Modifications:
  * ITSx : add organism model option scanning, change default behavior regarding the trimming of conserved regions

  * Use english typo for normalise and visualise

  * rename phix_db.loc in contaminant_db.loc

  * update tool dependencies version

    

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
