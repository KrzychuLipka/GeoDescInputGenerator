import random
import json
from typing import List
from pathlib import Path
from data_repository import (
    floors,
    rooms,
    landmarks,
    landmark_positions,
    user_positions,
)


class DataGenerator:
    TAG = "DataGenerator"

    def __init__(self, output_dir: str = ".", dataset_size: int = 1000):
        self.dataset_size = dataset_size
        self.output_path = Path(output_dir) / "geo_dataset_input.txt"

    def generate(self):
        with self.output_path.open("w", encoding="utf-8") as f:
            for _ in range(self.dataset_size):
                f.write(self.generate_input_line() + "\n")
        print(
            f"[{self.TAG}] Wygenerowano {self.dataset_size} danych wej. i zapisano do {self.output_path}"
        )

    def generate_input_line(self) -> str:
        floor = random.choice(floors)
        room = random.choice(rooms)
        landmark = random.choice(landmarks)
        user_position = random.choice(user_positions)
        landmark_position = random.choice(landmark_positions)
        include_landmark_info = random.choice([True, False])
        parts: list[str] = [
            "geoDescriptionType: location;",
            f"floor: {floor};",
            f"userPositionInfo: {user_position} {room};",
        ]

        if include_landmark_info:
            parts.append(f"landmarkPositionInfo: {landmark} {landmark_position};")

        return " ".join(parts)

if __name__ == "__main__":
    generator = DataGenerator(output_dir=".")
    generator.generate()

# from lmstudio import llm

# model = llm()  # automatycznie łączy się z lokalnym serwerem

# response = model.predict(
#     prompt="Hello",
#     max_tokens=50,
#     temperature=0.2
# )

# print(response.text)
