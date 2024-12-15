from flask import flash

def validate_cryptography1(flag):
    """
    Validasi flag untuk tantangan Cryptography 1.
    """
    correct_flag = "capstone{CL4SS1CC1PH3R}"
    if flag == correct_flag:
        flash("Congratulations! You solved the Cryptography 1 challenge!", "success")
        return True
    else:
        flash("Incorrect flag. Try again!", "error")
        return False

def validate_number(flag):
    """
    Validasi flag untuk tantangan Number.
    """
    correct_flag = "capstone{IDKTHEFLAG}"
    if flag == correct_flag:
        flash("Congratulations! You solved the Number challenge!", "success")
        return True
    else:
        flash("Incorrect flag. Try again!", "error")
        return False
