def is_valid(combination):
    diff=0
    for brack in combination:
        if brack=='(':
            diff+=1
        else:
            if diff==0:
                return False
            else:
                diff-=1
    return diff==0
            