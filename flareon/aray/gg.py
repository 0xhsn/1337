from z3 import *
import hashlib
import binascii

byte_indices = range(85)
bytes_vars = [BitVec(f'byte_{i}', 8) for i in byte_indices]

# Add these constraints to the solver
s = Solver()
s.add(len(bytes_vars) == 85)
s.add(85 ^ bytes_vars[0] != 16)
s.add(85 ^ bytes_vars[0] != 41)
s.add(85 ^ bytes_vars[1] != 0)
s.add(85 ^ bytes_vars[1] != 232)
s.add(85 ^ bytes_vars[2] != 205)
s.add(85 ^ bytes_vars[2] != 54)
s.add(85 ^ bytes_vars[3] != 43)
s.add(85 ^ bytes_vars[3] != 147)
s.add(85 ^ bytes_vars[4] != 23)
s.add(85 ^ bytes_vars[4] != 161)
s.add(85 ^ bytes_vars[5] != 243)
s.add(85 ^ bytes_vars[5] != 43)
s.add(85 ^ bytes_vars[6] != 129)
s.add(85 ^ bytes_vars[6] != 39)
s.add(85 ^ bytes_vars[7] != 15)
s.add(85 ^ bytes_vars[7] != 221)
s.add(85 ^ bytes_vars[8] != 107)
s.add(85 ^ bytes_vars[8] != 2)
s.add(85 ^ bytes_vars[9] != 5)
s.add(85 ^ bytes_vars[9] != 164)
s.add(85 ^ bytes_vars[10] != 44)
s.add(85 ^ bytes_vars[10] != 205)
s.add(85 ^ bytes_vars[11] != 33)
s.add(85 ^ bytes_vars[11] != 107)
s.add(85 ^ bytes_vars[12] != 226)
s.add(85 ^ bytes_vars[12] != 116)
s.add(85 ^ bytes_vars[13] != 42)
s.add(85 ^ bytes_vars[13] != 219)
s.add(85 ^ bytes_vars[14] != 99)
s.add(85 ^ bytes_vars[14] != 161)
s.add(85 ^ bytes_vars[15] != 27)
s.add(85 ^ bytes_vars[15] != 205)
s.add(85 ^ bytes_vars[16] != 144)
s.add(85 ^ bytes_vars[16] != 7)
s.add(85 ^ bytes_vars[17] != 16)
s.add(85 ^ bytes_vars[17] != 208)
s.add(85 ^ bytes_vars[18] != 234)
s.add(85 ^ bytes_vars[18] != 33)
s.add(85 ^ bytes_vars[19] != 222)
s.add(85 ^ bytes_vars[19] != 31)
s.add(85 ^ bytes_vars[20] != 17)
s.add(85 ^ bytes_vars[20] != 83)
s.add(85 ^ bytes_vars[21] != 27)
s.add(85 ^ bytes_vars[21] != 94)
s.add(85 ^ bytes_vars[22] != 191)
s.add(85 ^ bytes_vars[22] != 31)
s.add(85 ^ bytes_vars[23] != 18)
s.add(85 ^ bytes_vars[23] != 242)
s.add(85 ^ bytes_vars[24] != 94)
s.add(85 ^ bytes_vars[24] != 217)
s.add(85 ^ bytes_vars[25] != 224)
s.add(85 ^ bytes_vars[25] != 47)
s.add(85 ^ bytes_vars[26] != 161)
s.add(85 ^ bytes_vars[26] != 44)
s.add(85 ^ bytes_vars[27] != 43)
s.add(85 ^ bytes_vars[27] != 244)
s.add(85 ^ bytes_vars[28] != 12)
s.add(85 ^ bytes_vars[28] != 238)
s.add(85 ^ bytes_vars[29] != 158)
s.add(85 ^ bytes_vars[29] != 37)
s.add(85 ^ bytes_vars[30] != 249)
s.add(85 ^ bytes_vars[30] != 18)
s.add(85 ^ bytes_vars[31] != 5)
s.add(85 ^ bytes_vars[31] != 32)
s.add(85 ^ bytes_vars[32] != 30)
s.add(85 ^ bytes_vars[32] != 77)
s.add(85 ^ bytes_vars[33] != 157)
s.add(85 ^ bytes_vars[33] != 27)
s.add(85 ^ bytes_vars[34] != 39)
s.add(85 ^ bytes_vars[34] != 115)
s.add(85 ^ bytes_vars[35] != 120)
s.add(85 ^ bytes_vars[35] != 18)
s.add(85 ^ bytes_vars[36] != 6)
s.add(85 ^ bytes_vars[36] != 95)
s.add(85 ^ bytes_vars[37] != 37)
s.add(85 ^ bytes_vars[37] != 141)
s.add(85 ^ bytes_vars[38] != 84)
s.add(85 ^ bytes_vars[38] != 8)
s.add(85 ^ bytes_vars[39] != 49)
s.add(85 ^ bytes_vars[39] != 18)
s.add(85 ^ bytes_vars[40] != 230)
s.add(85 ^ bytes_vars[40] != 49)
s.add(85 ^ bytes_vars[41] != 74)
s.add(85 ^ bytes_vars[41] != 233)
s.add(85 ^ bytes_vars[42] != 91)
s.add(85 ^ bytes_vars[42] != 1)
s.add(85 ^ bytes_vars[43] != 33)
s.add(85 ^ bytes_vars[43] != 251)
s.add(85 ^ bytes_vars[44] != 96)
s.add(85 ^ bytes_vars[44] != 17)
s.add(85 ^ bytes_vars[45] != 146)
s.add(85 ^ bytes_vars[45] != 19)
s.add(85 ^ bytes_vars[46] != 186)
s.add(85 ^ bytes_vars[46] != 18)
s.add(85 ^ bytes_vars[47] != 11)
s.add(85 ^ bytes_vars[47] != 119)
s.add(85 ^ bytes_vars[48] != 29)
s.add(85 ^ bytes_vars[48] != 99)
s.add(85 ^ bytes_vars[49] != 156)
s.add(85 ^ bytes_vars[49] != 10)
s.add(85 ^ bytes_vars[50] != 86)
s.add(85 ^ bytes_vars[50] != 219)
s.add(85 ^ bytes_vars[51] != 0)
s.add(85 ^ bytes_vars[51] != 204)
s.add(85 ^ bytes_vars[52] != 22)
s.add(85 ^ bytes_vars[52] != 238)
s.add(85 ^ bytes_vars[53] != 243)
s.add(85 ^ bytes_vars[53] != 19)
s.add(85 ^ bytes_vars[54] != 39)
s.add(85 ^ bytes_vars[54] != 141)
s.add(85 ^ bytes_vars[55] != 244)
s.add(85 ^ bytes_vars[55] != 17)
s.add(85 ^ bytes_vars[56] != 246)
s.add(85 ^ bytes_vars[56] != 22)
s.add(85 ^ bytes_vars[57] != 186)
s.add(85 ^ bytes_vars[57] != 13)
s.add(85 ^ bytes_vars[58] != 12)
s.add(85 ^ bytes_vars[58] != 77)
s.add(85 ^ bytes_vars[59] != 142)
s.add(85 ^ bytes_vars[59] != 194)
s.add(85 ^ bytes_vars[60] != 43)
s.add(85 ^ bytes_vars[60] != 130)
s.add(85 ^ bytes_vars[61] != 94)
s.add(85 ^ bytes_vars[61] != 239)
s.add(85 ^ bytes_vars[62] != 15)
s.add(85 ^ bytes_vars[62] != 246)
s.add(85 ^ bytes_vars[63] != 34)
s.add(85 ^ bytes_vars[63] != 135)
s.add(85 ^ bytes_vars[64] != 158)
s.add(85 ^ bytes_vars[64] != 50)
s.add(85 ^ bytes_vars[65] != 28)
s.add(85 ^ bytes_vars[65] != 215)
s.add(85 ^ bytes_vars[66] != 146)
s.add(85 ^ bytes_vars[66] != 51)
s.add(85 ^ bytes_vars[67] != 63)
s.add(85 ^ bytes_vars[67] != 55)
s.add(85 ^ bytes_vars[68] != 8)
s.add(85 ^ bytes_vars[68] != 135)
s.add(85 ^ bytes_vars[69] != 30)
s.add(85 ^ bytes_vars[69] != 241)
s.add(85 ^ bytes_vars[70] != 209)
s.add(85 ^ bytes_vars[70] != 41)
s.add(85 ^ bytes_vars[71] != 3)
s.add(85 ^ bytes_vars[71] != 128)
s.add(85 ^ bytes_vars[72] != 219)
s.add(85 ^ bytes_vars[72] != 61)
s.add(85 ^ bytes_vars[73] != 17)
s.add(85 ^ bytes_vars[73] != 61)
s.add(85 ^ bytes_vars[74] != 193)
s.add(85 ^ bytes_vars[74] != 45)
s.add(85 ^ bytes_vars[75] != 35)
s.add(85 ^ bytes_vars[75] != 25)
s.add(85 ^ bytes_vars[76] != 30)
s.add(85 ^ bytes_vars[76] != 88)
s.add(85 ^ bytes_vars[77] != 22)
s.add(85 ^ bytes_vars[77] != 223)
s.add(85 ^ bytes_vars[78] != 163)
s.add(85 ^ bytes_vars[78] != 6)
s.add(85 ^ bytes_vars[79] != 104)
s.add(85 ^ bytes_vars[79] != 186)
s.add(85 ^ bytes_vars[80] != 236)
s.add(85 ^ bytes_vars[80] != 56)
s.add(85 ^ bytes_vars[81] != 7)
s.add(85 ^ bytes_vars[81] != 242)
s.add(85 ^ bytes_vars[82] != 228)
s.add(85 ^ bytes_vars[82] != 32)
s.add(85 ^ bytes_vars[83] != 197)
s.add(85 ^ bytes_vars[83] != 31)
s.add(85 ^ bytes_vars[84] != 3)
# First constraint: (bytes_vars[6:3]) ^ 298697263 == 2108416586
s.add((Concat(bytes_vars[6], bytes_vars[5], bytes_vars[4], bytes_vars[3]) ^ BitVecVal(298697263, 32)) & 0xFFFFFFFF == BitVecVal(2108416586, 32))

