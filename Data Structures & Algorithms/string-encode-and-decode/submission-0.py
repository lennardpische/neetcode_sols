class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [] 
        for string in strs:
            delimiter_enc = f"{len(string)}#{string}"
            encoded.append(delimiter_enc)
        return "".join(encoded)
    
    def decode(self, s: str) -> List[str]:
        idx = 0
        decoded = []
        while idx < len(s):
            delim_idx = s.find("#", idx)
            string_length = int(s[idx:delim_idx])
            decoded.append(s[delim_idx+1:delim_idx+string_length+1])
            idx = delim_idx + string_length +1 
        return decoded
            

