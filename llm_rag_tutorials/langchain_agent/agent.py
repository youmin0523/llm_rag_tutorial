# 랭체인 에이전트는 LLM이 주어진 목적을 달성하기 위해 여러 개의 도구(Tool)을 순차적으로 선택하고 실행하도록 구성된 동적 실행 엔진
# 에이전트는 사용자의 입력에 따라 어떤 도구를 사용할지 스스로 결정하고, 각 도구에서 얻은 정보를 바탕으로 다음 행동을 계획하여 최종 응답을 생성


# 시스템의 주요 구성 요소


# 1. LLM: 시스템의 중심으로, 사용자가 입력한 질문을 이해하고 적절한 도구를 호출해 데이터를 처리한다.
# 2. Parser: LLM이 사용자 질문을 분석한 후 적절한 도구를 호출하는 역할을 한다. 예를 들어 논문 검색과 관련된 질문을 받으면 지정된 논문 API를 호출하는 방식이다.
# 3. Tools: 시스템에서 활용되는 실제 API들이며 각각의 툴은 특정한 목적을 가지고 데이터를 처리한다.
# 4. Observation: 툴이 반환한 결과를 LLM이 다시 분석하고 해석되는 단계다. 각 툴이 제공한 데이터를 바탕으로 LLM은 최종적인 답변을 만든다.
# 5. 최종 답변: LLM이 도구로부터 받은 데이터를 바탕으로 사용자의 질문에 대한 답변을 생성하는 단계다. 사용자가 원하는 정보를 얻을 때까지, 이 과정은 툴 호출과 관찰 단계를 반복할 수 있다.


# LangChain Hub
# 프롬프트, 체인, 에이전트 등 랭체인의 핵심 구성 요소들을 공유하고 탐색하며 관리할 수 있는 오픈 커뮤니티 플랫폼이다.
# 이를 통해 사용자는 실무에 활용 가능한 다양한 프롬프트와 체인을 빠르게 확인하고 직접 다운로드하거나, 자신이 작성한 프롬프트를 업로드하여 기여할 수 있으며, 파이썬 또는 다른 SDK를 통해 손쉽게 push/pull 기능을 사용할 수 있다.

# 필요 모듈 설치


# agent 생성을 취한 모듈
from langchain_classic.agents import AgentExecutor


# 벡터 DB를 agent에게 전달하기 위한 tool
from langchain_classic.agents import create_openai_tools_agent


# 랭체인 허브
from langchain_classic import hub


# arXiv 논문 검색을 위한 tool
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun


# 네이버 뉴스에서 최신 기사를 로드하고 이를 벡터화하여 검색이 가능한 형태로 만든다
# OpenAI의 임베딩을 사용하여 FAISS 벡터 스토어에 저장하고, 이 데이터를 검색할 수 있다.


# 벡터 DB 구축 및 검색 도구
from langchain_classic.tools.retriever import create_retriever_tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings


# 벡터 DB 모듈 및 웹 크롤링 모듈
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader


# 질의 주제 검색: 위키피디아
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun


# OpenAI 모듈
from langchain_openai import ChatOpenAI


# OpenAI Key
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# 모델 구성
openai = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)