# Second constraint: (bytes_vars[13:10]) + 383041523 == 2448764514
s.add((Concat(bytes_vars[13], bytes_vars[12], bytes_vars[11], bytes_vars[10]) + BitVecVal(383041523, 32)) & 0xFFFFFFFF == BitVecVal(2448764514, 32))

# Third constraint: (bytes_vars[20:17]) - 323157430 == 1412131772
s.add((Concat(bytes_vars[20], bytes_vars[19], bytes_vars[18], bytes_vars[17]) - BitVecVal(323157430, 32)) & 0xFFFFFFFF == BitVecVal(1412131772, 32))

# Fourth constraint: (bytes_vars[25:22]) ^ 372102464 == 1879700858
s.add((Concat(bytes_vars[25], bytes_vars[24], bytes_vars[23], bytes_vars[22]) ^ BitVecVal(372102464, 32)) & 0xFFFFFFFF == BitVecVal(1879700858, 32))

# Fifth constraint: (bytes_vars[31:28]) - 419186860 == 959764852
s.add((Concat(bytes_vars[31], bytes_vars[30], bytes_vars[29], bytes_vars[28]) - BitVecVal(419186860, 32)) & 0xFFFFFFFF == BitVecVal(959764852, 32))

# Sixth constraint: (bytes_vars[40:37]) + 367943707 == 1228527996
s.add((Concat(bytes_vars[40], bytes_vars[39], bytes_vars[38], bytes_vars[37]) + BitVecVal(367943707, 32)) == BitVecVal(1228527996, 32))

