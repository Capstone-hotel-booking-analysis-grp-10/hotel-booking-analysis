import pandas as pd						            # Import to handle dataframe
from sdv.metadata import SingleTableMetadata		# Import to detect metadata from the dataframe (primary source or information for GAN
from sdv.single_table import CTGANSynthesizer		# Import to train and generate (sample) the data

data = pd.read_csv("file_name.csv")					# Read the file, it has to be integer encoded (labelled not one hot encoded)
		
metadata = SingleTableMetadata()					# Create metadata object
metadata.detect_from_dataframe(data)				# Detect metadata by giving the dataframe (data)

synthesizer = CTGANSynthesizer(metadata, epochs=500, verbose=True)	# Create Synthesizer Object | Epoch = Number of Iterations of Training | Verbose = shows progress
synthesizer.fit(data)							                    # Train the Synthesizer

synthetic_data = synthesizer.sample(num_rows=1000)			        # Sample the data from trained Synthesizer (1000 rows in this example)

synthetic_data.to_csv("synthetic_data.csv", index=False)		    # Save the data to csv