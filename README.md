# Radiology-Report-Generation
Python demonstration of using two different neural networks to generate radiology reports

Original paper: Progressive Transformer-Based Generation of Radiology Reports:

https://arxiv.org/pdf/2102.09777.pdf


The authors have used a two stage process with the first neural network labeling an X-Ray like so:

POSITIVE - improved bilateral airspace opaci.

UNCERTAIN airspace disease

NEGATIVE consolidations identified pneumothorax


With the following neural network using those generated results as the inputs for writing a complete radiology report:

"Compared to previous examination, there is a significant imporvement in aeration bilaterally, with improved bilateral airspace opacities. Currently, there are only minimal streaky opacities in the bilateral midlung..."


They hope that this can solve two main problems - replace the extensive training necessary for humans to be able to generate comparable results with machine learning, and potentially homogenize the resulting reports, so that they'll be similar across time and space (with humans writing the reports there's always going to be some variation with how things are phrased, written, and maybe missed).

This repository contains a recipe for understanding the methods behind the paper, and a Python example of how to generate the reports using CNN's and NLG.
