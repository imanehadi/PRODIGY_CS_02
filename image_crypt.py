#!/usr/bin/env python3

import argparse
import hashlib
from pathlib import Path
import numpy as np
from PIL import Image

def key_to_seed(key: str) -> int:
    digest = hashlib.sha256(key.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big", signed=False)

def load_image(path: Path):
    img = Image.open(path)
    arr = np.array(img)
    return img.mode, arr

def save_image(arr: np.ndarray, mode: str, path: Path):
    Image.fromarray(arr, mode).save(path)

def prng_keystream(shape, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=shape, dtype=np.uint8)

def permute_pixels(arr: np.ndarray, seed: int):
    h, w = arr.shape[0], arr.shape[1]
    c = 1 if arr.ndim == 2 else arr.shape[2]
    rng = np.random.default_rng(seed)
    n = h * w
    perm = rng.permutation(n)
    flat = arr.reshape(n, c)
    permuted = flat[perm]
    return permuted.reshape(arr.shape), perm

def unpermute_pixels(arr: np.ndarray, perm: np.ndarray):
    h, w = arr.shape[0], arr.shape[1]
    c = 1 if arr.ndim == 2 else arr.shape[2]
    inv = np.empty_like(perm)
    inv[perm] = np.arange(perm.size, dtype=perm.dtype)
    flat = arr.reshape(-1, c)
    unperm = flat[inv]
    return unperm.reshape(arr.shape)

def encrypt_array(arr: np.ndarray, key: str, mode: str) -> np.ndarray:
    seed = key_to_seed(key)
    out = arr.copy()
    if mode in ("shuffle", "both"):
        out, _ = permute_pixels(out, seed)
    if mode in ("xor", "both"):
        ks = prng_keystream(out.shape, seed)
        out = np.bitwise_xor(out, ks)
    return out

def decrypt_array(arr: np.ndarray, key: str, mode: str) -> np.ndarray:
    seed = key_to_seed(key)
    out = arr.copy()
    if mode in ("xor", "both"):
        ks = prng_keystream(out.shape, seed)
        out = np.bitwise_xor(out, ks)
    if mode in ("shuffle", "both"):
        _, perm = permute_pixels(np.zeros_like(out), seed)
        out = unpermute_pixels(out, perm)
    return out

def encrypt_image(in_path: Path, out_path: Path, key: str, mode: str):
    img_mode, arr = load_image(in_path)
    enc = encrypt_array(arr, key, mode)
    save_image(enc, img_mode, out_path)

def decrypt_image(in_path: Path, out_path: Path, key: str, mode: str):
    img_mode, arr = load_image(in_path)
    dec = decrypt_array(arr, key, mode)
    save_image(dec, img_mode, out_path)

def build_parser():
    p = argparse.ArgumentParser(description="Image Encryptor via Pixel Manipulation (educational).")
    sub = p.add_subparsers(dest="command", required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("-i", "--input", required=True, help="Input image path")
    common.add_argument("-o", "--output", required=True, help="Output image path")
    common.add_argument("-k", "--key", required=True, help="Passphrase / key")
    common.add_argument("-m", "--mode", choices=["xor", "shuffle", "both"], default="both", help="Mode of operation")
    sub.add_parser("encrypt", parents=[common], help="Encrypt an image")
    sub.add_parser("decrypt", parents=[common], help="Decrypt an image")
    return p

def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "encrypt":
        encrypt_image(Path(args.input), Path(args.output), args.key, args.mode)
    else:
        decrypt_image(Path(args.input), Path(args.output), args.key, args.mode)
    print(f"{args.command.capitalize()}ed -> {args.output}")

if __name__ == "__main__":
    main()