# Seventh constraint: (bytes_vars[44:41]) + 404880684 == 1699114335
s.add((Concat(bytes_vars[44], bytes_vars[43], bytes_vars[42], bytes_vars[41]) + BitVecVal(404880684, 32)) == BitVecVal(1699114335, 32))

# Eighth constraint: (bytes_vars[49:46]) - 412326611 == 1503714457
s.add((Concat(bytes_vars[49], bytes_vars[48], bytes_vars[47], bytes_vars[46]) - BitVecVal(412326611, 32)) == BitVecVal(1503714457, 32))

# Ninth constraint: (bytes_vars[55:52]) ^ 425706662 == 1495724241
s.add((Concat(bytes_vars[55], bytes_vars[54], bytes_vars[53], bytes_vars[52]) ^ BitVecVal(425706662, 32)) == BitVecVal(1495724241, 32))

# Tenth constraint: (bytes_vars[62:59]) ^ 512952669 == 1908304943
s.add((Concat(bytes_vars[62], bytes_vars[61], bytes_vars[60], bytes_vars[59]) ^ BitVecVal(512952669, 32)) == BitVecVal(1908304943, 32))

# Eleventh constraint: (bytes_vars[69:66]) ^ 310886682 == 849718389
s.add((Concat(bytes_vars[69], bytes_vars[68], bytes_vars[67], bytes_vars[66]) ^ BitVecVal(310886682, 32)) == BitVecVal(849718389, 32))

# Twelfth constraint: (bytes_vars[73:70]) + 349203301 == 2034162376
s.add((Concat(bytes_vars[73], bytes_vars[72], bytes_vars[71], bytes_vars[70]) + BitVecVal(349203301, 32)) == BitVecVal(2034162376, 32))

