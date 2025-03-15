import pandas as pd
import numpy as np

class BitmapIndex:
    def __init__(self, df: pd.DataFrame, column: str):
       """
       Initialize the BitmapIndex with a dataframe and column name.
       """ 
       self.df = df
       self.column = column
       self.bitmaps = {}
       self.compressed_bitmaps = {} # dict to store RLE compressed bitmaps
       self.create_bitmaps()
       self.compress()

    def create_bitmaps(self):
        """
        convert the column values into bitmap index representation.
        Each unique value gets its own bitmap.
        """
        unique_values = self.df[self.column].unique()
        for value in unique_values:
            self.bitmaps[value] = (self.df[self.column]==value).astype(int).values

    def run_length_encode(self,bitmap):
        """
        compress a binary bitmap using Run-Length encoding (RLE).
        """
        encoded = []
        prev_bit = bitmap[0]
        count = 1

        for bit in bitmap[1:]:
            if bit == prev_bit:
                count+=1
            else:
                encoded.append((count, prev_bit))
                count=1
                prev_bit = bit 

        encoded.append((count,prev_bit))
        return encoded
    
    def compress(self):
        """
        apply rle compression to all bitmaps.
        """
        self.compressed_bitmaps = {key: self.run_length_encode(bitmap) for key, bitmap in self.bitmaps.items()}

    def display(self):
        print(f"\nBitmap Index for Column: {self.column}")
        for key,bitmap in self.bitmaps.items():
            print(f"{key}:{bitmap}") 

        print("\nCompressed Bitmaps (RLE):")
        for key,rle in self.compressed_bitmaps.items():
            print(f"{key}",end=":")
            for count,prev_bit in rle:
                print(f"{count}:{prev_bit}",end=" ")
            print()


df = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'C', 'B', 'B', 'C', 'A', 'C', 'C']
}) 

bitmap_index = BitmapIndex(df, 'Category')
bitmap_index.display()




            

        