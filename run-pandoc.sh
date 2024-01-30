
#MARKDOWNFILES="$(printf '"./%s" ' */*.md)"
#pandoc -f markdown -o "output/cosmos-db-openai-python-dev-guide.docx" -s $MARKDOWNFILES

pandoc -f markdown -o "cosmos-db-openai-python-dev-guide.docx" -s \
    "./00_Introduction/README.md" \
    "./01_Azure_Overview/README.md" \
    "./02_Overview_Cosmos_DB/README.md" \
    "./03_Overview_Azure_OpenAI/README.md" \
    "./04_Overview_AI_Concepts/README.md" \
    "./05_Explore_OpenAI_models/README.md" \
    "./06_Provision_Azure_Resources/README.md" \
    "./07_Create_First_Cosmos_DB_Project/README.md" \
    "./08_Load_Data/README.md" \
    "./09_Vector_Search_Cosmos_DB/README.md" \
    "./10_LangChain/README.md" \
    "./11_Backend_API/README.md" \
    "./12_User_Interface/README.md" 