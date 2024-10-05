def izracunaj_godine(godine1,godine2):
    razlika_u_godinama=godine1-godine2
    if(razlika_u_godinama>0):
        print("prvi je stariji")
    elif(razlika_u_godinama<0):
        print("drugi je stariji")
    else:
        print("obojica su isto godiste")