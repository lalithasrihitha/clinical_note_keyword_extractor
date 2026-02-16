def clean_text(text):
        """  makes text easier to search
                - everything lowercase
                - no extra spaces

                ex:
                INPUT: "  HELLOOO   DOCTOR  "
                OUTPUT: "hello doctor"
        """
    #step1 : making everything lowercase
        text = text.lower()
    #step2: removing spaces from start and end
        text = text.strip()
    #step3:replace multiple space with only single space
        while '  ' in text:
            text  = text.replace('  ', ' ')

        return text

 #testing the function

test_texts = ["PATIENT   has     JAUNDICE",
             "DOCTOR   IS   very    busy  ",
             "THE NURSES ARE ON   A   HOLIDAY   TODAY  "
             ]

for test_text in test_texts:
    result = clean_text(test_text)
    print("BEFORE:" ,test_text)
    print(result)