# Thirteenth constraint: (bytes_vars[83:80]) - 473886976 == 69677856
s.add((Concat(bytes_vars[83], bytes_vars[82], bytes_vars[81], bytes_vars[80]) - BitVecVal(473886976, 32)) == BitVecVal(69677856, 32))

# Proceeding with the MD5, SHA256, and CRC32 hash constraints

# Function to find MD5 matches for two-byte values
def find_md5_matches(expected_md5):
    matches = []
    for b0 in range(256):
        for b1 in range(256):
            data = bytes([b0, b1])
            md5_hash = hashlib.md5(data).hexdigest()
            if md5_hash == expected_md5:
                matches.append((b0, b1))
    return matches

# Function to find SHA256 matches for two-byte values
def find_sha256_matches(expected_sha256):
    matches = []
    for b0 in range(256):
        for b1 in range(256):
            data = bytes([b0, b1])
            sha256_hash = hashlib.sha256(data).hexdigest()
            if sha256_hash == expected_sha256:
                matches.append((b0, b1))
    return matches

# Function to find CRC32 matches for two-byte values
def find_crc32_matches(expected_crc32):
    matches = []
    for b0 in range(256):
        for b1 in range(256):
            data = bytes([b0, b1])
            crc32_hash = binascii.crc32(data) & 0xFFFFFFFF  # Ensure unsigned 32-bit representation
            if crc32_hash == expected_crc32:
                matches.append((b0, b1))
    return matches

# MD5 constraint at (0, filesize)
expected_md5_0_filesize = "b7dc94ca98aa58dabb5404541c812db2"
s.add(Or([And(bytes_vars[0] == b0, bytes_vars[1] == b1) for b0, b1 in find_md5_matches(expected_md5_0_filesize)]))

# Additional MD5 constraints based on offsets
additional_md5_constraints = [
    (0, 2, "89484b14b36a8d5329426a3d944d2983"),      # MD5 at offset 0 (first two bytes)
    (32, 2, "738a656e8e8ec272ca17cd51e12f558b"),     # MD5 at offset 32
    (50, 2, "657dae0913ee12be6fb2a6f687aae1c7"),     # MD5 at offset 50
    (76, 2, "f98ed07a4d5f50f7de1410d905f1477f"),     # MD5 at offset 76
]
for offset, size, expected_md5 in additional_md5_constraints:
    matches_md5 = find_md5_matches(expected_md5)
    if matches_md5:
        s.add(Or([And(bytes_vars[offset] == b0, bytes_vars[offset + 1] == b1) for b0, b1 in matches_md5]))

# SHA256 constraints based on offsets
additional_sha256_constraints = [
    (14, 2, "403d5f23d149670348b147a15eeb7010914701a7e99aad2e43f90cfa0325c76f"), # SHA256 at offset 14
    (56, 2, "593f2d04aab251f60c9e4b8bbc1e05a34e920980ec08351a18459b2bc7dbf2f6")  # SHA256 at offset 56
]
for offset, size, expected_sha256 in additional_sha256_constraints:
    matches_sha256 = find_sha256_matches(expected_sha256)
    if matches_sha256:
        s.add(Or([And(bytes_vars[offset] == b0, bytes_vars[offset + 1] == b1) for b0, b1 in matches_sha256]))

# CRC32 constraints based on offsets
additional_crc32_constraints = [
    (8, 2, 0x61089c5c),   # CRC32 at offset 8
    (34, 2, 0x5888fc1b),  # CRC32 at offset 34
    (63, 2, 0x66715919),  # CRC32 at offset 63
    (78, 2, 0x7cab8d64)   # CRC32 at offset 78
]
for offset, size, expected_crc32 in additional_crc32_constraints:
    matches_crc32 = find_crc32_matches(expected_crc32)
    if matches_crc32:
        s.add(Or([And(bytes_vars[offset] == b0, bytes_vars[offset + 1] == b1) for b0, b1 in matches_crc32]))

# Solve and validate the solution
if s.check() == sat:
    m = s.model()
    byte_array = [m.evaluate(bv, model_completion=True).as_long() for bv in bytes_vars]
    # Write the byte array to a file
    with open("solution.bin", "wb") as f:
        f.write(bytearray(byte_array))
    print("Byte array written to 'solution.bin'")
    # Verify MD5 hash
    md5_hash = hashlib.md5(bytes(byte_array)).hexdigest()
    if md5_hash == expected_md5_0_filesize:
        print("Solution found!")
        print("Byte array:", byte_array)
else:
    print("No solution found!")
