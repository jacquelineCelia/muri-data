This directory contains machine-readable original texts, tokenized texts, and
tree-parsed texts in parallel for Kinyarwanda and English.

The structure is as follows:

/orig
    
    All of the source files in XML format. Here is a rough description of the schema:
    - unit blocks: denote a higher-level discourse boundary like
      turns in interviews or paragraphs in written text.
    - align blocks: within each unit block, there is one or more align block,
      which denotes that all of its child elements are aligned (i.e., it contains
      parallel texts in Kinyarwanda and English or Kinyarwanda, English, and French)
    - text blocks: contains a langid attribute which specifies the language within
      this block
    - s blocks: contains a single sentence. These are provided because a single sentence
      in the Kinyarwanda may map to several sentences in English
    - the actual text, in UTF-8

/tok

    Each XML file maps to one or more tokenized files--one for each language. For example,
    kgmc_0002.xml contains Kinyarwanda and English, so there are kgmc_0002.kin.tok and
    a kgmc_0002.eng.tok files. The lines in these files are aligned (i.e., each line corresponds
    to the contents of an <align> block in the XML). Therefore, some lines contain multiple
    sentences, and the sentence boundaries are denoted by an <EOS> tag.

/parsed

    For some of the token files, we have completed tree-parsing. The files contain one tree
    per line, and the trees correspond to the lines in the token files. Therefore, line 1 in
    kgmc_0002.eng.tree is the translation of line 1 in kgmc_0002.kin.tree. Since a single tree
    may have to contain more than one sentence, we have introduced a top-level syntactic element:
    (TOP S S S ...), which can contain one or more sentence elements.

/info

    For each of the XML files, we extract all the available metadata and present it line-by-line
    so that it is aligned with the token and parsed files.

/morph

    Contains files with morphological segmentations and associated tools. In addition to 
    directories containing segmentations produced from our sources, there are a number of other
    directories, that include:

    /morph/token-decomp

        Files have a list of verb types that are broken up into morphological segments via a
        script rather than a human annotator.

    /morph/FST
    
        Finite-State Transducer for producing morphological analyses. Can be run using
        FOMA as described at the end of this document.

Each of these subdirectories is further divided into our sources:

kgmc

     Source: Kigali Genocide Memorial Center, Rwandan genocide survivor testimonies.
     Num docs: of 35, of which 1 is tree-parsed
     Translations: KGMC translators
     Syntactic annotation: Kyle Jerro

bbc

     Source: http://www.bbc.co.uk/gahuza/
     Num docs: 2
     Translations: provided by our volunteer informant
     Syntactic annotation: Kyle Jerro
	 
	 bbc_0001: http://www.bbc.co.uk/gahuza/imikino/2011/01/110126_rafael_concussion.shtml
	 bbc_0002: http://www.bbc.co.uk/gahuza/imikino/2010/11/101111_nigeriawomensoccer.shtml

igt

     Source: interlinear glossed texts from books and papers on Kinyarwanda
     Num docs: 1
     Translations: from the IGT
     Syntactic annotation: Evelyn Richter

Additional directories that are not subdivided into these sources are:

/gfl

    Contains GFL annotation files. These files contain the original sentence, along with an
    English translation and the associated GFL annotated version of the sentence. Only contains 
    data from KGMC.

/tagged

    POS annotations that have been timed in 30 minute blocks. Each file is broken up by comments 
    such as '%% After 0:30', which indicate how far the annotator had made it through the file 
    before the stated time. Both sentences (tokens) and types are annotated, in separate files.

/dict

    Contains a dictionary from kinyarwanda.net in XML format.



Setting up Foma for FSTs
------------------------

Download the most recent version (0.9.17 as of this writing) of Foma from 
http://code.google.com/p/foma/downloads/list and follow the instructions to install.

Set an environment variable for the directory where Foma is installed:

    $ export FOMA_HOME="/path/to/foma"
    
The directory at `FOMA_HOME` should contain the `flookup` executable:

    $ ls $FOMA_HOME
    flookup
    ...

Foma can be tested using the FSTs provided in this archive:

    $ echo "ngombe" | $FOMA_HOME/flookup FST/kin-20.fst
    ngombe	+V+1SG+gomb+PERF
