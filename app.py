import from langchain.chains import LLMChain
import from langchain.llms import OpenAI
import from langchain.prompts import PromptTemplate

# Initialize the OpenAI model with your API key
llm = OpenAI(api_key='sk-4Yrq0ICDnFpHbFhP7qaEAV97-HiEBQDyEash8AjxVVT3BlbkFJ4DOsXwAVLGgDGFjCQzL0NlKwDV6YFN_sE224DQLlgA')

# Define a prompt template for querying
prompt_template = PromptTemplate(
    input_variables=["data_description", "question"],
    template="""
    You are a data analyst. Here is the data you have:
    {data_decription}

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
    data_description = "Welcome to KidzCareHub, your trusted pediatric care assistant. I’m Rhea, here to provide you with helpful information and advice on your child's health, nutrition, development, and well-being. Whether you have questions about common childhood illnesses, developmental milestones, or general parenting tips, I'm here to help guide you with reliable information. Please remember, while I strive to offer accurate and helpful guidance, it’s always best to consult with a healthcare professional for medical advice and treatment."
    while True:
        question = input("Enter A Question \n")
        answer = get_response(data_description, question)

        print(answer)

        if question == "exit":

            break
