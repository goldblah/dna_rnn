#!/bin/bash

cd /opt/genes/genomes

mkdir -p data_csv

for d in */
	do
		cd $d
		python3 ~/fasta_to_pandas.py *_output.fasta *_output_750.fasta *_output_500.fasta '../data_csv'
		cd ..
	done
