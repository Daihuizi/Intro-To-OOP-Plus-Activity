# add your get_student_with_more_classes function here!

def get_student_with_more_classes(s1, s2):
    if s1.get_num_classes() > s2.get_num_classes():
        return s1.name
    elif s2.get_num_classes() > s1.get_num_classes():
        return s2.name
    else:
        return None 
    #My edge case is when both students have the same number of classes. I decided to return None.


