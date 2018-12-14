<img src="static/images/FROGS_logo.png" width="20%" style="display: block; margin: auto;"/>



[![Release](https://img.shields.io/badge/release-3.1.0-blue.svg)![Date](https://img.shields.io/badge/date-DD%20Month%20YYYY-red.svg)](https://github.com/geraldinepascal/FROGS-wrappers/releases)



# Description

FROGS is a workflow designed to produce an OTU count matrix from high depth sequencing amplicon data.

FROGS-wrapper allow to add FROGS on a Galaxy instance.


​    
# Installing FROGS-wrapper

## Simplest way

FROGS is available in the Toolshed : [release 2.0.0](https://toolshed.g2.bx.psu.edu/repository?repository_id=525e78406276b403&changeset_revision=76c750c5f0d1)

It will install FROGS thanks to [conda](https://anaconda.org/bioconda/frogs), download all these XML tools and well configure them in your Galaxy.

## From source

#### Prerequisites

You should start by installing [FROGS](https://github.com/geraldinepascal/FROGS) (remember, FROGS is now installable via [conda](https://anaconda.org/bioconda/frogs) )

FROGS python programs need to be available in your path, if installing from source, you need to add `<FROGS_PATH>/app` directory in the Galaxy PATH environment variable. (see [environment-setup-file parameter](https://docs.galaxyproject.org/en/latest/admin/config.html#environment-setup-file) )

#### FROGS-wrapper installation

1.    <u>Download wrapper</u>

   Download the last released versions of FROGS-wrapper
   ​        Available at https://github.com/geraldinepascal/FROGS-wrappers/releases

   Uncompress and unarchive the release in your ` <Galaxy_Dir>/tools` directory

   (replace the) link to the new directory like this

   ` ln -s <Galaxy_Dir>/tools/FROGS-wrapper-<Release_Number>  <Galaxy_Dir>/tools/FROGS`

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
           <tool file="FROGS/clusters_stat.xml" />
           <tool file="FROGS/affiliations_stat.xml" />
           <tool file="FROGS/biom_to_stdBiom.xml" />
           <tool file="FROGS/biom_to_tsv.xml" />
           <tool file="FROGS/tsv_to_biom.xml" />
           <tool file="FROGS/tree.xml" />
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
   If you used previous version of FROGS, you must removed `app` direcotry path. 

3. <u>Add images</u>

   **Deal with images ??**

4. <u>Set memory and parallelisation settings</u>

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

# Upload and configure the databanks

3 tools use external databanks. Theses databanks are defined in `loc` files and `loc` files are defined in Galaxy datatable. 

**Deal with data-table???**  

We provide some databanks for each of them, you simply need to download them and add them in the corresponding `loc` files.

- Assignation databank for affiliation_OTU tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/assignation

  `loc` file example : `<FROGS-wrapper_Dir>/tool-data/frogs_db.loc.sample`

- Contaminant databank for filter tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/contaminants

  `loc` file example : `<FROGS-wrapper_Dir>/tool-data/phiX_db.loc.sample`

- Hyper variable in length amplicon databank for affiliation_postprocess tool

  URL : http://genoweb.toulouse.inra.fr/frogs_databanks/HVL

  `loc` file example : `<FROGS-wrapper_Dir>/tool-data/HVL.loc.sample`



# License
    GNU GPL v3

# Copyright
    2018 INRA

# Citation
    Please cite the **FROGS article**: *Escudie F., et al. Bioinformatics, 2018. FROGS: Find, Rapidly, OTUs with Galaxy Solution.*

# Contact
    frogs@inra.fr

