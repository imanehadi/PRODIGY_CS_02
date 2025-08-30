project:
  name: "Image Encryptor via Pixel Manipulation"
  description: >
    This is a simple educational project that demonstrates image encryption and
    decryption using pixel manipulation in Python. It allows you to encrypt images
    by shuffling pixel positions and/or applying XOR with a pseudorandom keystream,
    and then decrypt them back to the original.

features:
  - "Encrypt images using XOR: pixel values are XORed with a pseudorandom keystream derived from a passphrase."
  - "Encrypt images using Shuffle: pixel positions are permuted pseudorandomly."
  - "Encrypt images using Both: Shuffle then XOR."
  - "Decrypt images back to their original form."
  - "Command-line interface (CLI) for easy usage."

requirements:
  python: "3.10+"
  libraries:
    - "Pillow"
    - "numpy"

installation:
  ubuntu:
    - "sudo apt update"
    - "sudo apt install -y python3-pil python3-numpy"
  virtualenv:
    - "python3 -m venv .venv --system-site-packages"
    - "source .venv/bin/activate"
    - "pip install pillow numpy"

usage:
  encrypt:
    description: "Encrypt an image"
    command: "python3 image_crypt.py encrypt -i <input_image> -o <output_image> -k <key> -m <mode>"
    example:
      - command: "python3 image_crypt.py encrypt -i photo.png -o photo.enc.png -k 'my-secret-key' -m both"
      - input_image: "photo.png"
      - output_image: "photo.enc.png"
      - key: "my-secret-key"
      - mode: "both"
  decrypt:
    description: "Decrypt an image"
    command: "python3 image_crypt.py decrypt -i <input_image> -o <output_image> -k <key> -m <mode>"
    example:
      - command: "python3 image_crypt.py decrypt -i photo.enc.png -o photo.dec.png -k 'my-secret-key' -m both"
      - input_image: "photo.enc.png"
      - output_image: "photo.dec.png"
      - key: "my-secret-key"
      - mode: "both"

project_structure:
  - "image_crypt.py       # Main Python script"
  - "README.yaml          # Project documentation (this file)"
  - ".gitignore           # Ignore virtual environment & temporary files"
      - "photo.enc.png"
      - "photo.dec.png"

notes:
  - "Always use the same key and mode for encryption and decryption."
  - "The project uses NumPy arrays for pixel manipulation and Pillow for reading/writing images."
  - "Designed for educational purposes: demonstrates basic image encryption techniques."










