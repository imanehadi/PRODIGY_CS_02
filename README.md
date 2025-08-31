#  Image Encryptor via Pixel Manipulation

This is a simple **educational project** that demonstrates image encryption and decryption using **pixel manipulation** in Python.  
It allows you to **encrypt images** by shuffling pixel positions and/or applying XOR with a pseudorandom keystream, and then **decrypt them back** to the original.

---

## ✨ Features
- 🔒 Encrypt images using:
  - **XOR**: Pixel values are XORed with a pseudorandom keystream derived from a passphrase.
  - **Shuffle**: Pixel positions are permuted pseudorandomly.
  - **Both**: Shuffle then XOR.  
- 🔓 Decrypt images back to their original form.  
- 🖥️ Command-line interface (CLI) for easy usage.  

---

## 📦 Requirements
- Python 3.10+  
- Libraries:  
  - `Pillow` (for image handling)  
  - `numpy` (for pixel manipulation)  

---

## ⚙️ Installation & Usage

```bash
================= ⚙️ INSTALLATION =================
# On Ubuntu
sudo apt update
sudo apt install -y python3-pil python3-numpy

# Or, using pip inside a virtual environment
python3 -m venv .venv --system-site-packages
source .venv/bin/activate
pip install pillow numpy
===================================================


================= 🔒 ENCRYPT AN IMAGE ==============
python3 image_crypt.py encrypt -i <input_image> -o <output_image> -k <key> -m <mode>

# Example:
python3 image_crypt.py encrypt -i photo.png -o photo.enc.png -k "my-secret-key" -m both

# Options:
# -i → input image path
# -o → output image path
# -k → passphrase/key
# -m → mode (xor, shuffle, or both)
===================================================


================= 🔓 DECRYPT AN IMAGE ==============
python3 image_crypt.py decrypt -i <input_image> -o <output_image> -k <key> -m <mode>

# Example:
python3 image_crypt.py decrypt -i photo.enc.png -o photo.dec.png -k "my-secret-key" -m both
===================================================














