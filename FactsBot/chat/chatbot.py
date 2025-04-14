from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv()

llm = ChatOpenAI()
embeddings = OpenAIEmbeddings()

db = Chroma(
    embedding_function=embeddings,
    persist_directory="embeddings_db",
)

retriever = TextLoader("facts.txt").load_and_split(
    text_splitter=CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=0
    )
)

chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
)

class Chatbot:
    def send_message(self, message: str) -> str:
        print(chain.run(message))
        return ""
