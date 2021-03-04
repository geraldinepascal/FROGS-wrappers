					<img src="static/images/FROGS_logo.png" width="20%" style="display: block; margin: auto;"/>					<img src="galaxy_project_logo_square.png" width="20%" style="display: block; margin: auto;"/> 



Visit our web site : http://frogs.toulouse.inra.fr/

[![Release](https://img.shields.io/badge/release-3.2.1-blue.svg)![Date](https://img.shields.io/badge/date-March%202021-red.svg)](https://github.com/geraldinepascal/FROGS-wrappers/releases)[<img src="https://www.podcastscience.fm/wp-content/uploads/2017/12/deezer.png" width="5%" style="display: block; margin: auto;"/>](https://www.deezer.com/fr/playlist/5233843102?utm_source=deezer&utm_content=playlist-5233843102&utm_term=18632989_1545296531&utm_medium=web)



# Description

FROGS is a workflow designed to produce an OTU count matrix from high depth sequencing amplicon data.

FROGS also provide statistical tools to explore OTU count table and taxonomical affiliations.

FROGS-wrappers allow to add FROGS on a Galaxy instance.

# Table of content

* [Installing FROGS\-wrappers](#installing-frogs-wrappers)
  * [Simplest way](#simplest-way)
  * [From sources](#from-sources)
      * [Prerequisites](#prerequisites)
      * [FROGS\-wrappers installation](#frogs-wrappers-installation)
* [Use PEAR as reads merge software in preprocess](#use-pear-as-reads-merge-software-in-preprocess)
* [Upload and configure the databanks](#upload-and-configure-the-databanks)
* [Galaxy configuration](#galaxy-configuration)
  * [Setup Galaxy environment variables](#setup-galaxy-environment-variables)
  * [Install python packages inside virtual env](#install-python-packages-inside-virtual-env)
  * [Avoid FROGS HTML report sanitization](#avoid-FROGS-HTML-report-sanitization)
  * [Set memory and parallelisation settings](#set-memory-and-parallelisation-settings)
* [License](#license)
* [Copyright](#copyright)
* [Citation](#citation)
* [Contact](#contact)

# Installing FROGS-wrappers

## Simplest way

FROGS is available on the Toolshed.

It will install FROGS thanks to [conda](https://anaconda.org/bioconda/frogs), download all these XML tools and well configure them in your Galaxy.

The 25 FROGS tools will be in random order in your tools panel. We propose to control that order by modifying the `shed_tool_conf.xml`  which will render the following`integrated_tool_panel.xml ` file. 

We suppose that you installed FROGS in a specific section named `FROGS`. 

```
<section id="FROGS" name="FROGS" version="">

    <label id="FROGS_OTU_toolshed_3.2.1" text="OTUs reconstruction" version="" />

    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_demultiplex/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_preprocess/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_clustering/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_remove_chimera/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_OTU_filters/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_itsx/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_affiliation_OTU/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_affiliation_filters/3.2.1" />    
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_affiliation_postprocess/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_normalisation/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_Tree/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_clusters_stat/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_affiliations_stat/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_biom_to_stdBiom/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_biom_to_tsv/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_tsv_to_biom/3.2.1" />

    <label id="FROGSSTAT_Phyloseq_toolshed_3.2.1" text="OTUs structure and composition analysis" version="" />
    
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Import_Data/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Composition_Visualisation/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Alpha_Diversity/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Beta_Diversity/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Sample_Clustering/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Structure_Visualisation/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Multivariate_Analysis_Of_Variance/3.2.1" />
    
    <label id="FROGSSTAT_DESeq_toolshed_3.2.1" text="Differential abundance analysis" version="" />
    
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_DESeq2_Preprocess/3.2.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_DESeq2_Visualization/3.2.1" />
</section>
```



## From sources

#### Prerequisites

You should start by installing [FROGS](https://github.com/geraldinepascal/FROGS) (remember, FROGS is now installable via conda ).

#### FROGS-wrappers installation

1.    <u>Download wrapper</u>

   Download the last released versions of FROGS-wrappers: https://github.com/geraldinepascal/FROGS-wrappers/releases

   Uncompress and unarchive the release in your ` <Galaxy_Dir>/tools` directory

   (replace the) link to the new directory like this

   ` ln -s <Galaxy_Dir>/tools/FROGS-wrappers-<Release_Number>  <Galaxy_Dir>/tools/FROGS`

2. <u>Add tools in galaxy</u>

   Add the tools in `<Galaxy_Dir>/config/tool_conf.xml`

   ```
     <section id="frogs_local" name="FROGS local">
       <label id="frogs_otu_construction" text="OTUs reconstruction" />
       <tool file="FROGS/demultiplex.xml" />
       <tool file="FROGS/preprocess.xml" />
       <tool file="FROGS/clustering.xml" />
       <tool file="FROGS/remove_chimera.xml" />
       <tool file="FROGS/otu_filters.xml" />
       <tool file="FROGS/itsx.xml" />
       <tool file="FROGS/affiliation_OTU.xml" />
       <tool file="FROGS/affiliation_filters.xml" />
       <tool file="FROGS/affiliation_postprocess.xml" />
       <tool file="FROGS/normalisation.xml" />
       <tool file="FROGS/tree.xml" />
       <tool file="FROGS/clusters_stat.xml" />
       <tool file="FROGS/affiliations_stat.xml" />
       <tool file="FROGS/biom_to_stdBiom.xml" />
       <tool file="FROGS/biom_to_tsv.xml" />
       <tool file="FROGS/tsv_to_biom.xml" />
       <label id="frogsstat_phyloseq" text="OTUs structure and composition analysis" />
       <tool file="FROGS/phyloseq_import_data.xml" />
       <tool file="FROGS/phyloseq_composition.xml" />
       <tool file="FROGS/phyloseq_alpha_diversity.xml" />
       <tool file="FROGS/phyloseq_beta_diversity.xml" />
       <tool file="FROGS/phyloseq_clustering.xml" />
       <tool file="FROGS/phyloseq_structure.xml" />
       <tool file="FROGS/phyloseq_manova.xml" />
       <label id="frogsstat_deseq" text="Differential abundance analysis" />
       <tool file="FROGS/deseq2_preprocess.xml" />
       <tool file="FROGS/deseq2_visualization.xml" />
     </section>     
   ```
   NB: If you used previous version of FROGS (<3.1), you must removed `app` direcotry name in the paths names. 

3. <u> Correct tools order</u>

Tools order in the Galaxy interface will not follow the tool_conf.xml definition.

Modify manually the `galaxy_dir/config/integrated_tool_panel.xml`:

```
    <section id="frogs_local" name="FROGS local" version="">
        <label id="frogs_otu_construction" text="OTUs reconstruction" version="" />
        <tool id="FROGS_demultiplex" />
        <tool id="FROGS_preprocess" />
        <tool id="FROGS_clustering" />
        <tool id="FROGS_remove_chimera" />
        <tool id="FROGS_OTU_filters" />
        <tool id="FROGS_itsx" />
        <tool id="FROGS_affiliation_OTU" />
        <tool id="FROGS_affiliation_filters" />
        <tool id="FROGS_affiliation_postprocess" />
        <tool id="FROGS_normalisation" />
        <tool id="FROGS_Tree" />
        <tool id="FROGS_clusters_stat" />
        <tool id="FROGS_affiliations_stat" />
        <tool id="FROGS_biom_to_stdBiom" />
        <tool id="FROGS_biom_to_tsv" />
        <tool id="FROGS_tsv_to_biom" />
        <label id="frogsstat_phyloseq" text="OTUs structure and composition analysis" version="" />
        <tool id="FROGSSTAT_Phyloseq_Import_Data" />
        <tool id="FROGSSTAT_Phyloseq_Composition_Visualisation" />
        <tool id="FROGSSTAT_Phyloseq_Alpha_Diversity" />
        <tool id="FROGSSTAT_Phyloseq_Beta_Diversity" />
        <tool id="FROGSSTAT_Phyloseq_Sample_Clustering" />
        <tool id="FROGSSTAT_Phyloseq_Structure_Visualisation" />
        <tool id="FROGSSTAT_Phyloseq_Multivariate_Analysis_Of_Variance" />
        <label id="frogsstat_deseq" text="Differential abundance analysis" version="" />
        <tool id="FROGSSTAT_DESeq2_Preprocess" />
        <tool id="FROGSSTAT_DESeq2_Visualization" />
    </section>
```



1. <u>Add images</u>

   Add the FROGS-wrappers images in `<Galaxy_Dir>/static/images` directory

   `cp <Galaxy_Dir>/tools/FROGS/static/images/* <Galaxy_Dir>/static/images/.`


# Use PEAR as reads merge software in preprocess
[PEAR](https://cme.h-its.org/exelixis/web/software/pear/) is one of the most effective software for read pair merging, but as its licence is not free for private use, we can not distribute it in FROGS.
If you work in an academic lab on a private Galaxy server, or if you have payed your licence you can use PEAR in FROGS preprocess.
For that, you need to:

* have PEAR in your PATH or in the FROGS libexec directory

* add PEAR in the FROGS-wrappers preprocess Galaxy wrapper (`<FROGS_DIR>/tools/preprocess/preprocess.xml`): 

  :warning: there is two places where the list `merge_software` is defined, add pear in both of them!

```
    <conditional name="merge_software_type">
        <param name="merge_software" type="select" label="Merge software" help="Select the software to merge paired-end reads.">
            <option value="vsearch" selected="true">Vsearch</option>
            <option value="flash">Flash</option>
            <option value="pear">PEAR</option>
        </param>
        <when value="flash">
            <param name="expected_amplicon_size" type="integer" label="Expected amplicon size" help="Maximum amplicon length expected in approximately 90% of the amplicons." value="" />
        </when>
    </conditional>
```

:warning: remember, there is two places where the list `merge_software` is defined, add pear in both of them!

# Upload and configure the databanks

Databanks are defined in `loc` files and `loc` files are defined in Galaxy datatable. 

* FROGS provides a data_manager. It concerns only taxonomical assignation databank which are listed here : http://genoweb.toulouse.inra.fr/frogs_databanks/assignation/FROGS_databases.tsv.txt.

  You may choose to download all preformated database, or filter them on:

  * date : all availbale database since DATE
  * amplicon : ex: 16S
  * base : ex SILVA
  * filters : this column is not always filled, but we propose SILVA database filtered on pintail score
  * version	: ex : 138.1
  
* Manual installation :

  * datatables : `<Galaxy_Dir>/config/tool_data_table_conf.xml` , example : `<Galaxy_Dir>/tools/FROGS/tool_data_table_conf.xml.sample`

    Add FROGS-wrappers datatables in the Galaxy datatables, but replace `{__HERE__}` by `tools/FROGS`. 

  * loc files example : `<Galaxy_Dir>/tools/FROGS/tool-data/`

    Copy and rename them as indicated in the tool_data_table.

    Then add entry as indicated in each loc files.

* Toolshed installation : 

  * datatables : `<Galaxy_Dir>/config/shed_tool_data_table_conf.xml` (nothing to modify, FROGS datatables should automatically be added)
  * loc files to filled in : `tool-data/toolshed.g2.bx.psu.edu/repos/frogs/frogs/<RANDOM>/`



We provide some databanks for each of these 3 data tables, you simply need to download them and add them in the corresponding `loc` files. 

- Assignation databank for affiliation_OTU tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/assignation

  loc file :`frogs_db.loc`

- Contaminant databank for filter tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/contaminants

  loc file : `frogs_contaminant_db.loc`

- Hyper variable in length amplicon databank for affiliation_postprocess tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/HVL

  loc file : `frogs_HVL.loc`


# Galaxy configuration

## setup Galaxy environment variables

FROGS python programs (and all dependencies) need to be available in the PATH, if not installing from the toolshed, you need to add `<FROGS_PATH>/app` directory in the Galaxy PATH environment variable. (see [environment-setup-file parameter](https://docs.galaxyproject.org/en/latest/admin/config.html#environment-setup-file) ). 

You can also activate `conda` as tool dependency resolver (https://docs.galaxyproject.org/en/latest/admin/conda_faq.html) by setting `conda_prefix` path and `conda_auto_install ` to `true` in the `<Galaxy_dir>/config/galaxy.yml` configuration file.

## Install python packages inside virtual env

Galaxy runs in a specific virtual env. To allow FROGS clusters stat to access to the python scipy library, you may need to (re)install it inside the Galaxy virtual env
```
cd <Galaxy_Dir>
source .venv/bin/activate
pip install scipy
deactivate
```

## Avoid FROGS HTML report sanitization

By default Galaxy sanitizes HTML outputs to prevent XSS attacks.
FROGS outputs, for almost all tools, report in HTML format. To allow their visualization inside Galaxy, we need to avoid the Galaxy sanitization.
You need to uncomment `sanitize_whitelist_file` line in `<Galaxy_Dir>/config/galaxy.ini`, create the corresponding `<Galaxy_Dir>/config/sanitize_whitelist.txt` file if not already done, and add the following lines in it. You may also manage it from the Admin interface of Galaxy in the `Manage Allowlist` section.

```
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_DESeq2_Preprocess/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_DESeq2_Visualization/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Alpha_Diversity/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Beta_Diversity/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Composition_Visualisation/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Import_Data/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Multivariate_Analysis_Of_Variance/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Sample_Clustering/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGSSTAT_Phyloseq_Structure_Visualisation/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_OTU_filters/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_Tree/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_affiliation_OTU/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_affiliation_filters/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_affiliations_stat/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_clusters_stat/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_itsx/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_normalisation/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_preprocess/3.2.1
toolshed.g2.bx.psu.edu/repos/frogs/frogs/FROGS_remove_chimera/3.2.1

```

## Set memory and parallelisation settings

If you have more than one CPU, it is recommended to increase the number of CPUs used by tools.

All CPUs must be on the same computer/node.


   * Specifications

     |         Tool          | RAM per CPU | Minimal RAM | Configuration example |
     | :-------------------: | :---------: | :---------: | :-------------------: |
     |      preprocess       |     8Gb     |      -      |   12 CPUs and 96 GB   |
     |      clustering       |      -      |    10 Gb    |   16 CPUs and 60 GB   |
     | ITSx / remove_chimera |     3Gb     |     5Gb     |   12 CPUs and 36 GB   |
     |    affiliation_OTU    |      -      |    20 Gb    |  30 CPUs and 300 GB   |

   * Galaxy configuration

     You need to add `destiantion` sections (one per tool) in the `<Galaxy-Dir>/config/job_conf.xml` 
     Example for SGE scheduler:


```
<destinations>
	...
	<destination id="FROGS_preprocess_job" runner="drmaa">
		<param id="galaxy_external_runjob_script">scripts/drmaa_external_runner.py</param>
		<param id="galaxy_external_killjob_script">scripts/drmaa_external_killer.py</param>
		<param id="galaxy_external_chown_script">scripts/external_chown_script.py</param>
		<param id="nativeSpecification">-clear -q galaxyq -l mem=5G -l h_vmem=13G -pe parallel_smp 12</param>
	</destination>
	<destination id="FROGS_clustering_job" runner="drmaa">
		<param id="galaxy_external_runjob_script">scripts/drmaa_external_runner.py</param>
		<param id="galaxy_external_killjob_script">scripts/drmaa_external_killer.py</param>
		<param id="galaxy_external_chown_script">scripts/external_chown_script.py</param>
		<param id="nativeSpecification">-clear -q galaxyq -l mem=3G -l h_vmem=10G -pe parallel_smp 16</param>
	</destination>
	<destination id="FROGS_remove_chimera_job" runner="drmaa">
		<param id="galaxy_external_runjob_script">scripts/drmaa_external_runner.py</param>
		<param id="galaxy_external_killjob_script">scripts/drmaa_external_killer.py</param>
		<param id="galaxy_external_chown_script">scripts/external_chown_script.py</param>
		<param id="nativeSpecification">-clear -q galaxyq -l mem=3G -l h_vmem=4G -pe parallel_smp 12</param>
	</destination>
	<destination id="FROGS_itsx_job" runner="drmaa">
		<param id="galaxy_external_runjob_script">scripts/drmaa_external_runner.py</param>
		<param id="galaxy_external_killjob_script">scripts/drmaa_external_killer.py</param>
		<param id="galaxy_external_chown_script">scripts/external_chown_script.py</param>
		<param id="nativeSpecification">-clear -q galaxyq -l mem=3G -l h_vmem=4G -pe parallel_smp 12</param>
	</destination>
	<destination id="FROGS_affiliation_OTU_job" runner="drmaa">
		<param id="galaxy_external_runjob_script">scripts/drmaa_external_runner.py</param>
		<param id="galaxy_external_killjob_script">scripts/drmaa_external_killer.py</param>
		<param id="galaxy_external_chown_script">scripts/external_chown_script.py</param>
		<param id="nativeSpecification">-clear -q galaxyq -l mem=7G -l h_vmem=10G -pe parallel_smp 30</param>
	</destination>
</destinations>
<tools>
...
	<tool id="FROGS_preprocess" destination="FROGS_preprocess_job"/>   
	<tool id="FROGS_clustering" destination="FROGS_clustering_job"/>     
	<tool id="FROGS_remove_chimera" destination="FROGS_remove_chimera_job"/> 
	<tool id="FROGS_itsx" destination="FROGS_itsx_job"/> 
	<tool id="FROGS_affiliation_OTU" destination="FROGS_affiliation_OTU_job"/>
</tools>
```

# License
    GNU GPL v3

# Copyright
    2021 INRAE

# Citation
    Please cite the **FROGS article**: *Escudie F., et al. Bioinformatics, 2018. FROGS: Find, Rapidly, OTUs with Galaxy Solution.*

# Contact
    frogs-support@inrae.fr

