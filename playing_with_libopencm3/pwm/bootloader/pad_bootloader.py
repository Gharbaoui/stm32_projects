BOOTLOADER_SIZE = 0x8000
BOOTLOADER_FILE_NAME = "bootloader.bin"

with open(BOOTLOADER_FILE_NAME, "rb") as f:
    raw_file = f.read()

bytes_to_add = BOOTLOADER_SIZE - len(raw_file)
new_bytes = bytes([0xff for _ in range(bytes_to_add)])

with open(BOOTLOADER_FILE_NAME, "wb") as f:
    f.write(raw_file + new_bytes)