import openai
import hjson
import streamlit as st
import os
import subprocess


st.title('Laurens Awesome Coding tool')
st.write('''
This is a code generation program that takes in natural language text and converts it to programmming language commands. 
''')
st.write('Select the programming language you want to generate to:')
language = st.selectbox('', ('Python', 'C#', 'JavaScript', 'Go', 'Perl', 'PHP', 'Ruby', 'Swift', 'TypeScript', 'SQL', 'Shell'))

openai.api_key = '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'


input_text = st.text_area('Enter your question')




if st.button('Submit'):

    response = openai.Completion.create(
      model="code-davinci-002",
      temperature=.4,
      max_tokens=6500,
      prompt=language + " " + input_text,
      top_p=1,
      frequency_penalty=.4,
      presence_penalty=.3
    )

    hjson.dump(response, open("response.json", "w"))

    res=response['choices'][0]['text']

    st.code(res)

    if st.button("Run"):
      st.code("Running...")
      st.code(subprocess.run([res], shell=True))

if st.button("Restart"):
  st.write("Restarted...")
  os.system("python main.py")
