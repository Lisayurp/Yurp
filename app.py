from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Initialize the OpenAI model with your API key
llm = OpenAI(api_key='sk-4Yrq0ICDnFpHbFhP7qaEAV97-HiEBQDyEash8AjxVVT3BlbkFJ4DOsXwAVLGgDGFjCQzL0NlKwDV6YFN_sE224DQLlgA')

# Define a prompt template for querying
prompt_template = PromptTemplate(
    input_variables=["data_description", "question"],
    template="""
    You are a data analyst. Here is the data you have:
    {data_description}

    Based on this data, answer the question: {question}
    """
)

# Create a LangChain
chain = LLMChain(llm=llm, prompt=prompt_template)

def get_response(data_description, question):
    # Running the chain to get a response based on the data description and a question
    response = chain.run(data_description=data_description, question=question)
    return response

# Example usage
if __name__ == "__main__":
    data_description = "Data includes various facts about Pediatric care,  General Health Questions"
    while True:
        question = input("Enter A Question \n")
        answer = get_response(data_description, question)

        print(answer)

        if question == "exit":

            break
