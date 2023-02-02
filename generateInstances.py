import json
import random
import exrex
from collections import ChainMap

outJSON = "file.json"
numberOfIterations = 100 #Defines the number of differnt residue-pairs we sample for a single pattern

#TODO: I believe that there are some specific cases like Ter for X missing :-)
#TODO: I generated the three maps by hand! They are not perfect and some long forms are missing!

# A dictionary mapping three-letter amino acids codes onto one-letter
# amino acid codes
ThreeToOne = \
 {'A': 'Ala',
  'R': 'Arg',
  'N': 'Asn',
  'D': 'Asp',
  'C': 'Cys',
  'Q': 'Gln',
  'E': 'Glu',
  'G': 'Gly',
  'H': 'His',
  'I': 'Ile',
  'L': 'Leu',
  'K': 'Lys',
  'M': 'Met',
  'F': 'Phe',
  'P': 'Pro',
  'S': 'Ser',
  'T': 'Thr',
  'W': 'Trp',
  'Y': 'Tyr',
  'V': 'Val', }


# A dictionary mapping amino acid names to their one-letter abbreviations
ThreeToFull = \
 {'ALANINE': 'Ala',
  'ARGENINE': 'Arg',
  'ASPARAGINE': 'Asn',
  'ASPARTIC ACID': 'Asp',
  'CYSTEINE': 'Cys',
  'GLUTAMINE': 'Gln',
  'GLUTAMIC ACID': 'Glu',
  'GLYCINE': 'Gly',
  'HISTIDINE': 'His',
  'ISOLEUCINE': 'Ile',
  'LEUCINE': 'Leu',
  'LYSINE': 'Lys',
  'METHIONINE': 'Met',
  'PHENYLALANINE': 'Phe',
  'PROLINE': 'Pro',
  'SERINE': 'Ser',
  'THREONINE': 'Thr',
  'TRYPTOPHAN': 'Trp',
  'TYROSINE': 'Tyr',
  'VALINE': 'Val', }


ThreeToThree =  {'Ala': 'Ala',
  'Arg': 'Arg',
  'Asn': 'Asn',
  'Asp': 'Asp',
  'Cys': 'Cys',
  'Gln': 'Gln',
  'Glu': 'Glu',
  'Gly': 'Gly',
  'His': 'His',
  'Ile': 'Ile',
  'Leu': 'Leu',
  'Lys': 'Lys',
  'Met': 'Met',
  'Phe': 'Phe',
  'Pro': 'Pro',
  'Ser': 'Ser',
  'Thr': 'Thr',
  'Trp': 'Trp',
  'Tyr': 'Tyr',
  'Val': 'Val', }

fullDict = ChainMap(ThreeToThree, ThreeToOne, ThreeToFull)

longForm = list(ThreeToFull.keys())
threeForm = list(ThreeToThree.keys())
oneForm = list(ThreeToOne.keys())

#TODO: Here we can define from wich set of AA we want to sample (e.g.,
vocabulary  = longForm

patterns = [
    "<WRES>\s<PPOS>\s<MRES>",
    "<WRES><PPOS>(?:-{0,2}>|→)<MRES>"
]

data = {}
for pattern in patterns:

    instances = []
    for i in range(numberOfIterations):



        random.shuffle(vocabulary)


        WRES = vocabulary[0]  #Wildtype residue
        MRES = vocabulary[1] # Mutated residue
        PPOS = str(random.randint(1,2000)) #Location

        text = pattern
        text = text.replace("<WRES>", WRES)
        text = text.replace("<MRES>", MRES)
        text = text.replace("<PPOS>", PPOS)

        numberOfPossibleTexts = exrex.count(text, 500)#How many text pairs can we generate (with a limit)
        sample = list(exrex.generate(text, min(numberOfPossibleTexts, 500))) #Generate up to 500 permutations of the text
        random.shuffle(sample)

        #TODO: Currently we cover only *protein* *substitutions*
        hgvs = "p." +fullDict[WRES] +PPOS +fullDict[MRES]


        instance = {}
        instance["samples"] = sample[0:10]
        instance["hgvs"] = hgvs
        instances.append(instance)
    data[pattern] = instances



json_object = json.dumps(data, indent=4)
with open(outJSON, "w") as outfile:
    outfile.write(json_object)
