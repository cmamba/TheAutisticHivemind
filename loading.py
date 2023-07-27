from datasets import GeneratorBasedBuilder, DatasetInfo, SplitGenerator, Split
from typing import Any, Dict, List, Tuple
import pandas as pd

class MyDataset(GeneratorBasedBuilder):
    def _info(self) -> DatasetInfo:
        return DatasetInfo(
            description="ME"
        )

    def _split_generators(self, dl_manager):
        return [
            SplitGenerator(
                name=Split.TRAIN,
                gen_kwargs={"filepath": "/content/drive/MyDrive/llm_data/STUPID.csv"},
            )
        ]

    def _generate_examples(self, filepath):
        print("Hey")
        df = pd.read_csv(filepath)
        for id, row in df.iterrows():
            yield id, {
                'text': row['train']
            }




