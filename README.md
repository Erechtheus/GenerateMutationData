# GenerateMutationData


#List of research questions

- Can the model represent the location correctly? Basically, the question is if the model can copy the numbers from the src-text
- Is the model able to recognize different surface forms of AA (Can we train a model on long/tripple/or single-forms only?)
  - Long-form (Alanine)
  - Tripple-form (ala)
  - Single-form (A)
- How does our model perform on PubMed? (i.e., use our data from tmVar or SETH)
- Train a model on instances from Pattern 1-100 and test it on unseen patterns
- Can we train on longer context? E.g., use the sentence instead of single instances?
- Can we (to some degree) predict the reference sequence (e.g., cDNA, proteim) or different mutation types (e.g., substitution, deletion)


# TODO!
- The list of amino acids is not complete (e.g., Ter, Termination, X are  missing)
- The amino acids currently are all uppercase (I think that is nat what we want :)
- I generated the three amino-acids maps by hand! They are incorrect and some long forms are missing!
- Currently, I only generated patterns for Amino acid subsititutions
- Currently, I genereated only traning instances with the long form amino-acids (this can easily be changed)
- 
