# Script for the IB IA Biology Bioinformatics
#
# Written by James Laitmer and Senal Bulumulle 
#
#

from Bio import Phylo
tree = Phylo.read('sample.xml', 'phyloxml')
Phylo.draw(tree)






