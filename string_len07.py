def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    if len(s1)%2!=0:
        s1
    else:
        s1=""
    if len(s2)%2!=0:
        s2 
    else:
        s2="" 
    if len(s3)%2!=0:
        s3 
    else: 
        s3=""

    
    return '"['+s1+s2+s3+']"' 
print(main('code','coder','python'))