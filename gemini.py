import google.generativeai as genai #pip install google-generativeai
genai.configure(api_key="your_api_key") #use this tutorial to get your api key https://youtu.be/OVnnVnLZPEo?si=qjWr_M2MW9wF_grP
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("hello")
generated_text = response._result.candidates[0].content.parts[0].text
print(generated_text)
