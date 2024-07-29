from survey import AnonymousSurvey

#Визначити запитання та створити опитування.
question = "Which foreign country did you visit first?"
my_survey = AnonymousSurvey(question)

#Показати запитання та зберегти відповіді на нього.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Write country country: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#Показати результати опитування.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_result()







