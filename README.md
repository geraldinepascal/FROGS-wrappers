​					<img src="static/images/frogs_images/FROGS_logo.png" width="20%" style="display: block; margin: auto;"/>					<img src="galaxy_project_logo_square.png" width="20%" style="display: block; margin: auto;"/> 



Visit our web site : http://frogs.toulouse.inra.fr/

[![Release](https://img.shields.io/badge/release-3.1.0-blue.svg)![Date](https://img.shields.io/badge/date-January%202018-red.svg)](https://github.com/geraldinepascal/FROGS-wrappers/releases)[<img src="https://www.podcastscience.fm/wp-content/uploads/2017/12/deezer.png" width="5%" style="display: block; margin: auto;"/>](https://www.deezer.com/fr/playlist/5233843102?utm_source=deezer&utm_content=playlist-5233843102&utm_term=18632989_1545296531&utm_medium=web)



# Description

FROGS is a workflow designed to produce an OTU count matrix from high depth sequencing amplicon data.

FROGS-wrapper allow to add FROGS on a Galaxy instance.

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

The 22 FROGS tools will be in random order in your tools panel. We propose to control that order by modifying the `integrated_tool_panel.xml `. 

We suppose that you installed FROGS in a spécific section named `FROGS` (update the FROGS version if necessary).

```
<section id="FROGS" name="FROGS" version="">

    <label text="OTUs reconstruction" id="FROGS_OTU" />

    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_demultiplex/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_preprocess/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_clustering/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_remove_chimera/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_filters/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_itsx/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_affiliation_OTU/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_affiliation_postprocess/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_normalisation/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_Tree/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_clusters_stat/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_affiliations_stat/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_biom_to_stdBiom/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_biom_to_tsv/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGS_tsv_to_biom/3.1" />

    <label text="OTUs structure and composition analysis" id="FROGSSTAT_Phyloseq" />
    
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGSSTAT_Phyloseq_Import_Data/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGSSTAT_Phyloseq_Composition_Visualisation/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGSSTAT_Phyloseq_Alpha_Diversity/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGSSTAT_Phyloseq_Beta_Diversity/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGSSTAT_Phyloseq_Sample_Clustering/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGSSTAT_Phyloseq_Structure_Visualisation/3.1" />
    <tool id="toolshed.g2.bx.psu.edu/repos/frogs/frogs_3_1_0/FROGSSTAT_Phyloseq_Multivariate_Analysis_Of_Variance/3.1" />
</section>
```



## From sources

#### Prerequisites

You should start by installing [FROGS](https://github.com/geraldinepascal/FROGS) (remember, FROGS is now installable via [conda](https://anaconda.org/bioconda/frogs) )

#### FROGS-wrappers installation

1.    <u>Download wrapper</u>

   Download the last released versions of FROGS-wrappers: https://github.com/geraldinepascal/FROGS-wrappers/releases

   Uncompress and unarchive the release in your ` <Galaxy_Dir>/tools` directory

   (replace the) link to the new directory like this

   ` ln -s <Galaxy_Dir>/tools/FROGS-wrappers-<Release_Number>  <Galaxy_Dir>/tools/FROGS`

2.   <u>Add tools in galaxy</u>

   Add the tools in `<Galaxy_Dir>/config/tool_conf.xml`

   ```
       <section id="FROGS_wrappers" name="FROGS">
       <label text="OTUs reconstruction" id="FROGS_OTU" />
           <tool file="FROGS/demultiplex.xml" />
           <tool file="FROGS/preprocess.xml" />
           <tool file="FROGS/clustering.xml" />
           <tool file="FROGS/remove_chimera.xml" />  
           <tool file="FROGS/filters.xml" />
           <tool file="FROGS/itsx.xml" />
           <tool file="FROGS/affiliation_OTU.xml" />
           <tool file="FROGS/affiliation_postprocess.xml" />
           <tool file="FROGS/normalisation.xml" />
           <tool file="FROGS/tree.xml" />
           <tool file="FROGS/clusters_stat.xml" />
           <tool file="FROGS/affiliations_stat.xml" />
           <tool file="FROGS/biom_to_stdBiom.xml" />
           <tool file="FROGS/biom_to_tsv.xml" />
           <tool file="FROGS/tsv_to_biom.xml" />
       <label text="OTUs structure and composition analysis" id="FROGSSTAT_Phyloseq" />
           <tool file="FROGS/r_import_data.xml" />
           <tool file="FROGS/r_composition.xml" />
           <tool file="FROGS/r_alpha_diversity.xml" />
           <tool file="FROGS/r_beta_diversity.xml" />
           <tool file="FROGS/r_structure.xml" />
           <tool file="FROGS/r_clustering.xml" />
           <tool file="FROGS/r_manova.xml" />
       </section>     
   ```
   NB: If you used previous version of FROGS, you must removed `app` direcotry name in the paths names. 

3. <u>Add images</u>

   Add the FROGS-wrappers images in `<Galaxy_Dir>/static/images` directory
   
   `cp -r <Galaxy_Dir>/tools/FROGS/static/images/frogs_images/ <Galaxy_Dir>/static/images/.`


# Use PEAR as reads merge software in preprocess
[PEAR](https://cme.h-its.org/exelixis/web/software/pear/) is one of the most effective software for read pair merging, but as its licence is not free for private use, we can not distribute it in FROGS.
If you work in an academic lab on a private Galaxy server, or if you have payed your licence you can use PEAR in FROGS preprocess.
For that, you need to:

* have PEAR in your PATH or in the FROGS libexec directory

* add PEAR in the FROGS preprocess Galaxy wrapper (<FROGS_DIR>/tools/preprocess/preprocess.xml): 

  :warning: there is two places where the list merge_software is defined, add pear in both of them!

  add pear value in the list of `merge_software`
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

:warning: remember, there is two places where the list merge_software is defined, add pear in both of them!

# Upload and configure the databanks

Databanks are defined in `loc` files and `loc` files are defined in Galaxy datatable. 

* Manual installation :

  * datatables : `<Galaxy_Dir>/config/tool_data_table_conf.xml` , example : `<Galaxy_Dir>/tools/FROGS/tool_data_table_conf.xml.sample`

    Add FROGS-wrappers datatables in the Galaxy datatables, but replace `{__HERE__}` by `tools/FROGS`. 

  * loc files example : `<Galaxy_Dir>/tools/FROGS/tool-data/`

    Copy and rename them as indicated in the tool_data_table.

    Then add entry as indicated in each loc files.

* Toolshed installation : 

  * datatables : `<Galaxy_Dir>/config/shed_tool_data_table_conf.xml` (nothing to modify, FROGS datatables should automatically be added)
  * loc files to filled in : `tool-data/toolshed.g2.bx.psu.edu/repos/frogs/frogs_<VERSION>/<RANDOM>/`



We provide some databanks for each of these 3 data tables, you simply need to download them and add them in the corresponding `loc` files. 

- Assignation databank for affiliation_OTU tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/assignation

  loc file :`frogs_db.loc`

- Contaminant databank for filter tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/contaminants

  loc file : `phiX_db.loc`

- Hyper variable in length amplicon databank for affiliation_postprocess tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/HVL

  loc file : `HVL.loc`


# Galaxy configuration

## setup Galaxy environment variables

FROGS python programs need to be available in the PATH, if installing from source or via conda, you need to add `<FROGS_PATH>/app` directory in the Galaxy PATH environment variable. (see [environment-setup-file parameter](https://docs.galaxyproject.org/en/latest/admin/config.html#environment-setup-file) )

## Install python packages inside virtual env

Galaxy runs in a specific virtual env. To allow FROGS clusters stat to access to the python scipy library, you need to (re)install it inside the Galaxy virtual env
```
cd <Galaxy_Dir>
source .venv/bin/activate
pip install scipy
deactivate
```

## Avoid FROGS HTML report sanitization

By default Galaxy sanitizes HTML outputs to prevent XSS attacks.
FROGS outputs, for almost all tools, report in HTML format. To allow their visualization inside Galaxy, we need to avoid the Galaxy sanitization.
You need to uncomment `sanitize_whitelist_file` line in `<Galaxy_Dir>/config/galaxy.ini`, create the corresponding `<Galaxy_Dir>/config/sanitize_whitelist.txt` file if not already done, and add the following lines in it.
```
FROGSSTAT_Phyloseq_Alpha_Diversity
FROGSSTAT_Phyloseq_Beta_Diversity
FROGSSTAT_Phyloseq_Composition_Visualisation
FROGSSTAT_Phyloseq_Import_Data
FROGSSTAT_Phyloseq_Multivariate_Analysis_Of_Variance
FROGSSTAT_Phyloseq_Sample_Clustering
FROGSSTAT_Phyloseq_Structure_Visualisation
FROGS_Tree
FROGS_affiliation_OTU
FROGS_affiliations_stat
FROGS_clustering
FROGS_clusters_stat
FROGS_filters
FROGS_itsx
FROGS_normalisation
FROGS_preprocess
FROGS_remove_chimera
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
    2018 INRA

# Citation
    Please cite the **FROGS article**: *Escudie F., et al. Bioinformatics, 2018. FROGS: Find, Rapidly, OTUs with Galaxy Solution.*

# Contact
    frogs@inra.fr

