# MARKDOWNFILES="$(printf './%s ' */*.md)"
# IMAGEFOLDERS="$(for dir in */; do echo "\"./$(basename "./$dir")\":"; done)"
# pandoc -f markdown --toc \
#     -t docx \
#     -o "cosmos-db-openai-python-dev-guide.docx" \
#     --resource-path $IMAGEFOLDERS \
#     -s $MARKDOWNFILES  


pandoc -f markdown --toc \
    -t docx \
    -o "cosmos-db-openai-python-dev-guide.docx" \
    --resource-path "./00_Introduction":"./01_Azure_Overview":"./02_Overview_Cosmos_DB":"./03_Overview_Azure_OpenAI":"./04_Overview_AI_Concepts":"./05_Explore_OpenAI_models":"./06_Provision_Azure_Resources":"./07_Create_First_Cosmos_DB_Project":"./08_Load_Data":"./09_Vector_Search_Cosmos_DB":"./10_LangChain":"./11_Backend_API":"./12_User_Interface" \
    -s "./00_Introduction/README.md" \
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
