import openai
import json
import requests
import streamlit as st
import configparser


# grab credentials from secure folder
config = configparser.ConfigParser()
config.read("config.txt")
api_key = config.get("configuration","openai_api")



openai.api_key = api_key

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content


st.title('Book Summarizer With ChatGPT')

    
if st.button('Analyze'):
    with st.spinner('Getting book summary...'):
        chatGPTPrompt = f"""Write a thorough yet concise summary of This Naked Mind by Annie Grace.

                            concentrate on only the most important takeaways and primary points from the book that together will give me a solid overview and understanding of the book and its topic


                            Include all of the following in your summary:

                            Main topic or theme of the book
                            Key ideas or arguments presented
                            Chapter titles or main sections of the book with a paragraph on each
                            Key takeaways or conclusions
                            Author's background and qualifications
                            Comparison to other books on the same subject
                            Target audience or intended readership
                            Reception or critical response to the book
                            Publisher and First Published Date
                            Recommendations [Other similar books on the same topic]

                            To sum up:  The book's biggest Takeaway and point in a singular sentence

                            OUTPUT: Markdown format with #Headings, ##H2, ###H3, + bullet points, + sub-bullet points"""
    
        analysis = BasicGeneration(chatGPTPrompt)
        st.text_area("Analysis", analysis,
                    height=500)
        st.success('Done!')








    
    

    
    







