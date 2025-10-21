import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

st.title("LangChain LLM App")

# ラジオボタンで専門家の種類を選択
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ("サッカーに関する専門家", "野球に関する専門家")
)

user_input = st.text_input("プロンプトを入力してください:")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

if st.button("送信"):
    if not user_input:
        st.warning("プロンプトを入力してください！")
    else:
        # 専門家の種類に応じたシステムメッセージを設定
        if expert_type == "サッカーに関する専門家":
            system_message = "You are an expert in soccer."
        elif expert_type == "野球に関する専門家":
            system_message = "You are an expert in baseball."

        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=user_input),
        ]
        result = llm.invoke(messages)  
        st.subheader("LLMの応答:")
        st.write(result.content)