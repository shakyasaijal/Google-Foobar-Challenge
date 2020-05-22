def solution(s):
    # ASCII in decimal
    # Because lance and janice is a computer and they are messaging each other during duty. Then obviously they dont have time for understanding ascii or using anyother python libraries.
    # Keep it simple
    alpha_normal = [i for i in range(97, 123)]
    alpha_reverse = alpha_normal[::-1]

    # Map
    normal_reverse = {alpha_normal[i]: alpha_reverse[i]
                      for i in range(len(alpha_normal))}

    # Decrypt
    decrypt = [chr(normal_reverse[ord(i)])
               if normal_reverse.has_key(ord(i)) else i for i in s]

    return ''.join(decrypt)