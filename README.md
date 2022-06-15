# Data-Analysis-Project
Immunology bioinformatician Technical Project

Questions
1) Is there a correlation between clone size and mutation?
When a clone undergoes expansion in the presence of antigen, it usually also undergoes mutation.  For each clone we have two fields avg_v_identity and copies.  The former gives the fraction of nucleotide bases in the clone that match the germline (e.g. 1 - mutation) and the latter the number of reads that are associated with the clone, giving a rough measure of size.

Given this, come up with a figure that one could use to see if there is a correlation between these two variables.  Next, statistically test the hypothesis that the two are related.
2) Is V-gene usage uniform within and consistent between donors?
During development, each B-cell undergoes V(D)J recombination that pseudo-randomly joins one V, one D, and one J gene to create part of the heavy-chain which goes on to encode a portion of the cell’s antibodies.  For this question we’ll focus on the V-gene which is annotated by the v_gene column.

Does it appear that within each donor V-genes are evenly distributed amongst clones?  How would you visualize this?  What happens when you look at V-gene usage weighted by copies?

Across donors, does it appear that there is a pattern of V-gene usage (i.e. do most donors use the same V-genes) or is each donor different?  How would you visualize this?
3) Does disease affect the clonal repertoire?
In this final task, we introduce one additional piece of information.  HPAP001, HPAP003, and HPAP004 are all healthy individuals whereas HPAP015, HPAP030, and HPAP031 have all been clinically diagnosed with type 1 diabetes.

We also describe a few more of the fields in the tables:

j_gene: J-gene of the clone
functional: If the clone is productive (i.e. in-frame and contains no stop codons)
cdr3_nt: CDR3 nucleotide sequence (the CDR3 is a highly-variable region where V, D, and J come together) 
cdr3_aa: The amino-acid translation of cdr3_nt
uniques: Number of unique sequences that were sequenced from the clone
germline: Germline sequence of the clone
top_copy_seq: Sequence of the top copy read in the clone

Given this, see if you can find a difference between controls and those with diabetes.  You may use any method and any fields you’d like, but please make at least one or two figures to present your findings.


This project answers these questions as well as provides an excel file on the current tsv files stored in the "analysis project" folder. Other tsv files can be replaced with the ones in the "analysis_project" folder and it will still work.