alphabet=['a','b','c','d','f','e','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
        shift_amount*=-1
    
    for letter in original_text:

        if letter not in original_text:
            output_text +=letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"here is the {encode_or_decode}d result:{output_text}")

should_continue=True
while should_continue:
    direction = input("type 'encode' to encrypt ,type 'decode' to decrypt").lower()
    text = input("type ur msg:").lower()
    shift=int(input("number of shifts:"))
    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart=input("type 'yes' if you want to continue else type'no'").lower()
    if restart=="no":
        should_continue=False
        print("ok")